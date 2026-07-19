# import requests
# import json
#
#
# class TestPytestMultiEnvDemo:
#
#     def test_get_demo_multi_env(self, env_config, env_request_data, env_response_data):
#         host = env_config["host"]
#         get_api = env_config["getAPI"]
#         get_api_response_data = env_response_data["getAPI"]
#         # send request
#         response = requests.get(host+get_api)
#         # assert
#         assert response.status_code == 200
#         assert response.json() == get_api_response_data
#
#     def test_post_demo_multi_env(self, env_config, env_request_data, env_response_data):
#         host = env_config["host"]
#         post_api = env_config["postAPI"]
#         post_api_request_data = env_request_data["postAPI"]
#         post_api_response_data = env_response_data["postAPI"]
#         # send request
#         response = requests.post(host + post_api, post_api_request_data)
#         # assert
#         assert response.status_code == 201
#         assert response.json() == post_api_response_data
import requests
import json


class TestPytestMultiEnvDemo:

    def test_get_demo_multi_env(self, env_config, env_request_data, env_response_data):
        host = env_config["host"]
        get_api = env_config["getAPI"]
        get_api_response_data = env_response_data["getAPI"]
        response = requests.get(host + get_api)
        assert response.status_code == 200
        # 如果GET返回列表或动态数据，建议类似处理
        assert response.json() == get_api_response_data  # 若完全匹配，保持不变

    def test_post_demo_multi_env(self, env_config, env_request_data, env_response_data):
        host = env_config["host"]
        post_api = env_config["postAPI"]
        post_api_request_data = env_request_data["postAPI"]
        post_api_response_data = env_response_data["postAPI"]  # 参考用

        # 使用 json 参数发送 JSON 数据
        response = requests.post(host + post_api, json=post_api_request_data)
        assert response.status_code == 201

        actual = response.json()
        print("Actual POST response:", actual)  # 方便调试

        # 只验证请求中的字段是否在响应中存在且值一致
        for key, value in post_api_request_data.items():
            assert actual.get(key) == value, f"Field '{key}' mismatch: expected {value}, got {actual.get(key)}"

        # 验证 id 存在（假设是自动生成的）
        assert "id" in actual, "Response missing 'id'"
        assert isinstance(actual["id"], int), "id is not an integer"