from aiohttp import web

from models import ApiUser


async def get_users(request):
    try:
        users = list(ApiUser.select().dicts())
        return web.json_response(users)
    except Exception as e:
        return web.json_response({"error": "Error retrieving users"}, status=500)


async def add_user(request):
    try:
        data = await request.json()
        user = ApiUser.create(**data)
        return web.json_response({"id": user.id})
    except Exception as e:
        return web.json_response({"error": "Error adding user"}, status=500)


async def update_user(request):
    user_id = int(request.match_info["id"])
    try:
        data = await request.json()
        query = ApiUser.update(**data).where(ApiUser.id == user_id)
        query.execute()
        return web.json_response({"status": "updated"})
    except Exception as e:
        return web.json_response({"error": "Error updating user"}, status=500)


async def delete_user(request):
    user_id = int(request.match_info["id"])
    try:
        query = ApiUser.delete().where(ApiUser.id == user_id)
        query.execute()
        return web.json_response({"status": "deleted"})
    except Exception as e:
        return web.json_response({"error": "Error deleting user"}, status=500)


def setup_user_routes(app):
    app.router.add_get("/users", get_users)
    app.router.add_post("/users", add_user)
    app.router.add_put("/users/{id}", update_user)
    app.router.add_delete("/users/{id}", delete_user)
