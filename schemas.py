from typing import Optional

from pydantic import BaseModel


# define pydantic schemas
class StockSymbolSchema(BaseModel):
    stock_symbol: str
    company_name: str
    stock_code: str
    sector: str
    subsector: str
    mkt: str
    exchange: str
    company_description: Optional[str] = None


class StockSymbolCreate(StockSymbolSchema):
    pass


class StockSymbolReturn(StockSymbolSchema):
    id: int
