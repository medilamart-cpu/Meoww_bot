import requests

url = "https://mayurbhajiya.petpooja.com/orders/getMenu"

data = {
    "search": "",
    "attributes_filter": ""
}

r = requests.post(url, data=data)

print(r.status_code)
print(r.text[:1000])
