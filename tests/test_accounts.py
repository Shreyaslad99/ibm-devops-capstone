import unittest

from service import create_app
from service.routes import _reset_store


class AccountsApiTestCase(unittest.TestCase):
    def setUp(self):
        _reset_store()
        self.app = create_app({"TESTING": True})
        self.client = self.app.test_client()

    def test_health(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["status"], "ok")

    def test_create_and_read_account(self):
        created = self.client.post(
            "/accounts",
            json={"name": "Ada Lovelace", "email": "ada@example.com"},
        )
        self.assertEqual(created.status_code, 201)
        account_id = created.get_json()["id"]
        read = self.client.get(f"/accounts/{account_id}")
        self.assertEqual(read.status_code, 200)
        self.assertEqual(read.get_json()["name"], "Ada Lovelace")

    def test_list_accounts(self):
        self.client.post(
            "/accounts", json={"name": "Grace", "email": "g@example.com"}
        )
        response = self.client.get("/accounts")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.get_json()), 1)

    def test_update_account(self):
        created = self.client.post(
            "/accounts", json={"name": "Old", "email": "a@b.com"}
        )
        account_id = created.get_json()["id"]
        response = self.client.put(
            f"/accounts/{account_id}", json={"name": "New"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["name"], "New")

    def test_delete_account(self):
        created = self.client.post(
            "/accounts", json={"name": "Delete Me", "email": "d@e.com"}
        )
        account_id = created.get_json()["id"]
        deleted = self.client.delete(f"/accounts/{account_id}")
        self.assertEqual(deleted.status_code, 204)
        missing = self.client.get(f"/accounts/{account_id}")
        self.assertEqual(missing.status_code, 404)

    def test_missing_fields_rejected(self):
        response = self.client.post("/accounts", json={"name": "Missing email"})
        self.assertEqual(response.status_code, 400)

    def test_cors_allows_request_origin(self):
        origin = "https://client.example"
        response = self.client.get("/accounts", headers={"Origin": origin})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers.get("Access-Control-Allow-Origin"), origin)

    def test_security_headers_present(self):
        response = self.client.get("/health")
        self.assertEqual(response.headers.get("X-Content-Type-Options"), "nosniff")
        self.assertEqual(response.headers.get("X-Frame-Options"), "DENY")
        self.assertIn("object-src 'none'", response.headers.get("Content-Security-Policy", ""))


if __name__ == "__main__":
    unittest.main()
