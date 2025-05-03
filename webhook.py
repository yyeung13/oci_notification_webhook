# This is a sample webhook code in Python
from flask import Flask, request, Response
import requests
import ssl

app = Flask(__name__)

@app.route('/oci_webhook', methods=['POST'])
def oci_webhook():
    # Check for confirmation header
    confirmation_url = request.headers.get('X-OCI-NS-ConfirmationURL')
    if confirmation_url:
        print(f"Auto-confirming subscription with header URL: {confirmation_url}")
        try:
            resp = requests.get(confirmation_url)
            print(f"Confirmation response: {resp.status_code}")
        except Exception as e:
            print(f"Error confirming subscription: {e}")
        return Response(status=200)

    # Check for confirmation URL in the JSON body (fallback)
    #data = request.get_json()
    try:
        data = request.get_json()
    except Exception as e:
        print(f"Error parsing JSON: {e}")
        return Response(status=400)

    if data and 'ConfirmationURL' in data:
        confirmation_url = data['ConfirmationURL']
        print(f"Auto-confirming subscription with body URL: {confirmation_url}")
        try:
            resp = requests.get(confirmation_url)
            print(f"Confirmation response: {resp.status_code}")
        except Exception as e:
            print(f"Error confirming subscription: {e}")
        return Response(status=200)

    # Handle regular notification
    print("Received notification:", data)
    return Response(status=200)

if __name__ == "__main__":
    context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    #context.load_cert_chain('certbot_cert.pem', 'certbot_key.pem')
    context.load_cert_chain('fullchain.pem', 'certbot_key.pem')
    app.run(host='0.0.0.0', port=5443, ssl_context=context)
