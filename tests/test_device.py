import importlib

import pytest
from aiohttp import web
from aiohttp.test_utils import AioHTTPTestCase
from unittest.mock import patch

import app
from models import Device

sample_device = {
    "name": "Device1",
    "type": "Sensor",
    "login": "device1_login",
    "password": "device1_password",
    "location_id": 1,
    "api_user_id": 1,
}


class DeviceTestCase(AioHTTPTestCase):
    async def get_application(self):
        importlib.reload(app)
        return app.app

    async def test_get_devices(self):
        with patch("models.Device.select") as mock_select:
            mock_select.return_value.dicts.return_value = [sample_device]
            resp = await self.client.request("GET", "/devices")
            assert resp.status == 200
            json_resp = await resp.json()
            assert json_resp == [sample_device]

    async def test_add_device(self):
        with patch("models.Device.create") as mock_create:
            mock_create.return_value = Device(id=1, **sample_device)
            resp = await self.client.request("POST", "/devices", json=sample_device)
            assert resp.status == 200
            json_resp = await resp.json()
            assert json_resp["id"] == 1

    async def test_update_device(self):
        with patch("models.Device.update") as mock_update:
            mock_update.return_value.execute.return_value = 1
            resp = await self.client.request(
                "PUT", "/devices/1", json={"name": "UpdatedDevice"}
            )
            assert resp.status == 200
            json_resp = await resp.json()
            assert json_resp["status"] == "updated"

    async def test_delete_device(self):
        with patch("models.Device.delete") as mock_delete:
            mock_delete.return_value.execute.return_value = 1
            resp = await self.client.request("DELETE", "/devices/1")
            assert resp.status == 200
            json_resp = await resp.json()
            assert json_resp["status"] == "deleted"
