from dotenv import load_dotenv
import os
import pandas as pd
from entsoe import EntsoePandasClient

load_dotenv(".env")

client = EntsoePandasClient(
    api_key=os.getenv("ENTSOE_API_KEY")
)

start = pd.Timestamp("2025-01-01", tz="Europe/Oslo")
end = pd.Timestamp("2026-01-01", tz="Europe/Oslo")

areas = ["NO_1", "NO_2", "NO_3", "NO_4", "NO_5"]

for area in areas:

    prices = client.query_day_ahead_prices(
        country_code=area,
        start=start,
        end=end
    )

    filename = f"prices/{area.lower()}_prices_2025.csv"

    prices.to_csv(filename)

    print(f"Saved {filename}")