from backend.models.customer import Customer


def get_sample_data():

    EXAMPLE_CUSTOMERS = [
        Customer(id='15', first_name='John', last_name='Doe'),
        Customer(id='16', first_name='Jane', last_name='Watson'),
        Customer(id='32', first_name='Michael', last_name='Steel'),
        Customer(id='34', first_name='Hanna', last_name='Hanno'),
        Customer(id='47', first_name='Bob', last_name='Truoo'),
    ]

    sample_data = []
    sample_data.extend(EXAMPLE_CUSTOMERS)
    return sample_data
