### Build a Shopping Cart
from IPython.display import clear_output
class Cart():
    def __init__(self, cart=[]):
        self.cart=cart
        print('\n--- Shopping Cart: ---\n{}'.format(cart))
    def showCart(self):
        clear_output()
        print('\n--- Shopping Cart: ---')
        for item in self.cart:
            print(item.title())
    def addItem(self):
        self.showCart()
        added = input('What item would you like to add? ')
        self.cart.append(added.lower())
        print('\n{} has been added to your shopping cart'.format(added.title()))
    def removeItem(self):
        self.showCart()
        removed = input('What item would you like to remove? ')
        if removed.lower() in self.cart:
            self.cart.remove(removed)
            print('\n{} has been removed from your shopping cart'.format(removed.title()))
        else:
            print('\nThere is no {} in your shopping cart'.format(removed.title()))
    def quitCart(self):
        print('\nWe are sorry to see you go!')
    def checkQuit(self):
        if self.cart == []:
            print('\nShopping cart is empty...\n')
            keep_shopping = input('Would you like to add an item? (y/n) ')
            if keep_shopping.lower() == 'y':
                return False
            else:
                print('\nWe are sorry to see you go! :\'(')
                return True
        else:
            myCart.showCart()
            leave_items = input('Are you sure you would like to leave this site without the purchasing the items in your cart? (y/n)\n')
            if leave_items.lower() == 'y':
                print('\nWe are sorry to see you go! :\'(')
                return True
            else:
                return False

def letsShop():
    flag=False
    while flag != True:
        ans=input('What would you like to do (e.g. add/remove/show/quit)? ')
        if ans.lower() == 'quit':
            flag = myCart.checkQuit()
        elif ans.lower() == 'add':
            myCart.addItem()
        elif ans.lower() == 'remove':
            myCart.removeItem()
        elif ans.lower() == 'show':
            myCart.showCart()
        else:
            print('{} is not a valid option'.format(ans.title()))

myCart=Cart()
letsShop()
