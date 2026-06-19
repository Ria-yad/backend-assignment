from faker import Faker
import pandas as pd
import random

fake = Faker()

random.seed(42)

# Customers
customers = []

for i in range(1, 100001):
    customers.append({
        "id": i,
        "name": fake.name(),
        "email": fake.email()
    })

pd.DataFrame(customers).to_csv(
    "data/customers.csv",
    index=False
)

print("Customers generated")

# Orders
orders = []

for i in range(1, 1000001):
    orders.append({
        "id": i,
        "customer_id": random.randint(1, 100000),
        "amount": round(random.uniform(10, 1000), 2)
    })

pd.DataFrame(orders).to_csv(
    "data/orders.csv",
    index=False
)

print("Orders generated") 

# Refunds
refunds = []

for i in range(1, 200001):
    refunds.append({
        "id": i,
        "order_id": random.randint(1, 1000000),
        "refund_amount": round(random.uniform(5, 500), 2)
    })

pd.DataFrame(refunds).to_csv(
    "data/refunds.csv",
    index=False
)

print("Refunds generated")