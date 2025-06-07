# INGESTION THROUGH WEB SCRAPING USING BEAUTIFULSOUP
def ingest_google_news():
    ticker_list = ['AAPL.O', 'LVS', 'COTY.K','JPM', 'XOM', '005930.KS']

    sep = '.'
    
    df = pd.DataFrame()
    t_news = []
    t_publisher = []
    t_urls = []
    t_dates = []
    t_tickers = []

    for t in ticker_list:
        news = []
        publisher = []
        urls = []
        dates = []
        tickers = []

        # cleaning ticker
        ticker = t
        t = t.split(sep, 1)[0]

        # set header by random user agent 
        r = requests.Session()
        headers = random_header()
        r.headers = headers
        # print(headers)

        # set query for google
        query = '{} stock news'.format(t)
        url = f"https://www.google.com/search?q={query}&tbm=nws&lr=lang_en&hl=en&sort=date&num=5"
        res = r.get(url, headers=headers)
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        
        links = soup.select(".dbsr a")
        for l in links:
            tickers.append(t)
            try:
                url_w = l.get("href")
                print(url_w)
                urls.append(url_w)
                dt = find_date(url_w)
                dates.append(dt)

                res = requests.get(url_w, headers=headers)
                parsed_article = bs4.BeautifulSoup(res.text,'lxml')
                paragraphs = parsed_article.find_all('p')

                article_text = ""
                for p in paragraphs:
                    article_text += p.text

            except Exception as e:
                article_text = ''

            news.append(article_text)

        sources = soup.select(".XTjFC g-img")
        for s in sources:
            publisher.append(s.next_sibling.lower())

        t_urls += urls
        t_news += news
        t_publisher += publisher
        t_dates += dates
        t_tickers += tickers

    df['ticker'] = t_tickers
    df['links'] = t_urls
    df['article_text'] = t_news
    df['publisher'] = t_publisher
    df['created_at'] = t_dates

    # import to csv
    today = date.today()
    d1 = today.strftime("%d%m%Y")
    df.to_csv(f'data_news/google_news_{d1}.csv')

    del news, publisher, urls, dates, tickers
    del t_news, t_publisher, t_urls, t_dates, t_ticker