import secrets

def generate_api_token():
    return secrets.token_hex(20)  # Generates a 40-character hexadecimal token
