import csv
import logging

from pydantic import ValidationError
from sqlalchemy.orm import Session

from db_connection import db_context
from models import StockSymbolOrm
from schemas import StockSymbolCreate

logger = logging.getLogger(__name__)


def check_existing_ticker(db: Session, stock_symbol: str):
    existing_ticker = (
        db.query(StockSymbolOrm)
        .filter(StockSymbolOrm.stock_symbol == stock_symbol)
        .first()
    )
    if existing_ticker:
        logger.info(f"The stock code: {stock_symbol} already exists")
    return existing_ticker


def read_csv_file(file_path: str):
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        return list(reader)


def insert_ticker_csv_into_db(csv_file_path: str):
    rows = read_csv_file(csv_file_path)
    with db_context() as db_session:
        for row in rows:
            stock_symbol = row["stock_symbol"]
            existing_stock_code = check_existing_ticker(db_session, stock_symbol)
            if not existing_stock_code:
                try:
                    stock_symbol = StockSymbolCreate(**row)
                    stock_symbol = StockSymbolOrm(**stock_symbol.__dict__)
                    db_session.add(stock_symbol)
                    db_session.commit()
                except ValidationError as e:
                    logger.error("Validation error: ", e)
                    print(e)
                    db_session.rollback()


if __name__ == "__main__":
    insert_ticker_csv_into_db("data/sgx_stock_list.csv")
    insert_ticker_csv_into_db("data/bursa_stock_list.csv")
