from datetime import datetime

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField


app = Flask(__name__)
app.config['SECRET_KEY'] = ''
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##CONFIGURE TABLE
class BlogPost(db.Model):
    # query = None
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route('/')
def get_all_posts():
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = BlogPost.query.get(index)
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/new_post", methods=["GET", "POST"])
def new_post():
    title = "New Post"
    if request.method == "POST":
        newpost = BlogPost(title=request.form["title"], date=datetime.now().strftime("%B %d, %Y"), body=request.form["body"],  author=request.form["author"], img_url= request.form["img_url"], subtitle=request.form["subtitle"])
        db.session.add(newpost)
        db.session.commit()
        return redirect("index.html")
    create_form = CreatePostForm()
    return render_template("make-post.html", form=create_form, title=title)


@app.route("/edit_post/<post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    title = "Edit Post"
    post_to_update = BlogPost.query.get(post_id)
    edit_form = CreatePostForm(
        title=post_to_update.title,
        subtitle=post_to_update.subtitle,
        img_url=post_to_update.img_url,
        author=post_to_update.author,
        body=post_to_update.body
    )
    if edit_form.validate_on_submit() and request.method == 'POST':
        post_to_update.title = edit_form.title.data
        post_to_update.subtitle = edit_form.subtitle.data
        post_to_update.body = edit_form.body.data
        post_to_update.author = edit_form.author.data
        post_to_update.img_url = edit_form.img_url.data
        db.session.commit()
        return redirect(url_for("show_post", index=post_to_update.id))
    return render_template("make-post.html", form=edit_form, title=title)


@app.route("/delete/<id>", methods=["GET", "POST"])
def delete(id):
    post_to_delete = BlogPost.query.get(id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for("get_all_posts"))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
