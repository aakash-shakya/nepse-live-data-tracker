import requests as req
from constants import REQUEST_HEADERS


class HandleRequests:

    

    def __init__(self, url, body):
        self.url = url
        self.body = body
        self.headers = REQUEST_HEADERS

    def get_request(self):
        response = req.get(self.url, headers=self.headers)
        return response

    def post_request(self):
        response = req.post(self.url, data=self.body, headers=self.headers)
        return response

    def get_response_text(self):
        response = self.get_request()
        return response.text

    