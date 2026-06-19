# Backend Assignment

## Tech Stack
- Python
- FastAPI
- PostgreSQL
- Locust

## Dataset
- Customers: 100,000
- Orders: 1,000,000
- Refunds: 200,000

## Mock APIs
- GET /customers
- GET /orders
- GET /refunds

## Analytics APIs
- GET /analytics/total-orders
- GET /analytics/total-revenue
- GET /analytics/total-refunds
- GET /analytics/net-revenue
- GET /analytics/average-order-value
- GET /analytics/repeat-customer-revenue
- GET /analytics/revenue-trends
- GET /analytics/top-customers

## Ingestion
Data is fetched from paginated APIs and stored in PostgreSQL.

## Performance Optimization
Created indexes:
- idx_orders_customer_id
- idx_orders_order_date
- idx_refunds_order_id

## Load Testing
Performed load testing using Locust with 50 concurrent users.