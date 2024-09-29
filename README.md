## Building Trigram Search for Stock Tickers with Python SQLAlchemy and PostgreSQL

(Note: Please read the setup guide at https://www.tanyongsheng.com/note/building-trigram-search-for-stock-tickers-with-python-sqlalchemy-and-postgresql/ for more details, and please rename `.env.sample` to `.env`)

1. `git clone https://github.com/tan-yong-sheng/postgres_trigram_search.git`

2. `docker compose up -d`

3. 

```bash
python -m virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

4. `python -m scrape_tickers`

5. `python -m insert_tickers_db`

6. `python -m main`


## Additional note:

Please feel free to adjust the parameters `search_term` or `exchange_market` in main.py file

  - search_term: str
  - exchange_market: enum('Bursa', 'SGD)


This is just a simple prototype project. Thanks for reading, and hope for more suggestions.
