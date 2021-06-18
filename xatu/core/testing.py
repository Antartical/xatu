from __future__ import annotations

from unittest import TestCase
from fastapi.testclient import TestClient
from xatu.asgi import app


class APITestCase(TestCase):
    """TestCase class for API testing."""

    client: TestClient

    def setUp(self):
        super().setUp()
        self.client = TestClient(app)
