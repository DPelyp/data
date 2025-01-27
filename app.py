import pytest
from flask import Flask, request, jsonify, render_template
from cve_id import ApiRequest
from cpe import ApiRequest

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_request', methods=['POST'])
def send_request():
    cve_id = request.json.get('cve_id')
    if not cve_id:
        return jsonify({"error": "No CVE ID provided"}), 400
    api_request = ApiRequest(cve_id)
    result = api_request.sendReq()
    return jsonify(result)

@app.route('/send_request_cpe', methods=['POST'])
def send_request_cpe():
    cpe_id = request.json.get('cpe_id')
    if not cpe_id:
        return jsonify({"error": "No cpe provided"}), 400
    api_request = ApiRequest(cpe_id)
    result = api_request.sendReq()
    return jsonify(result)

@app.route('/tests', methods=['GET'])
def run_tests():
    try:
        result = pytest.main(["--tb=short", "-q", "cve_id.py"])
        return jsonify({"test_result": result}), 200
    except Exception as e:
        return jsonify({'Error' : {e}}), 500

if __name__ == '__main__':
    app.run(debug=True)