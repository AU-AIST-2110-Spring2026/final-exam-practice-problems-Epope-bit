# List of grocery item prices
prices = [1.25, 2.50, 3.99, 4.00, 5.75, 6.20, 7.50, 8.00, 9.99, 10.00,
          12.50, 14.00, 15.75, 16.00, 18.25, 20.00, 22.50, 24.00, 25.99,
          30.00, 32.50, 35.00, 40.00, 45.50, 50.00, 55.00, 60.00]


def filter_prices(prices: list[float]) -> list[float]:
    '''Function to filter and sort grocery prices'''

    # List where you should store the filtered prices
    filtered_prices = []

    # Step 1: Filter prices
    # Prices should be greater than or equal to 5.00
    # Prices should be less than or equal to 25.00
    # Prices should be whole-dollar amounts, such as 8.00 or 10.00

    # Step 2: Sort prices from lowest to highest
    # Use the sort function

    # Step 3: Return the filtered and sorted list
    # return filtered_prices

def main():
    '''DO NOT MODIFY THIS FUNCTION'''
    print(filter_prices(prices))


if __name__ == "__main__":
    main()