from fastapi import APIRouter
from . import orders, order_details

def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)

    @app.get("/")
    def root():
        return {"message": "Welcome to the API"}