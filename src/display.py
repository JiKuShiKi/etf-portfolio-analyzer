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

def plot_portfolio_chart(results: list) -> None:
    """shows a pie chart of portfolio distribution."""
    labels = [etf["name"] for etf in results]
    values = [etf["total_value"] for etf in results]
    plt.figure(figsize=(8, 6))
    plt.pie(values, labels=labels, autopct="%1.1f%%", startangle=90)
    plt.title("Portfolio Verteilung")
    plt.tight_layout()
    plt.show()