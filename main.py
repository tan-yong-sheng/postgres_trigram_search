from sqlalchemy import func
from sqlalchemy.sql.expression import desc

from db_connection import Base, db_context, engine
from models import StockSymbolOrm
from schemas import StockSymbolReturn

search_term = "genting malaysia"
exchange_market = "Bursa"

# Create the tables in database
Base.metadata.create_all(engine)

with db_context() as session:
    # Conditions for similarity matching
    similarity_condition = (
        (func.similarity(StockSymbolOrm.stock_code, search_term) > 0.2)
        | (func.similarity(StockSymbolOrm.stock_symbol, search_term) > 0.2)
        | (func.similarity(StockSymbolOrm.company_name, search_term) > 0.3)
    ) & (StockSymbolOrm.exchange == exchange_market)

    # Rank score based on average similarity
    rank_score = (
        func.similarity(StockSymbolOrm.stock_code, search_term)
        + func.similarity(StockSymbolOrm.stock_symbol, search_term)
        + func.similarity(StockSymbolOrm.company_name, search_term) * 1.1
    )

    # Perform trigram search based on the conditions defined above
    results = (
        session.query(StockSymbolOrm)
        .filter(similarity_condition)
        .order_by(desc(rank_score))
        .all()
    )

    results = [StockSymbolReturn(**result.__dict__) for result in results]
    print("Results: ", results)
