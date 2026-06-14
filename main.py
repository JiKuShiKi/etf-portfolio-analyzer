import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from src.analyzer import load_portfolio, analyze_portfolio
from src.display import print_portfolio_table, plot_portfolio_chart

def main():
    """Main function that brings everything together"""
    print("Lade Portfolio...")
    portfolio = load_portfolio()
    results = analyze_portfolio(portfolio)
    print_portfolio_table(results)
    plot_portfolio_chart(results)

if __name__ == "__main__":
    main()
