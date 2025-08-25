# news-headline-analyzer
A Python project that scrapes live news headlines from any valid URL, analyzes headline lengths, and visualizes the distribution of headline lengths using BeautifulSoup, pandas, and matplotlib.

> ⚠️ **Disclaimer:** This project does **NOT** work on websites with paywalls. Only free and publicly accessible pages will return results.

---

## ✨ Features

- 🔍 **Live Web Scraping**: Extracts `<h1>` headlines from any valid URL.  
- 📊 **Headline Analysis**: Measures the length (number of characters) of each headline.  
- 📈 **Visualization**: Displays the distribution of headline lengths in a histogram.  
- 🗃️ **Data Export**: Saves the scraped headlines and lengths to an Excel file.  
- 📦 **Modular Design**: Easily extendable for additional analyses or visualizations.  

---

## 🛠️ Technologies Used

- `requests` – For making HTTP requests to web pages.  
- `BeautifulSoup` – For parsing and extracting headlines from HTML.  
- `pandas` – For creating and manipulating the DataFrame.  
- `numpy` – For basic operations on headline lengths.  
- `matplotlib` – For plotting histograms of headline lengths.  

---

## 🚀 How It Works

1. The program prompts the user to enter a valid URL.  
2. It scrapes all `<h1>` tags from the page.  
3. Headlines are displayed in the console and stored in a pandas DataFrame.  
4. The program calculates the character length of each headline.  
5. A histogram shows the distribution of headline lengths.  
6. Data is saved to `headlines.xlsx` for further use.  
