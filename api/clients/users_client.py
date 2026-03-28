class ReqresClient:

    def __init__(self, api_request_context, base_url, headers):
        self.request = api_request_context
        self.base_url = base_url
        self.headers = headers

    def get_users(self, page=1):
        return self.request.get(
            f"{self.base_url}/users",
            params={"page": page},
            headers=self.headers
        )