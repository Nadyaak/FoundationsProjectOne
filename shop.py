####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "NadyaCake"
signature_flavors = ["honey","lemon","tiramisu","orange","red velvet"]
order_list = []


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    # your code goes here!
    print ("Our menu :")
    for it in menu:
        print ("_ \" %s \" (KD %s)" %(it,menu[it]))


def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    # your code goes here!
    for orig in original_flavors :
        print("- \" %s \" " %(orig))


def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    # your code goes here!
    for sign in signature_flavors :
        print("- \" %s \" " %(sign))



def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    # your code goes here!
    if order in menu :
        return True
    elif order in original_flavors :
        return True
    elif order in signature_flavors :
        return True
    else :
        return False    


def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    # your code goes here!
    print ("What's your order? (Enter the exact spelling of the itemyou want. Type 'Exit' to end your order.) ")
    order = input()
    while order.lower()!="exit":
        if is_valid_order(order.lower()):
            order_list.append(order)
            print("Successfully added")
        else :
            print ("wrong spelling or we don't have it")   
        order = input()    


    return order_list


def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    # your code goes here!
    if total  >= 5 :
        return True
    else :
        return False   


def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    # your code goes here!
    for pr in order_list:
        if pr in menu :
            total += menu[pr]
        elif pr in original_flavors :
            total+= original_price 
        else :
            total += signature_price 
    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print("\nYour order is: ")
    # your code goes here!
    total = get_total_price(order_list)
    for order in order_list:
        print ("- %s" %(order))
    print("That'll be KD %s" %(total))    
    if accept_credit_card(total): 
        print("This order is eligible for credit card payment")
    else :
        print("This order is  not eligible for credit card payment") 
    print("Thank you for shopping at %s" %(cupcake_shop_name))    