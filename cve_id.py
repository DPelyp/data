import requests
import pytest

class ApiRequest:
    def __init__(self, cve_id):
        self.cve_id = cve_id
        self.base_url = "https://services.nvd.nist.gov/rest/json/cves/2.0"

    def sendReq(self):
        try:
            url = f"{self.base_url}?cveId={self.cve_id}"
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return f"Error: Request failed {e}"

def test_send_request_success():
    """Простий тест для перевірки формування запиту (без реального виклику мережі)"""
    api_request = ApiRequest("CVE-2022-4304")
    assert isinstance(api_request.base_url, str), f"Помилка: URL має бути рядком, але отримано {type(api_request.base_url).__name__}"