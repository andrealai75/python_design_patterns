from vendor import Vendor


class VendorAdapter(Vendor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    @property
    def address(self):
        return str(self.number) + ' ' + self.street
