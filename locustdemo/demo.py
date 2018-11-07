from locust import HttpLocust, TaskSet, task


class Ggdemo(TaskSet):
    @task(1)
    def open_gg(self):
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
        r = self.client.get("/index", headers=header, verify=False)
        print(r.status_code)
        assert r.status_code == 200


class WebsiteUser(HttpLocust):
    task_set = Ggdemo
    min_wait = 3000
    max_wait = 6000


if __name__ == "__main__":
    import os
    os.system("locust -f demo.py --host=http://gg.test.hrhbbx.com")
