from fastapi import FastAPI
from sqlalchemy import text

from app.database import engine

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Backend Assignment Started"}


@app.get("/customers")
def get_customers(page: int = 1, limit: int = 100):

    offset = (page - 1) * limit

    with engine.connect() as conn:
        result = conn.execute(
            text(
                f"""
                SELECT *
                FROM customers
                ORDER BY id
                LIMIT {limit}
                OFFSET {offset}
                """
            )
        )

        customers = [dict(row._mapping) for row in result]

    return customers  

@app.get("/orders")
def get_orders(page: int = 1, limit: int = 100):

    offset = (page - 1) * limit

    with engine.connect() as conn:
        result = conn.execute(
            text(
                f"""
                SELECT *
                FROM orders
                ORDER BY id
                LIMIT {limit}
                OFFSET {offset}
                """
            )
        )

        orders = [dict(row._mapping) for row in result]

    return orders


@app.get("/refunds")
def get_refunds(page: int = 1, limit: int = 100):

    offset = (page - 1) * limit

    with engine.connect() as conn:
        result = conn.execute(
            text(
                f"""
                SELECT *
                FROM refunds
                ORDER BY id
                LIMIT {limit}
                OFFSET {offset}
                """
            )
        )

        refunds = [dict(row._mapping) for row in result]

    return refunds  

@app.get("/analytics/total-orders")
def total_orders():

    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT COUNT(*) FROM orders")
        )

        total = result.scalar()

    return {"total_orders": total}


@app.get("/analytics/total-revenue")
def total_revenue():

    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT COALESCE(SUM(amount),0) FROM orders")
        )

        total = float(result.scalar())

    return {"total_revenue": total}


@app.get("/analytics/total-refunds")
def total_refunds():

    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT COUNT(*) FROM refunds")
        )

        total = result.scalar()

    return {"total_refunds": total}


@app.get("/analytics/net-revenue")
def net_revenue():

    with engine.connect() as conn:

        revenue = conn.execute(
            text("SELECT COALESCE(SUM(amount),0) FROM orders")
        ).scalar()

        refunds = conn.execute(
            text("SELECT COALESCE(SUM(refund_amount),0) FROM refunds")
        ).scalar()

    return {
        "net_revenue": float(revenue - refunds)
    }


@app.get("/analytics/average-order-value")
def average_order_value():

    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT AVG(amount) FROM orders")
        )

        avg_value = result.scalar()

    return {
        "average_order_value": float(avg_value)
    }  

@app.get("/analytics/repeat-customer-revenue")
def repeat_customer_revenue():

    with engine.connect() as conn:
        result = conn.execute(
            text("""
                SELECT COALESCE(SUM(amount),0)
                FROM orders
                WHERE customer_id IN (
                    SELECT customer_id
                    FROM orders
                    GROUP BY customer_id
                    HAVING COUNT(*) > 1
                )
            """)
        )

        revenue = result.scalar()

    return {
        "repeat_customer_revenue": float(revenue)
    }

@app.get("/analytics/top-customers")
def top_customers():

    with engine.connect() as conn:
        result = conn.execute(
            text("""
                SELECT
                    customer_id,
                    SUM(amount) AS total_spend
                FROM orders
                GROUP BY customer_id
                ORDER BY total_spend DESC
                LIMIT 10
            """)
        )

        customers = [
            dict(row._mapping)
            for row in result
        ]

    return customers 

@app.get("/analytics/revenue-trends")
def revenue_trends():

    with engine.connect() as conn:
        result = conn.execute(
            text("""
                SELECT
                    TO_CHAR(order_date, 'YYYY-MM') AS month,
                    ROUND(SUM(amount)::numeric, 2) AS revenue
                FROM orders
                GROUP BY month
                ORDER BY month
            """)
        )

        trends = [dict(row._mapping) for row in result]

    return trends