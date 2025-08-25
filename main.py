import requests as rq
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

url = input("Enter a valid URL: ")

while True:
  if "http" in url:
    break
  else:
    url = input("URL must contain 'http'. Please enter a valid URL: ")

response = rq.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
headlines = [h.get_text(strip=True) for h in soup.find_all("h1")]

#Check if the scraper found any headlines (they exist)
if headlines:
  print("Headlines found on the page:")
  for idx, headline in enumerate(headlines, start=1):
    print(f"{idx}: {headline}")
else:
  print("No headlines found on the page.")

#using pandas to create a DataFrame from the headlines
df = pd.DataFrame(headlines, columns=['Headlines'])
# Display the DataFrame
print("\nDataFrame created from headlines:")
print(df)
#using numpy to perform some operations on the DataFrame
if not df.empty:
    df['Length'] = df['Headlines'].apply(len)
    print("\nDataFrame with headline lengths:")
    print(df)
# using matplotlib to visualize the lengths of the headlines via histogram
if headlines:
    plt.figure(figsize=(8,5))
    plt.hist(df['Length'], bins=10, color='skyblue', edgecolor='black')
    plt.xlabel('Length of Headline (characters)')
    plt.ylabel('Number of Headlines')
    plt.title('Distribution of Headline Lengths')
    plt.show()
    print("Visualization complete.")
else:
    print("No headlines to visualize.")
