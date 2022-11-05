from backend.models.customer import Customer
from backend.models.city import City
from backend.models.freight import Freight

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


    return sample_data
