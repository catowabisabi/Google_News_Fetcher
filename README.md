# Google News Fetcher 谷歌新聞擷取器

[English](#english) | [中文](#chinese)

<a name="english"></a>
## English

### Overview
Google News Fetcher is a Python-based tool designed to automatically collect and analyze financial news and company information from various sources including Google News, Wikipedia, and financial websites. It's particularly useful for investors and financial analysts who need to keep track of market news about specific companies.

### Features
- Fetch latest financial news from Google News
- Extract company information from Wikipedia
- Support for multiple stock tickers
- Automated data collection and storage
- Export data to CSV format
- Multi-source news aggregation

### Requirements
- Python 3.x
- Selenium WebDriver
- BeautifulSoup4
- Pandas
- Requests
- ChromeDriver

### Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/Google_News_Fetcher.git
cd Google_News_Fetcher
```

2. Install required packages:
```bash
pip install selenium beautifulsoup4 pandas requests
```

3. Download and setup ChromeDriver:
   - Download ChromeDriver that matches your Chrome browser version
   - Place the ChromeDriver executable in your system PATH

### Usage
The project contains three main modules:

1. Google News Scraper (`bs_google_news.py`):
```python
from bs_google_news import ingest_google_news
ingest_google_news()  # Fetches news for predefined stock tickers
```

2. Wikipedia Information Scraper (`bs_google_wiki.py`):
```python
from bs_google_wiki import ingest_wiki
ingest_wiki()  # Collects company information from Wikipedia
```

3. Financial News Crawler (`finanical_new.py`):
```python
# Runs automated browser-based news collection
python finanical_new.py
```

### Output
- News data is saved in CSV format in the `data_news` directory
- Each file is timestamped with the collection date
- Data includes: ticker symbols, news content, publisher information, and timestamps

---

<a name="chinese"></a>
## 中文

### 概述
Google News Fetcher 是一個基於 Python 的工具，專門用於自動收集和分析來自 Google 新聞、維基百科和財經網站的金融新聞和公司資訊。這個工具特別適合需要追蹤特定公司市場新聞的投資者和金融分析師。

### 功能特點
- 從 Google 新聞獲取最新財經新聞
- 從維基百科擷取公司資訊
- 支援多個股票代碼
- 自動化數據收集和存儲
- 匯出數據為 CSV 格式
- 多來源新聞聚合

### 系統需求
- Python 3.x
- Selenium WebDriver
- BeautifulSoup4
- Pandas
- Requests
- ChromeDriver

### 安裝步驟
1. 克隆儲存庫：
```bash
git clone https://github.com/yourusername/Google_News_Fetcher.git
cd Google_News_Fetcher
```

2. 安裝所需套件：
```bash
pip install selenium beautifulsoup4 pandas requests
```

3. 下載並設置 ChromeDriver：
   - 下載與您的 Chrome 瀏覽器版本相匹配的 ChromeDriver
   - 將 ChromeDriver 執行檔放置在系統 PATH 中

### 使用方法
專案包含三個主要模組：

1. Google 新聞爬蟲 (`bs_google_news.py`):
```python
from bs_google_news import ingest_google_news
ingest_google_news()  # 擷取預定義股票代碼的新聞
```

2. 維基百科資訊爬蟲 (`bs_google_wiki.py`):
```python
from bs_google_wiki import ingest_wiki
ingest_wiki()  # 從維基百科收集公司資訊
```

3. 財經新聞爬蟲 (`finanical_new.py`):
```python
# 運行自動化瀏覽器新聞收集
python finanical_new.py
```

### 輸出結果
- 新聞數據以 CSV 格式保存在 `data_news` 目錄中
- 每個文件都帶有收集日期的時間戳
- 數據包括：股票代碼、新聞內容、發布者資訊和時間戳 