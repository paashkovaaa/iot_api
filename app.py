from aiohttp import web

from routes.device import setup_device_routes
from routes.location import setup_location_routes
from routes.user import setup_user_routes

app = web.Application()

setup_device_routes(app)
setup_user_routes(app)
setup_location_routes(app)


if __name__ == "__main__":
    web.run_app(app)
