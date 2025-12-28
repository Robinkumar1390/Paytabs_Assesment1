from werkzeug.security import check_password_hash

def validate_transaction(pin, amount, tx_type, stored_hash):
    if not check_password_hash(stored_hash, pin):
        return {"status": "error", "message": "Authentication failed"}, 401

    if amount <= 0:
        return {"status": "error", "message": "Invalid amount"}, 400

    return {
        "status": "success",
        "message": f"{tx_type} transaction of {amount} completed"
    }, 200
