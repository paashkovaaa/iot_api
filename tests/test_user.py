import importlib
import pytest
from aiohttp import web
from aiohttp.test_utils import AioHTTPTestCase
from unittest.mock import patch

import app
from models import ApiUser

sample_user = {
    "username": "user1",
    "email": "user1@example.com",
    "password": "password123",
}


class UserTestCase(AioHTTPTestCase):
    async def get_application(self):
        importlib.reload(app)
        return app.app

    async def test_get_users(self):
        with patch("models.ApiUser.select") as mock_select:
            mock_select.return_value.dicts.return_value = [sample_user]
            resp = await self.client.request("GET", "/users")
            assert resp.status == 200
            json_resp = await resp.json()
            assert json_resp == [sample_user]

    async def test_add_user(self):
        with patch("models.ApiUser.create") as mock_create:
            mock_create.return_value = ApiUser(id=1, **sample_user)
            resp = await self.client.request("POST", "/users", json=sample_user)
            assert resp.status == 200
            json_resp = await resp.json()
            assert json_resp["id"] == 1

    async def test_update_user(self):
        with patch("models.ApiUser.update") as mock_update:
            mock_update.return_value.execute.return_value = 1
            resp = await self.client.request(
                "PUT", "/users/1", json={"username": "UpdatedUser"}
            )
            assert resp.status == 200
            json_resp = await resp.json()
            assert json_resp["status"] == "updated"

    async def test_delete_user(self):
        with patch("models.ApiUser.delete") as mock_delete:
            mock_delete.return_value.execute.return_value = 1
            resp = await self.client.request("DELETE", "/users/1")
            assert resp.status == 200
            json_resp = await resp.json()
            assert json_resp["status"] == "deleted"
