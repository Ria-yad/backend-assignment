from locust import HttpUser, task, between

class AnalyticsUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def total_orders(self):
        self.client.get("/analytics/total-orders")

    @task
    def total_revenue(self):
        self.client.get("/analytics/total-revenue")

    @task
    def total_refunds(self):
        self.client.get("/analytics/total-refunds")

    @task
    def net_revenue(self):
        self.client.get("/analytics/net-revenue")

    @task
    def average_order_value(self):
        self.client.get("/analytics/average-order-value")