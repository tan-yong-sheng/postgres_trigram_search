from sqlalchemy import Column, Index, Integer, String, Text, UniqueConstraint

from db_connection import Base


# Define the stock_symbol table
class StockSymbolOrm(Base):
    __tablename__ = "stocks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    stock_symbol = Column(String)
    company_name = Column(String)
    stock_code = Column(String)
    sector = Column(String)
    subsector = Column(String)
    mkt = Column(String)
    exchange = Column(String)
    company_description = Column(Text, nullable=True)

    __table_args__ = (
        UniqueConstraint("stock_symbol", "exchange", name="uq_stock_symbol_exchange"),
        Index(
            "idx_stock_symbol_trgm",
            "stock_symbol", # index for trigram search on stock_symbol field
            postgresql_using="gist",
            postgresql_ops={"stock_symbol": "gist_trgm_ops"},
        ),
        Index(
            "idx_stock_code_trgm",
            "stock_code", # index for trigram search on stock_code field
            postgresql_using="gist",
            postgresql_ops={"stock_code": "gist_trgm_ops"},
        ),
        Index(
            "idx_company_name_trgm",
            "company_name",  # index for trigram search on company_name field
            postgresql_using="gist",
            postgresql_ops={"company_name": "gist_trgm_ops"},
        ),
    )


if __name__ == "__main__":
    # Create the tables in database
    from db_connection import engine
    Base.metadata.create_all(engine)
