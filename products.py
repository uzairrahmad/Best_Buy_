class Product:

    def __init__(self, name, price, quantity):
        """
        instantiate variables and also raise exception if the right values are not passed
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None
        if self.name == "" or self.price <= 0 or type(self.price) != int or self.quantity < 0:
            raise Exception("Either name,price or quantity of the product is wrong")

    def get_promotion(self):
        return self.promotion

    def set_promotion(self, discount):
        self.promotion = discount

    def get_quantity(self):
        return float(self.quantity)

    def set_quantity(self, quantity):
        self.quantity = quantity

    def is_active(self):
        """
        this method activates or deactivates quantity based on quantity values
        """
        if self.quantity > 0:
            return True
        else:
            return False

    def activate(self):
        """
        activator
        """
        self.active = True

    def deactivate(self):
        """
        deactivation
        """
        self.active = False

    def show(self):
        """
        This function simply returns the items if items have discount going on.Otherwise, returns
        the items.
        """
        if self.promotion is not None:
            return f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity} " \
                   f" **Promotion** {self.promotion.name}"

        return f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity} "

    def buy(self, quantity):
        """
        This function takes quantity as an argument and subtract the passed amount from
        quantity instance variable and will return the cost of the quantity
        entered
        """
        if quantity > self.quantity:
            raise Exception(f"Only have {self.quantity} in our inventory")
        if quantity < 0:
            raise Exception("Enter a value greater then 0")
        if self.promotion is not None:
            self.quantity -= quantity
            return self.promotion.apply_promotion(self.price, quantity)
        else:
            self.quantity -= quantity
            return float(quantity * self.price)


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)

    def show(self):
        """
        This function simply returns the items
        """
        return f"Product: {self.name}, Price: {self.price}"


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def show(self):
        """
        This function simply returns the items.
        """
        return f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity} "

    def buy(self, quantity):
        """
        This function takes quantity as an argument and subtract the passed amount from
        quantity instance variable and will return the cost of the quantity
        entered
        """
        if quantity > self.maximum:
            raise Exception("You cant order more then maximum quantity")
        if quantity > self.quantity:
            raise Exception(f"Only have {self.quantity} in our inventory")
        if quantity < 0:
            raise Exception("Enter a value greater then 0")
        else:
            self.quantity -= quantity
            return float(quantity * self.price)
