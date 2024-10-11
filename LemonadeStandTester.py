# Author: Ashton Lee
# Github User: ashton01L
# Date: 10/10/2024
# Description: You will be writing code for recording the menu items and daily sales of a lemonade stand.

import unittest
from LemonadeStand import MenuItem, SalesForDay, LemonadeStand, InvalidSalesItemError

class LemonadeStandTest(unittest.TestCase):
    def setUp(self):
        """
        Set up a LemonadeStand object and menu items for testing.
        """
        self.stand = LemonadeStand('Test Stand')
        self.item1 = MenuItem('lemonade', 0.5, 1.5)
        self.item2 = MenuItem('cookie', 0.2, 1.0)
        self.stand.add_menu_item(self.item1)
        self.stand.add_menu_item(self.item2)

    def test_add_menu_item(self):
        """
        Test if a menu items were added correctly. Prints item, cost, selling price.
        """
        self.assertIn('lemonade', self.stand._menu)
        self.assertIn('cookie', self.stand._menu)
        print("Menu items added to the stand:")
        for item_name, menu_item in self.stand._menu.items():
            print(f"Item: {item_name}, Wholesale cost: ${menu_item.get_cost():.2f}, Sell price: ${menu_item.get_price():.2f}")


    def test_enter_sales_for_today(self):
        """
        Test sales entry for multiple valid menu items. Prints results
        """
        day_sales = {'lemonade': 5, 'cookie': 3}
        self.stand.enter_sales_for_today(day_sales)
        self.assertEqual(self.stand.sales_of_menu_item_for_day(0, 'lemonade'), 5)
        self.assertEqual(self.stand.sales_of_menu_item_for_day(0, 'cookie'), 3)
        print("\nSales for today:")
        sales_dict = self.stand._sales_records[0].get_sales_dict()
        for item, quantity in sales_dict.items():
            print(f"Item: {item}, Quantity sold: {quantity}")

    def test_invalid_sales_item(self):
        """
        Test if an InvalidSalesItemError is raised for an invalid item.
        """
        with self.assertRaises(InvalidSalesItemError):
            self.stand.enter_sales_for_today({'invalid_item': 1})

    def test_total_sales_for_menu_item(self):
        """
        Test total sales calculation for multiple menu items. Prints results
        """
        day_sales = {'lemonade': 5, 'cookie': 3}
        self.stand.enter_sales_for_today(day_sales)
        self.assertEqual(self.stand.total_sales_for_menu_item('lemonade'), 5)
        self.assertEqual(self.stand.total_sales_for_menu_item('cookie'), 3)
        print("\nTotal profit per menu item:")
        print(f"Total profit for day on all lemonade sales: ${self.stand.total_profit_for_menu_item('lemonade'):.2f}")
        print(f"Total profit for day on all cookie sales: ${self.stand.total_profit_for_menu_item('cookie'):.2f}")

    def test_total_profit_for_menu_item(self):
        """
        Test total profit calculation for a menu item.
        """
        day_sales = {'lemonade': 5}
        self.stand.enter_sales_for_today(day_sales)
        self.assertAlmostEqual(self.stand.total_profit_for_menu_item('lemonade'), 5)

if __name__ == '__main__':
    unittest.main()