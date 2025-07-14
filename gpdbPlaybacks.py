import requests


url = "https://data.mixpanel.com/api/2.0/export?project_id=2928951&from_date=2025-01-01&to_date=2025-04-21&event=%5B%22common_play_pronunciation%22%5D&where=properties%5B%22organization_name%22%5D%20%3D%3D%20%22emerson.com%22"

headers = {
    "accept": "text/plain",
    "authorization": "Basic c2VydmljZS1hY2N0LXphdy42YTc3YWUubXAtc2VydmljZS1hY2NvdW50OkR1eXNYS09BUDNucVd0dG41QzJLWTlHQ1NPRzFyOU5Q"
}

response = requests.get(url, headers=headers)

print(response.text)
