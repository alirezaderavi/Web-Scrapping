# 📊 Web Scraping: Largest U.S. Companies by Revenue

This project demonstrates how to scrape data from Wikipedia using **Python** and **BeautifulSoup**. The goal is to extract structured information about the largest companies in the United States by revenue.

---

## 🚀 Project Overview

The script collects data from the Wikipedia page:

**"List of largest companies in the United States by revenue"**

It extracts the following fields:

* Rank
* Company Name
* Industry
* Revenue
* Revenue Growth
* Headquarters

The extracted data is then stored in a structured format using **Pandas** and exported as a CSV file.

---

## 🛠️ Technologies Used

* Python
* BeautifulSoup (bs4)
* Requests
* Pandas

---

## 📂 Project Structure

```
📁 project-folder
│── scrape_companies.py
│── us_companies_by_revenue.csv
│── README.md
```

---

## ⚙️ Installation

1. Clone the repository:

```
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

2. Install required libraries:

```
pip install requests beautifulsoup4 pandas
```

---

## ▶️ Usage

Run the script:

```
python WebScrapping.py
```

After execution, a CSV file will be generated:

```
us_companies_by_revenue.csv
```

---

## 🧠 How It Works

1. Sends an HTTP request to Wikipedia
2. Parses the HTML using BeautifulSoup
3. Locates the target table (`wikitable`)
4. Extracts rows and columns
5. Stores data in a Pandas DataFrame
6. Exports the data to CSV

---

## ⚠️ Notes & Troubleshooting

* If the script fails with:

  ```
  AttributeError: 'NoneType' object has no attribute 'find_all'
  ```

  it usually means the request was blocked.

* Fix by adding headers:

  ```python
  headers = {"User-Agent": "Mozilla/5.0"}
  ```

* Wikipedia page structure may change, requiring updates to the scraper.

---

## 📈 Example Output

| Rank | Name    | Industry   | Revenue | Revenue Growth | Headquarters |
| ---- | ------- | ---------- | ------- | -------------- | ------------ |
| 1    | Walmart | Retail     | $611B   | 6.7%           | Arkansas     |
| 2    | Amazon  | E-commerce | $513B   | 9.4%           | Washington   |

---

## 🔄 Alternative Approach

You can also use Pandas to scrape tables directly:

```python
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"
df = pd.read_html(url)[0]
```

---

## 📌 Future Improvements

* Clean and convert revenue to numeric format
* Handle missing or inconsistent data
* Automate periodic data updates
* Integrate with data analysis or ML pipelines

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repo and submit a pull request.

---

## 📄 License

This project is open-source and available under the MIT License.

---
