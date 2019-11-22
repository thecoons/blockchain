# import json
# import urllib3

# from flask_testing import LiveServerTestCase

# from app import app


# class MyTest(LiveServerTestCase):
#     def create_app(self):
#         app.config["TESTING"] = True
#         app.config["LIVESERVER_PORT"] = 5000
#         return app

#     def generate_local_url(self, path):
#         return self.get_server_url() + path

#     def test_node_can_register_valid_address(self):
#         data = {"nodes": ["http://192.168.0.1:5000"]}
#         encoded_data = json.dumps(data).encode("utf-8")

#         http = urllib3.PoolManager()
#         response = http.request(
#             "POST",
#             self.generate_local_url("/nodes/register"),
#             body=encoded_data,
#             headers={"Content-Type": "application/json"},
#         )

#         self.assertEqual(response.status, 201, response.__dict__)

#         total_nodes = json.loads(response.data.decode("utf-8"))["total_nodes"]

#         self.assertEqual(["192.168.0.1:5000"], total_nodes)

#     def test_node_can_filter_invalid_address_registered(self):
#         data = {"nodes": ["http//192.168.0.2:5000"]}
#         encoded_data = json.dumps(data).encode("utf-8")

#         http = urllib3.PoolManager()
#         response = http.request(
#             "POST",
#             self.generate_local_url("/nodes/register"),
#             body=encoded_data,
#             headers={"Content-Type": "application/json"},
#         )

#         self.assertEqual(response.status, 400, response.__dict__)
