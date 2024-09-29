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
            "stock_symbol",
            postgresql_using="gin",
            postgresql_ops={"stock_symbol": "gin_trgm_ops"},
        ),
        Index(
            "idx_stock_code_trgm",
            "stock_code",  # index for trigram search on multiple fields
            postgresql_using="gin",
            postgresql_ops={"stock_code": "gin_trgm_ops"},
        ),
        Index(
            "idx_company_name_trgm",
            "company_name",  # index for trigram search on multiple fields
            postgresql_using="gin",
            postgresql_ops={"company_name": "gin_trgm_ops"},
        ),
    )


if __name__ == "__main__":
    # Create the tables in database
    Base.metadata.create_all()
