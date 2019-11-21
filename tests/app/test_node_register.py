import json
import urllib3

from flask_testing import LiveServerTestCase

from app import app


class MyTest(LiveServerTestCase):
    def create_app(self):
        app.config["TESTING"] = True
        return app

    def generate_local_url(self, path):
        return self.get_server_url() + path

    def test_server_is_up_and_running(self):
        data = {"nodes": ["172.17.0.1", "172.17.0.2"]}
        encoded_data = json.dumps(data).encode("utf-8")

        http = urllib3.PoolManager()
        response = http.request(
            "POST",
            self.generate_local_url("/nodes/register"),
            body=encoded_data,
            headers={"Content-Type": "application/json"},
        )

        self.assertEqual(response.status, 201, response.__dict__)

        total_nodes = json.loads(response.data.decode("utf-8"))["total_nodes"]

        self.assertListEqual(["172.17.0.1", "172.17.0.2"], total_nodes)
