from aiohttp import web

from models import initialize_db
from routes.device import setup_device_routes
from routes.location import setup_location_routes
from routes.user import setup_user_routes

app = web.Application()

initialize_db()

setup_device_routes(app)
setup_user_routes(app)
setup_location_routes(app)


if __name__ == "__main__":
    web.run_app(app)
