import requests as rq
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import BeautifulSoup as bs

url = input("Enter a valid URL")

while True:
  if "http" in url:
    break
  else:
    url = input("Enter a valid URL")

response = rq.get(url)
html = response.text
soup = bs.BeautifulSoup(html, 'html.parser')
headlines = [headline.get_text() for headline in soup.find_all('h1')]

if headlines:
  print("Headlines found on the page:")
  for idx, headline in enumerate(headlines, start=1):
    print(f"{idx}: {headline}")
else:
  print("No headlines found on the page.")

# Example of using pandas to create a DataFrame from the headlines
df = pd.DataFrame(headlines, columns=['Headlines'])
# Display the DataFrame
print("\nDataFrame created from headlines:")
print(df)
# Example of using numpy to perform some operations on the DataFrame
if not df.empty:
    df['Length'] = df['Headlines'].apply(len)
    print("\nDataFrame with headline lengths:")
    print(df)
