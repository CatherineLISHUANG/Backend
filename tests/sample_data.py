from backend.models.customer import Customer
from backend.models.city import City
from backend.models.freight import Freight
from backend.models.order import Order
from backend.models.product import Product
import datetime


def get_sample_data():

    EXAMPLE_CUSTOMERS = [
        Customer(id='15', name='John Doe'),
        Customer(id='16', name='Jane Watson'),
        Customer(id='32', name='Michael Steel'),
        Customer(id='34', name='Hanna Hanno'),
        Customer(id='47', name='Bob Truoo'),
    ]

    sample_data = []
    sample_data.extend(EXAMPLE_CUSTOMERS)

    EXAMPLE_CITIES = [
        City(id='15', name='City A'),
        City(id='16', name='City B'),
        City(id='17', name='City C'),
        City(id='23', name='City D'),
        City(id='78', name='City E'),
    ]
    sample_data.extend(EXAMPLE_CITIES)

    EXAMPLE_FREIGHT = [
        Freight(id='15', departure_city_id='15'),
        Freight(id='16', arrival_city_id='16'),
        Freight(id='17', arrival_city_id='16', departure_city_id='15'),
    ]
    sample_data.extend(EXAMPLE_FREIGHT)

    EXAMPLE_PRODUCTS = [
        Product(
            id='576',
            code='54535',
            product_class='equipment',
            price='500',
            sales_unit='foo bar',
            name='my product 1'
        ),
        Product(
            id='5463432',
            code='1000',
            product_class='equipment',
            price='5400',
            sales_unit='foo bar',
            name='my product 2'
        ),
        Product(
            id='78695',
            code='1500',
            product_class='equipment',
            price='54300',
            sales_unit='foo bar',
            name='my product 3'
        ),
    ]
    sample_data.extend(EXAMPLE_PRODUCTS)

    EXAMPLE_ORDERS = [
        Order(
            id='1544',
            date=datetime.datetime(2022, 10, 30),
            product_quantity=3,
            customer_id=15,
            city_id=78,
            product_id=576,
        ),
        Order(
            id='1545',
            date=datetime.datetime(2022, 9, 15),
            product_quantity=3,
            customer_id=15,
            city_id=23,
            product_id=5463432,
        ),
        Order(
            id='1546',
            date=datetime.datetime(2022, 10, 30),
            product_quantity=3,
            customer_id=17,
            city_id=23,
            product_id=5463432,
        ),
        Order(
            id='1547',
            date=datetime.datetime(2022, 10, 30),
            product_quantity=3,
            customer_id=17,
            city_id=23,
            product_id=5463432,
        ),
    ]
    sample_data.extend(EXAMPLE_ORDERS)

    return sample_data
