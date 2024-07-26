from aiohttp import web
from models import Location


async def get_locations(request):
    try:
        locations = list(Location.select().dicts())
        return web.json_response(locations)
    except Exception as e:
        return web.json_response({"error": "Error retrieving locations"}, status=500)


async def add_location(request):
    try:
        data = await request.json()
        location = Location.create(**data)
        return web.json_response({"id": location.id})
    except Exception as e:
        return web.json_response({"error": "Error adding location"}, status=500)


async def update_location(request):
    location_id = int(request.match_info["id"])
    try:
        data = await request.json()
        query = Location.update(**data).where(Location.id == location_id)
        query.execute()
        return web.json_response({"status": "updated"})
    except Exception as e:
        return web.json_response({"error": "Error updating location"}, status=500)


async def delete_location(request):
    location_id = int(request.match_info["id"])
    try:
        query = Location.delete().where(Location.id == location_id)
        query.execute()
        return web.json_response({"status": "deleted"})
    except Exception as e:
        return web.json_response({"error": "Error deleting location"}, status=500)


def setup_location_routes(app):
    app.router.add_get("/locations", get_locations)
    app.router.add_post("/locations", add_location)
    app.router.add_put("/locations/{id}", update_location)
    app.router.add_delete("/locations/{id}", delete_location)
