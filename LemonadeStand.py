# Author: Ashton Lee
# Github User: ashton01L
# Date: 10/10/2024
# Description: You will be writing code for recording the menu items and daily sales of a lemonade stand.

class MenuItem:
    """
    A class to represent the object item on the lemonade stand menu.

    Attributes:
        _name (str): Name of the item on the menu
        _cost (float): Wholesale cost of specified item on the menu
        _price (float): Selling price of item on the menu
    """

    def __init__(self, name, cost, price):
        """
        Initializes MenuItem object with the provided item name, wholesale cost, and selling price

        :param:
             name (str): Item name
             cost (float): Item wholesale cost
             price (float): Item selling price
        """
        self._name = name
        self._cost = cost
        self._price = price

    def get_name(self):
        """
        Gets the name of the menu item

        :return:
            str: The name of the menu item
        """
        return self._name

    def get_cost(self):
        """
        Gets the wholesale cost of the menu item

        :return:
            float: The wholesale cost of the menu item
        """
        return self._cost

    def get_price(self):
        """
        Gets the selling price of the menu item

        :return:
            float: The selling price of the menu item
        """
        return self._price

class SalesForDay:
    """
    A class to represent the object for sales in a particular day

    Attributes:
        _days_open (int): Number of days the stand has been open so far
        _sales_dict (dict): a dictionary where the keys are the item names and the values are the number of specified
                            items sold on this day
    """

    def __init__(self, days_open, sales_dict):
        """
        Initializes he SalesForDay object with provided number of days the stand has been open for so far and the sales
            dictionary

        :param:
            days_open (int): Number of days open to date
            sales_dict (dict): dictionary with item names (keys) and number of those items sold (values) on this day
        """
        self._days_open = days_open
        self._sales_dict = sales_dict

    def get_days_open(self):
        """
        Gets the number of days open to date

        :return:
            int: The day number
        """
        return self._days_open

    def get_sales_dict(self):
        """
        Gets the dictionary of sale for that day

        :return:
            dict: A dictionary of items sold on this particular day
        """
        return self._sales_dict

class LemonadeStand:
    """
        A class to represent a lemonade stand object.

        Attributes:
            _name (str): The name of the lemonade stand.
            _current_day (int): The current day number.
            _menu (dict): A dictionary where keys are item names and values are MenuItem objects.
            _sales_records (list): A list of SalesForDay objects.
        """
    def __init__(self, name):
        """
        Initializes the LemonadeStand object with the given name.

        :param:
            name (str): The name of the stand.
        """
        self._name = name
        self._current_day = 0
        self._menu = {}
        self._sales_records = []

    def get_name(self):
        """
        Gets the name of the lemonade stand.

        :return:
            str: The name of the lemonade stand.
        """
        return self._name

    def add_menu_item(self, menu_item):
        """
        Add a MenuItem object to the lemonade stand menu.

        :param:
            menu_item (MenuItem): The MenuItem object to add to the menu.
        """
        self._menu[menu_item.get_name()] = menu_item

    def enter_sales_for_today(self, sales_dict):
        """
        Records the sales for the current day.

        :param:
            sales_dict (dict): A dictionary where the keys are item names and the values are the
                               number of those items sold.

        Raises:
            InvalidSalesItemError: If an item in the sales dictionary is not on the menu.
        """
        for item_name in sales_dict:
            if item_name not in self._menu:
                raise InvalidSalesItemError(f"{item_name}")

        sales_for_day = SalesForDay(self._current_day, sales_dict)
        self._sales_records.append(sales_for_day)
        self._current_day += 1

    def sales_of_menu_item_for_day(self, days_open, item_name):
        """
        Gets the number of a specified menu item sold on a specific day.

        :param:
            days_open (int): The day number.
            item_name (str): The name of the menu item.

        :return:
            int: The number of the item sold on that day. Returns 0 if no sales or the day does not exist.
        """
        sales_for_day = self._sales_records[days_open]
        sales_dict = sales_for_day.get_sales_dict()
        return sales_dict.get(item_name, 0)

    def total_sales_for_menu_item(self, item_name):
        """
        Gets the total number of a specific menu items sold over the history of the stand.

        :param:
            item_name (str): The name of the menu item.

        :return:
            int: The total number of the specific item sold.
        """
        total_sales = 0
        for sales_for_day in self._sales_records:
            sales_dict = sales_for_day.get_sales_dict()
            total_sales += sales_dict.get(item_name, 0)
        return total_sales

    def total_profit_for_menu_item(self, item_name):
        """
        Calculates the total historical profit for a specific menu item.

        :param:
            item_name (str): The name of the menu item.

        :return:
            float: The total profit for that specific item.
        """
        total_sales = self.total_sales_for_menu_item(item_name)
        menu_item = self._menu.get(item_name)
        profit_per_item = menu_item.get_price() - menu_item.get_cost()
        return total_sales * profit_per_item


    def total_profit_for_stand(self):
        """
        Returns the total profit for all items sold at the stand.

        :return:
            float: The total profit from all sales
        """
        total_profit = 0
        for item_name in self._menu:
            total_profit += self.total_profit_for_menu_item(item_name)
        return total_profit

class InvalidSalesItemError(Exception):
    """Custom exception for invalid menu items sold."""
    pass

def main():
    """Main function to run the LemonadeStand application."""
    stand = LemonadeStand('Lemons R Us')

    # Create and add menu items
    item1 = MenuItem('lemonade', 0.5, 1.5)
    stand.add_menu_item(item1)
    item2 = MenuItem('nori', 0.6, 0.8)
    stand.add_menu_item(item2)
    item3 = MenuItem('cookie', 0.2, 1.0)
    stand.add_menu_item(item3)

    # Example sales dictionary for day 0
    day_0_sales = {
        'lemonade': 5,
        'cookie': 2,
        'corndog': 1  # This should raise an InvalidSalesItemError
    }

    try:
        stand.enter_sales_for_today(day_0_sales)
    except InvalidSalesItemError as e:
        print(f"Error:  This item is not on the menu: {e}.")

    # Print total profit for lemonade
    print(f"Total profit for lemonade: ${stand.total_profit_for_menu_item('lemonade'):.2f}")


if __name__ == "__main__":
    main()