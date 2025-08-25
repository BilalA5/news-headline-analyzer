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
headlines = [headline.get_text() for headline in soup.find_all('h1' or 'h2' or 'h3')]

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
# using matplotlib to visualize the lengths of the headlines
if headlines:
    plt.figure(figsize=(10, 5))
    plt.bar(df['Headlines'], df['Length'], color='blue')
    plt.xlabel('Headlines')
    plt.ylabel('Length of Headline')
    plt.title('Length of Headlines')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
    # Save the DataFrame to an Excel file
    df.to_excel('headlines.xlsx', index=False)
    print("DataFrame saved to 'headlines.xlsx'.")
else:
    print("No headlines to visualize.")


