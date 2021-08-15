import requests
from datetime import datetime
import os

pix_token = os.environ.get("PIX_TOKEN")
pix_url = "https://pixe.la/v1/users"
user = "hiten8"
pix2_url = f"{pix_url}/{user}/graphs"
pix_id = "cycle"
pi_name = "Cycling Graph"
pix3_url = f"{pix2_url}/{pix_id}"
today_date = datetime.now().strftime("%Y%m%d")
pix4_url = f"{pix3_url}/{today_date}"

pix_json = {
    "token": pix_token,
    "username": user,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
head = {
    "X-USER-TOKEN": pix_token
}
pix2_json = {
    "id": pix_id,
    "name": pi_name,
    "unit": "Km",
    "type": "float",
    "color": "momiji",
}

pix3_json = {
    "date": today_date,
    "quantity": "10"
}
pix4_json = {
    "quantity": "15",
}

response = requests.post(url=pix3_url, json=pix3_json, headers=head)
print(response.text)
