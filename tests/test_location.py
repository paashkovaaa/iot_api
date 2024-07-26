import importlib
import pytest
from aiohttp import web
from aiohttp.test_utils import AioHTTPTestCase
from unittest.mock import patch

import app
from models import Location

sample_location = {
    "name": "Location1",
}


class LocationTestCase(AioHTTPTestCase):
    async def get_application(self):
        importlib.reload(app)
        return app.app

    async def test_get_locations(self):
        with patch("models.Location.select") as mock_select:
            mock_select.return_value.dicts.return_value = [sample_location]
            resp = await self.client.request("GET", "/locations")
            assert resp.status == 200
            json_resp = await resp.json()
            assert json_resp == [sample_location]

    async def test_add_location(self):
        with patch("models.Location.create") as mock_create:
            mock_create.return_value = Location(id=1, **sample_location)
            resp = await self.client.request("POST", "/locations", json=sample_location)
            assert resp.status == 200
            json_resp = await resp.json()
            assert json_resp["id"] == 1

    async def test_update_location(self):
        with patch("models.Location.update") as mock_update:
            mock_update.return_value.execute.return_value = 1
            resp = await self.client.request(
                "PUT", "/locations/1", json={"name": "UpdatedLocation"}
            )
            assert resp.status == 200
            json_resp = await resp.json()
            assert json_resp["status"] == "updated"

    async def test_delete_location(self):
        with patch("models.Location.delete") as mock_delete:
            mock_delete.return_value.execute.return_value = 1
            resp = await self.client.request("DELETE", "/locations/1")
            assert resp.status == 200
            json_resp = await resp.json()
            assert json_resp["status"] == "deleted"
