from . import customers, payment_info, ratings_reviews, orders, order_details, recipes, resources, sandwiches, promotions, menu_items

from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    recipes.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
    customers.Base.metadata.create_all(engine)
    payment_info.Base.metadata.create_all(engine)
    ratings_reviews.Base.metadata.create_all(engine)
    promotions.Base.metadata.create_all(engine)
    menu_items.Base.metadata.create_all(engine)

