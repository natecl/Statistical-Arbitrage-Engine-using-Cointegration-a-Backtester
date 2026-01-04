import yaml
import pandas as pd
from pathlib import path

def main():
    universe = load_universe("config/universe.yaml")
    tickers = extract_tickers(universe)

    

def load_universe(path:str) -> dict:
    with open(path, 'r') as f:
        return yaml.safe_load(f)
    
def extract_tickers(universe: dict) -> list[str]:
    tickers : set[str] = set()

    for group in universe["universe"]:
        for ticker in group["tickers"]:
            tickers.add(ticker)

    return sorted(tickers)

def download_prices(ticker: str, start: str, end: str) -> pd.DataFrame:
    df = DATA_PROVIDER_CALL(ticker, start, end)

    df = df[["Adj Close"]]
    df.columns = ["price"]

    assert "price" in df.columns
    assert df.index.is_monotonic_increasing

    return df




if __name__ == "__main__":
    main()