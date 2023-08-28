import requests

# Replace 'YOUR_TOKEN' with the actual token value
token= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk1Nzc3NTE1LCJpYXQiOjE2OTMxODU1MTUsImp0aSI6ImRkNzA4ZTRjYWUyMTQ2MTRhNGNhZGRkZGMwOTE0Zjg3IiwidXNlcl9pZCI6MX0.mqfYx4ysirlkJYWxr9ilfPIL062Hj8lnfVU785JDMI8"

headers = {'Authorization': f'Token {token}'}

# Replace 'YOUR_API_ENDPOINT' with the actual URL of your API endpoint
api_url = 'http://127.0.0.1:8006/api/search-by-color/'

# Replace 'HEX_COLOR' with the hex color you want to search for
hex_color = '#336699'  # Example hex color

data = {'hex_color': hex_color}

response = requests.post(api_url, headers=headers, json=data)

print(response.status_code)
print(response.json())