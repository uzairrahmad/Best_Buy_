
class Store:
    def __init__(self, items):
        """
        Initializer method
        """
        self.items = items
        self.total = 0

    def add_product(self, product):
        """
        This method will add the product passed as argument to this function
        """
        if product in self.items:
            print("Item already exists")
        else:
            self.items.append(product)

    def remove_product(self, product):
        """
        this method will remove the product passed as an argument to this function
        """
        if product not in self.items:
            print("Item doesn't exist")
        else:
            self.items.remove(product)

    def get_total_quantity(self) -> int:
        """
        This function will return integer value of total quantity of the items
        """
        for values in self.items:
            self.total += values.quantity
        return self.total

    def get_all_products(self):
        """This method will iterate through the object instance list and will return a
        new list with the items that are active"""
        active_products = []
        for items in self.items:
            if items.is_active:
                active_products.append(items)
        return active_products

    @staticmethod
    def order(shopping_list) -> float:
        """This is our static method that takes a list of tuple as argument, calculate the order total and
        return order cost
        """
        order_cost = 0
        for names, val in shopping_list:
            order_cost += names.buy(val)
        return order_cost
