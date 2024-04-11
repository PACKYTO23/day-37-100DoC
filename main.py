import requests
from datetime import datetime

USERNAME = "franciscogp"
TOKEN = "1234qwertyuiop56789"
GRAPH_ID = "graph1"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)

# print(response.text)

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_params = {
    "id": GRAPH_ID,
    "name": "Writing Graph",
    "unit": "Characters",
    "type": "int",
    "color": "momiji",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=GRAPH_ENDPOINT, json=graph_params, headers=headers)

# print(response.text)

POST_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

# print(today.strftime("%Y%m%d"))

post_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many characters did you write today?: "),
}

response = requests.post(url=POST_ENDPOINT, json=post_params, headers=headers)

print(response.text)

april_9_2024 = datetime(year=2024, month=4, day=9)
date_change = april_9_2024.strftime("%Y%m%d")

PUT_DELETE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{date_change}"

put_params = {
    "quantity": "750",
}

# response = requests.put(url=PUT_DELETE_ENDPOINT, json=put_params, headers=headers)

# print(response.text)

april_8_2024 = datetime(year=2024, month=4, day=8)
date_change = april_8_2024.strftime("%Y%m%d")

# response = requests.delete(url=PUT_DELETE_ENDPOINT, headers=headers)

# print(response.text)

# website = "https://pixe.la/v1/users/franciscogp/graphs/graph1.html"
