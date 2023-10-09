from locust import HttpUser, task, between, SequentialTaskSet, tag
import random

class TaskCase(SequentialTaskSet):

    # 初始化方法，也就是 setup
    def on_start(self):
        print("***********************setup")
        self.username = "user_" + str(random.randint(1000,10000000))
        self.pwd = "password"
        return super().on_start()

    @task
    @tag('P1')
    def regist(self):
        url = '/anything/regist'
        self.headers = {"Content-Type": "application/json"}
        body = {"username": self.username, "pwd": self.pwd}
        # catch_response为True，允许失败
        # name为标签名称
        with self.client.post(url, json=body, headers=self.headers, catch_response=True) as response:
            if response.status_code >= 400:
                print(url + '\n' + response.text)
                response.failure("/login failure!!!" + str(response.status_code))
            elif response.status_code == 200:
                print(url + '\n' + response.text)
                self.data = response.json()['data']
                # response.success(str(response.status_code))
                response.success()

    @task
    def login(self):
        url = '/anything/login'
        body = {"username": self.username, "pwd": self.pwd}
        with self.client.post(url, json=body, headers=self.headers, catch_response=True) as response:
            if response.status_code >= 400:
                print(url + '\n' + response.text)
                response.failure("/login failure!!!" + str(response.status_code))
            elif response.status_code == 200:
                print(url + '\n' + response.text)
                self.data = response.json()['data']
                # response.success(str(response.status_code))
                response.success()

    @task
    def getinfo(self):
        url = '/anything/getinfo'
        body = {"data": self.data}
        with self.client.post(url, json=body, headers=self.headers, catch_response=True) as response:
            if response.status_code >= 400:
                print(url + '\n' + response.text)
                response.failure("/getinfo failure!!!" + str(response.status_code))
            elif response.status_code == 200:
                print(url + '\n' + response.text)
                response.success()

    # 结束方法，也就是 teardown
    def on_stop(self):
        print("***********************teardown")
        return super().on_stop()

class userRun(HttpUser):
    host = "https://httpbin.org"
    tasks = [TaskCase]
    wait_time = between(0.1, 1)

