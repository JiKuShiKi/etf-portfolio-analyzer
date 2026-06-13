import matplotlib.pyplot as plt

def print_portfolio_table(results: list) -> None:
    """shows the portfolio as a tabel in the console"""
    print("\n===== ETF Portfolio Übersicht =====")
    print(f"{'ETF':<35} {'Kurs':>10} {'Anteile':>10} {'Wert':>10}")
    print("-" * 70)
    for etf in results:
        print(f"{etf['name']:<35} {etf['price']:>9.2f}€ {etf['shares']:>10.4f} {etf['total_value']:>9.2f}€")
    total = round(sum(etf["total_value"] for etf in results), 2)
    print("-" * 70)
    print(f"{'Gesamtwert':<35} {'':>10} {'':>10} {total:>9.2f}€")