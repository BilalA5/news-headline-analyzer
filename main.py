import requests as rq

url = input("Enter a valid url")

while true:
  if url.__contains__("http"):
    break
  else:
    url = input("Enter a valid url")

response = rq.get(url)
html = response.text
