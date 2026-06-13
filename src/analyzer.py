import json
import yfinance as yf
from pathlib import Path

def load_portfolio(path: str = "data/portfolio.json") -> list:
    """loads portfolio from json"""
    with open(Path(path), "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["portfolio"]

def get_current_price(ticker: str) -> float | None:
    """gets current price from yahoo finance"""
    try:
        etf = yf.Ticker(ticker)
        return round(etf.fast_info["last_price"], 2)
    except Exception as e:
        print(f"Fehler beii {ticker}: {e}")
        return None

def analyze_portfolio(portfolio: list) -> list:
    """calculating current price of all positions"""
    results = []
    for etf in portfolio:
        print(f"Lade Kurs für {etf["name"]}...")
        price = get_current_price(etf["ticker"])
        if price is not None:
            total_value = round(price * etf["shares"], 2)
            results.append({
                "name": etf["name"],
                "ticker": etf["ticker"],
                "shares": etf["shares"],
                "price": price,
                "total_value": total_value,
            })
        else:
            print(f"Überspringe {etf["name"]} (kein Kurs verfügbar")

    return results