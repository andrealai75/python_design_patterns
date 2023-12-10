from customers_mock import CUSTOMERSMOCK
from vendors_mocks import VENDORSMOCK

ALLMOCKS = CUSTOMERSMOCK + VENDORSMOCK

def main():
    for customer in ALLMOCKS:
        print(f'{customer.name} - {customer.address}')

if __name__ == '__main__':
    main()
