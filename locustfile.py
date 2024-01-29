from locust import HttpUser, task, between
from random import randint

class LoadTestUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def load_writers(self):
        self.client.get("/writers")

    @task
    def load_default_mode(self):
        self.client.get(f'/')

    @task
    def load_articles(self):
        self.client.get("/loadArticles?id=22")
