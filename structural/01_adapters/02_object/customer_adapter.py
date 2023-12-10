from abs_adapter import AbsAdapter


class CustomerAdapter(AbsAdapter):
    @property
    def name(self):
        return self.adaptee.name

    @property
    def address(self):
        return self.adaptee.address
