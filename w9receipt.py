import csv

def main():
    #key index for products is O because it has the product number
    key_index = 0
    products = read_products("products.csv", key_index)
    #print(products)
    print()
    print("Requested Items")
    request = process_request("request.csv", products)

def read_products(filename, key_column_index):
    #create the products dictionary to store the data
    products = {}
    # Open a CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open (filename, "rt") as csv_file:
        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)
        # The first line of the CSV file contains column
        # headings and not information, so this statement
        # skips the first line of the CSV file
        next(reader)
        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row in reader:
            # From the current row, retrieve
            # the column that contains the key.
            key = row[key_column_index]
            # Store the data from the current row
            # into the dictionary.
            products[key] = row
            print(products)
     # Return the dictionary.       
    return products

def process_request(filename, products):
    with open (filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        #write a loop that will read and process each row from the request.csv file.
        for row in reader:
            #read each line and put into a variable to use for products.csv
            requested_product_number = row[0]
            requested_quantity = row[1]
            #Use the requested product number to find the corresponding item in products dictionary.
            corresponding_item_products = products[requested_product_number]
            #get the corresponding name from the list that was gotten from corresponding item products
            name_product = corresponding_item_products[1]
            #get the corresponding price from the list that was gotten from corresponding item products
            product_price = corresponding_item_products[2]
            #print required data
            print(f"{name_product}: {requested_quantity} @ {product_price}")



if __name__ == "__main__":
    main()

