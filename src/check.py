from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    "sqlite:///bluestock_mf.db"
)

tables = [
    "fund_master",
    "nav_history",
    "investor_transactions",
    "scheme_performance"
]

for table in tables:

    query = f"""
    SELECT COUNT(*)
    as rows
    FROM {table}
    """

    print(
        table,
        pd.read_sql(query, engine)
    )