import products
import store
import promotions

# setup initial stock of inventory
product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250),
                products.NonStockedProduct("Windows License", price=125),
                products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                ]

# Create promotion catalog
second_half_price = promotions.SecondHalfPrice("Second Half price!")
third_one_free = promotions.ThirdOneFree("Third One Free!")
thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

# Add promotions to products
product_list[0].set_promotion(second_half_price)
product_list[1].set_promotion(third_one_free)
product_list[2].set_promotion(thirty_percent)
best_buy = store.Store(product_list)


def menu():
    print("""\nStore Menu 
---------
1). List all products in store
2). Show total amount in store
3). Make an order
4). Quit
    """)


def start(inventory):
    """This function is use while loop and controls the flow of the data based on user input.
    Throw exceptions if user input is not per requirement"""
    while True:
        menu()
        user_input = int(input("Please choose a number: "))
        if user_input == 1:
            for num, names in enumerate(inventory.items):
                print(num + 1, names.show())
        elif user_input == 2:
            print(f"There are {inventory.get_total_quantity()} items in the store")
        elif user_input == 3:
            print("When you want to finish order, enter empty text.")
            try:
                total = 0
                while True:
                    input_product_number = input("Which product # do you want?")
                    input_product_quan = input("What amount do you want? ")
                    if input_product_number == "" and input_product_quan == "":
                        break
                    else:
                        total += inventory.order(
                            [(inventory.items[int(input_product_number) - 1], int(input_product_quan))])
                        print("items added to the your shopping cart")
                print("**********")
                print(f"your total is {total}")
            except IndexError:
                print("Choose from available options only")
            except ValueError:
                print("Enter numbers only")

        elif user_input == 4:
            break
        else:
            if user_input != type(int):
                raise Exception("something wrong with your input")


def main():
    start(best_buy)


if __name__ == "__main__":
    main()
