import requests as rq

url = input("Enter a valid URL")

while True:
  if "http" in url:
    break
  else:
    url = input("Enter a valid URL")

response = rq.get(url)
html = response.text
