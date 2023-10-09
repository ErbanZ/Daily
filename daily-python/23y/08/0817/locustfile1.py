from locust import HttpUser, task
import requests

class hello(HttpUser):
    host = "https://httpbin.org"

    # @task
    # def hello_get(self):
    #     self.client.get("/get")

    # @task
    # def hello_post(self):
    #     self.client.post("/post")

    @task
    def hello_name(self):
        for i in range(10):
            self.client.get(f"/get?id={i}", name="/get?id=666")

