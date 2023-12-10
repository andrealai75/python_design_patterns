from customer import Customer
from customer_adapter import CustomerAdapter

CUSTOMERSMOCK = (
    CustomerAdapter(Customer('Pizza Love', '33 Pepperoni Lane')),
    CustomerAdapter(Customer('Happy and Green', '25 kane St.')),
    CustomerAdapter(Customer('Sweet Tooth', '42 Chocolate Ave.'))
)