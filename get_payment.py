import requests
##
url = "https://shopee.co.id/api/v4/mpp/get_payment_redirection"  # Replace with the actual URL

payload = {
    "checkout_id": 142762181271535,
    "flow_source": 1,
    "device_info": {
        "sz_device_fingerprint": "yahQ1IcmKVqCNLunfjyMCg==|I18zd7gA2oFDaiTlaYVEToGEGGAjwe0jTgWt5IaAQklKbvIMxqRkbAqy0ULrZa66mC+rlfAHBhWaMW35FhUDcXQ6xAGNJQ17BftO|IklL5776NWaPlkau|06|3"
    }
}
response = requests.post(url, json=payload)
print(response.status_code)
print(response.json())
if response.json()['error'] == 0:
    print("Get payment redirection success")
else:
    print(response.json()['error_msg'])
