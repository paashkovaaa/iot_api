from aiohttp import web
from models import Device


async def get_devices(request):
    try:
        devices = list(Device.select().dicts())
        return web.json_response(devices)
    except Exception as e:
        return web.json_response({"error": "Error retrieving devices"}, status=500)


async def add_device(request):
    try:
        data = await request.json()
        device = Device.create(**data)
        return web.json_response({"id": device.id})
    except Exception as e:
        return web.json_response({"error": "Error adding device"}, status=500)


async def update_device(request):
    device_id = int(request.match_info["id"])
    try:
        data = await request.json()
        query = Device.update(**data).where(Device.id == device_id)
        query.execute()
        return web.json_response({"status": "updated"})
    except Exception as e:
        return web.json_response({"error": "Error updating device"}, status=500)


async def delete_device(request):
    device_id = int(request.match_info["id"])
    try:
        query = Device.delete().where(Device.id == device_id)
        query.execute()
        return web.json_response({"status": "deleted"})
    except Exception as e:
        return web.json_response({"error": "Error deleting device"}, status=500)


def setup_device_routes(app):
    app.router.add_get("/devices", get_devices)
    app.router.add_post("/devices", add_device)
    app.router.add_put("/devices/{id}", update_device)
    app.router.add_delete("/devices/{id}", delete_device)
