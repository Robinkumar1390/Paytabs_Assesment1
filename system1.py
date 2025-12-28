from system2 import validate_transaction
from werkzeug.security import generate_password_hash

stored_pin_hash = generate_password_hash("1234")

def process_transaction(data):
    pin = data.get("pin")
    amount = data.get("amount")
    tx_type = data.get("type")

    if not pin or not amount or not tx_type:
        return {"status": "error", "message": "Invalid request"}, 400

    return validate_transaction(pin, amount, tx_type, stored_pin_hash)
