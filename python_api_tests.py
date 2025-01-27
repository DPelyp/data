import requests
import pytest

class ApiTests:
    def __init__ (self, base_url):
        self.base_url = base_url

    def sendRequestGet(self):
        try:
            url = self.base_url
            response = requests.get(url)
            return response
        except requests.RequestException as e:
            return {"Error" : str(e)}
    
    def sendRequestPost(self, payload):
        try:
            url = self.base_url
            response = requests.post(url, json=payload)
            return response.json()
        except requests.RequestException as e:
            return {"Error" : str(e)}

get_api = ApiTests('https://jsonplaceholder.typicode.com/posts/1')
post_api = ApiTests('https://jsonplaceholder.typicode.com/posts')

def test_get_status_code():
    response = get_api.sendRequestGet()
    assert response.status_code == 200, "Error, response code != 200"

def test_post_body():
    response = post_api.sendRequestPost({ "title": "foo", "body": "bar", "userId": 1})
    assert 'title' in response, 'Field "title" is absent'