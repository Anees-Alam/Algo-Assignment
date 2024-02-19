import timeit

class Product:
    def __init__(self, id, name, price, category):
        self.id = id
        self.name = name
        self.price = price
        self.category = category
# creating class named manage
class Manager:
    def __init__(self):
        self.products = []
    # used to read given file
    def load_data(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                id, name, price, category = line.strip().split(',')
                self.products.append(Product(id, name, float(price), category))
    # used to insert the info at the top of list
    def insert_data(self, new_product):
        self.products.insert(0, new_product)
    # used to update any existing data in list
    def update_data(self, product_id, new_details):
        for product in self.products:
            if product.id == product_id:
                product.name = new_details.get('name', product.name)
                product.price = new_details.get('price', product.price)
                product.category = new_details.get('category', product.category)
    # used to delete any existing data
    def delete_data(self, product_id):
        for product in self.products:
            if product.id == product_id:
                self.products.remove(product)
                break
    # used to search any existing data
    def search_id(self, product_id):
        for product in self.products:
            if product.id == product_id:
                return product
        return None
    # used to sort the list by price
    def bubble_sort_price(self):
        n = len(self.products)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.products[j].price > self.products[j+1].price:
                    self.products[j], self.products[j+1] = self.products[j+1], self.products[j]
    #used to show the list sorted using the bubble sort
    def show_all_products(self):
        self.bubble_sort_price()
        for product in self.products:
            print(f"ID: {product.id}, Name: {product.name}, Price: {product.price}, Category: {product.category}")


# functions used to generate sorted and reverse sorted data
def generate_sorted_data(size):
    return [Product(str(i), f"Product {i}", i, "Category") for i in range(1, size + 1)]

def generate_reversesorted_data(size):
    return [Product(str(i), f"Product {i}", i, "Category") for i in range(size, 0, -1)]


# created an instance and loaded file of lists
manager = Manager()
manager.load_data('product_data.txt')

# while function to give options
while True:
    print("\nChoose an action:")
    print("1. add a new product")
    print("2. Update a product")
    print("3. remove a product")
    print("4. look up a product")
    print("5. Show all products")
    print("6. Exit")

    choice = input("Enter the number (1-6): ")
    # for when 1 is pressed to add new data to list
    if choice == '1':
        id = input("Please enter product ID: ")
        name = input("Please enter product name: ")
        price = float(input("Please enter product price: "))
        category = input("Please enter product category: ")
        new_product = Product(id, name, price, category)
        manager.insert_data(new_product)
        print("Added successfully.")
    # for when 2 is pressed to update data in list
    elif choice == '2':
        product_id = input("Please enter the ID to update: ")
        name = input("Please enter the new name (press enter to leave it the same): ")
        price = input("Please enter the new price (press enter to leave it the same): ")
        category = input("Please enter the new category (press enter to keep unchanged): ")
        new_details = {}
        if name:
            new_details['name'] = name
        if price:
            new_details['price'] = float(price)
        if category:
            new_details['category'] = category
        manager.update_data(product_id, new_details)
        print("Updated successfully.")
    # for when 3 is pressed to delete any data from list
    elif choice == '3':
        product_id = input("Please enter ID to delete: ")
        manager.delete_data(product_id)
        print("Deleted successfully.")
    # for when 4 is pressed to search existing data in list
    elif choice == '4':
        product_id = input("Please enter the ID to search: ")
        product = manager.search_id(product_id)
        if product:
            print(product.name, product.price, product.category)
        else:
            print("not found.")
    # for when 5 is pressed to show all data in file
    elif choice == '5':
        manager.show_all_products()
            
    # for when 6 is pressed to exit/kill the program
    elif choice == '6':
        print("Exiting program.")
        break
    # for when an invalid number is pressed (any number other than 1-6)
    else:
        print("Invalid number")

# Time taken to sort data loaded from file
start_time = timeit.default_timer()
manager.bubble_sort_price()
end_time = timeit.default_timer()
print(f"Time taken to sort data from file: {end_time - start_time:.6f} seconds")

# Time taken to reverse sort data loaded from file
start_time = timeit.default_timer()
manager.products.reverse()  # Reverse the order of the products list
end_time = timeit.default_timer()
print(f"Time taken to reverse sort data from file: {end_time - start_time:.6f} seconds")