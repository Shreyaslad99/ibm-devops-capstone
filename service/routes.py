from flask import Blueprint, jsonify, request

accounts_blueprint = Blueprint("accounts", __name__)
_accounts = {}
_next_id = 1


def _reset_store():
    global _accounts, _next_id
    _accounts = {}
    _next_id = 1


@accounts_blueprint.get("/health")
def health():
    return jsonify({"status": "ok"}), 200


@accounts_blueprint.post("/accounts")
def create_account():
    global _next_id
    payload = request.get_json(silent=True) or {}
    name = payload.get("name")
    email = payload.get("email")
    if not name or not email:
        return jsonify({"error": "name and email are required"}), 400

    account = {"id": _next_id, "name": name, "email": email}
    _accounts[_next_id] = account
    _next_id += 1
    return jsonify(account), 201


@accounts_blueprint.get("/accounts")
def list_accounts():
    return jsonify([_accounts[key] for key in sorted(_accounts)]), 200


@accounts_blueprint.get("/accounts/<int:account_id>")
def read_account(account_id):
    account = _accounts.get(account_id)
    if account is None:
        return jsonify({"error": "account not found"}), 404
    return jsonify(account), 200


@accounts_blueprint.put("/accounts/<int:account_id>")
def update_account(account_id):
    account = _accounts.get(account_id)
    if account is None:
        return jsonify({"error": "account not found"}), 404

    payload = request.get_json(silent=True) or {}
    if "name" in payload:
        account["name"] = payload["name"]
    if "email" in payload:
        account["email"] = payload["email"]
    return jsonify(account), 200


@accounts_blueprint.delete("/accounts/<int:account_id>")
def delete_account(account_id):
    account = _accounts.pop(account_id, None)
    if account is None:
        return jsonify({"error": "account not found"}), 404
    return "", 204
