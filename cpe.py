import requests

class ApiRequest:
    def __init__(self, cpe_id):
        self.cpe_id = cpe_id
        self.base_url = "https://services.nvd.nist.gov/rest/json/cves/2.0?"

    def sendReq(self):
        try:
            url = f"{self.base_url}cpeName={self.cpe_id}"
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return f"Error: Request failed {e}"