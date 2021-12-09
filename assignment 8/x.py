#Does not exist Book Store
from pyfiglet import Figlet

f= Figlet(font="standard")
print(f.renderText( "Does not exist BookStore"))

my_list=[]
myfile = open("database.txt","r")
data = myfile.read().lower().split("\n")
for i in range(len(data)):
    product_info = data[i].split(',')
    my_dic = {}
    my_dic['id']= product_info[0]
    my_dic['name']= product_info[1]
    my_dic['price']= product_info[2]
    my_dic['count']= product_info[3]
    my_list.append(my_dic)

def show_menu():
    print("1- Show Items.")
    print("2- Add Items.")
    print("3- Edit Items.")
    print("4- Delete Item.")
    print("5- Buy Item.")
    print("6- Search Item.")
    print("7- Exit")

def Add_item():
    while True:
        dic_add={}
        add_item = input("Do you want to add a book item? Type yes or no  ")

        if add_item == "no":
            break
        elif add_item == "yes":
            dic_add["id"]= input("Please Enter Id: ")
            dic_add["name"]= input("please Enter Name: ")
            dic_add["price"]= input("Please Enter Price:  ")
            dic_add["count"]= input("Please Enter Count of book: ")
            print("Added 👍.")
            my_list.append(dic_add)

def Edit_item():
    while True:
        edit_item = input("Do you want to edit book information? Type yes or no . ")
        if edit_item=="yes":
            print("1- Edit id")
            print("2- Edit name ")
            print("3- Edit price ")
            print("4- Edit count ")

            edit_c = input("Please enter the operation code. ")
            print(my_list)
            choice_Edit = int(input("Please enter the operation code.1or2or3or4."))
            if   edit_c=="1":
                my_list[choice_Edit]["id"]= input("Please Enter Your Id for Edit= ")
            elif   edit_c=="2":
                my_list[choice_Edit]["name"]= input("Please Enter Your Name for Edit= ")
            elif   edit_c=="3":
                my_list[choice_Edit]["price"]= input("Please Enter Your Price for Edit= ")
            elif   edit_c=="4":
                my_list[choice_Edit]["count"]= input("Please Enter Your Count for Edit= ")
            
            print("Edit Is Successful.")

        elif edit_item=="no":
            break

def Delete_item():
    while True:
        delete_item = input("Do you want to delete a book? Type yes or no .")

        if delete_item=="no":
             break
        elif delete_item=="yes":
            choice_Delete = input("Please Enter Your Commpdity Id For Delete: ")
            for i in range(len(my_list)):
                if my_list[i]["id"]==choice_Delete:
                    my_list.pop(i)
                    print("Item deleted✌.")
                    break 

def Search_item():
    while True:
        search_item = input("Want to search for a book? Type yes or no  ")
        if search_item=="no":
            break
        elif search_item=="yes":
            nameofsearch = input("Please Enter Name of Book = ")
            for i in range(len(my_list)):
                if my_list[i]["name"]==nameofsearch:
                    print("Your Search is Ok")
                    print({"id":my_list[i]["id"]
                    ,"name":my_list[i]["name"]
                    ,"price":my_list[i]["price"]
                    ,"count":my_list[i]["count"]})
                    
                    break
            else:
                print("Error. book not available.😢 ")
                break

def buy_item():
    Total_price=0
    count=0
    factor=[]
    while True:
        
        buy_item = input("Do you want to buy a book? Type yes or no ")
        if buy_item=="yes":
            print(my_list)
            id_of_buy = input("Please Enter Your Id= ")
            for i in range(len(my_list)):
                if my_list[i]["id"]==id_of_buy:
                    print("Your Items is Ok.")
                    count_buy = int(input("Please Enter Count Of Book : "))
                    print("Your Factor is=")
                    fact={"price":my_list[i]["price"]
                    ,"sum_price":str(Total_price)
                    ,"sum_count":str(count)}
                    factor.append(fact)
                    print(factor)

                    break
                else: 
                    print(".Error ")
        elif buy_item == "no":
            break

while True:

    show_menu()

    choice = input("....Please Choose a Number Of Menu= ")

    if choice =="1":
        print(my_list)
        print(len(my_list))

    elif choice =="2":
        Add_item()

    elif choice =="3":
        Edit_item()

    elif choice =="4":
        Delete_item()

    elif choice == "5":
        buy_item()

    elif choice =="6":
        Search_item()

    elif choice =="7":
        exit()