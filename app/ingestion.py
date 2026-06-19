import requests
from sqlalchemy import text

from app.database import engine

BASE_URL = "http://127.0.0.1:8000"


def ingest_customers():
    page = 1

    while True:
        # your existing customer code
        page += 1


def ingest_orders():
    page = 1

    while True:
        response = requests.get(
            f"{BASE_URL}/orders?page={page}&limit=1000"
        )

        orders = response.json()

        if not orders:
            break

        with engine.begin() as conn:
            for order in orders:
                conn.execute(
                    text("""
                        INSERT INTO ingested_orders
                        (id, customer_id, amount)
                        VALUES
                        (:id, :customer_id, :amount)
                        ON CONFLICT (id) DO NOTHING
                    """),
                    order
                )

        print(f"Inserted page {page}: {len(orders)} orders")

        page += 1


if __name__ == "__main__":
    ingest_orders()