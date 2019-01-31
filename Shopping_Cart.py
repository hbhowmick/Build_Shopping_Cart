### Build a Shopping Cart <br>
<p><b>You can use either lists or dictionaries. The program should have the following capabilities:</b><br><br>
1) Takes in input <br>
2) Stores user input into a dictionary <br>
3) User can add or delete items <br>
4) User can see current shopping list <br>
5) Loops until user 'quits' <br>
6) Upon quiting the program, print out all items in the user's list <br>
</p>

# global list
cart = []

def addItem():
    added = input('What item would you like to add? ')
    cart.append(added.lower())
    print('\n{} has been added to your shopping cart'.format(added.title()))
    shoppingCart()

def removeItem():
    removed = input('What item would you like to remove? ')
    if removed.lower() in cart:
        cart.remove(removed)
        print('\n{} has been removed from your shopping cart'.format(removed.title()))
    else:
        print('\nThere is no {} in your shopping cart'.format(removed.title()))
    shoppingCart()

def showCart():
    print('\n--- Shopping Cart: ---')
    for item in cart:
        print(item.title())
    shoppingCart()


# loop and continue to ask until user quits, have the ability to perform all three functions above
def shoppingCart():
    ans = input('What would you like to do (e.g.add/remove/show/quit)? ')
    if ans.lower()== 'add' or ans.lower()== 'remove' or ans.lower()== 'show' or ans.lower()== 'quit':
        if ans.lower() == 'quit':
            if cart == []:
                print('\nShopping cart is empty...\n')
                keep_shopping = input('Would you like to add an item? (y/n) ')
                if keep_shopping.lower() == 'y':
                    shoppingCart()
                else:
                    print('\nWe are sorry to see you go! :\'(')
            else:
                print('\n--- Shopping Cart: ---')
                for item in cart:
                    print(item.title())
                leave_items = input('Are you sure you would like to leave this site without the purchasing the items in your cart? (y/n)\n')
                if leave_items.lower() == 'y':
                    print('\nWe are sorry to see you go! :\'(')
                else:
                    shoppingCart()
        elif ans.lower() == 'add':
            addItem()
        elif ans.lower() == 'remove':
            removeItem()
        elif ans.lower() == 'show':
            showCart()
    else:
        print('That is not a valid option')
        shoppingCart()

shoppingCart()
