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

load = client.query_load(
    country_code="NO",
    start=start,
    end=end
)

load.to_csv("load/forbruk_2025.csv")

print("Saved load/forbruk_2025.csv")