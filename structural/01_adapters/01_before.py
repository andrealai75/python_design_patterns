class Customer(object):
    def __init__(self, name, address):
        self._name = name
        self._address = address

    @property
    def name(self):
        return self._name
    
    @property
    def address(self):
        return self._address
    
    def __str__(self):
        return f'{self._name} - {self._address}'
    
class Vendor(object):
    def __init__(self, name, number, street):
        self._name = name
        self._number = number
        self._street = street
        
    @property
    def name(self):
        return self._name
    
    @property
    def number(self):
        return self._number
    
    @property
    def street(self):
        return self._street
    
    def __str__(self):
        return f'{self._name} - {self._number} - {self._street}'

MOCKCUSTOMERS = (
    Customer('Pizza Love', '33 Pepperoni Lane'),
    Customer('Happy and Green', '25 kane St.'),
    Customer('Sweet Tooth', '42 Chocolate Ave.')
)

MOCKVENDORS = (
    Vendor('Dough Factory', 1, 'Semolina Court'),
    Vendor('Farm Produce', 14, 'Country Rd.'),
    Vendor('Cocoa World', 53, 'Tropical Blvd.')
)

TYPE = 'vendors'

def main():
    if TYPE == 'customers':
        for customer in MOCKCUSTOMERS:
            print(customer)
    elif TYPE == 'vendors':
        for vendor in MOCKVENDORS:
            print(vendor)
    else:
        raise ValueError('Incorrect type: ' + TYPE)

if __name__ == '__main__':
    main()

