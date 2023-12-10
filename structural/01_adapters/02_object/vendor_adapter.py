from abs_adapter import AbsAdapter


class VendorAdapter(AbsAdapter):
    @property
    def name(self):
        return self.adaptee.name

    @property
    def address(self):
        return str(self.adaptee.number) + ' ' + self.adaptee.street
