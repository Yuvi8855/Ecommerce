import random
def generate_bill ():
    pass
def view_all_dish():
    pass
def add_new_dish():
    pass
def update_dish_price():
    pass
def add_new_employee():
    e_id =str(random.randint(100,1000));
    e_name =input("employee name-");
    e_gen =input("employe gen-");
    e_age =input("emplyee age-");
    e_gmail=input("enter employee mail-");
    e_address=input("employee address");
    fobj = open("all employee,"'a');
    fobj.write(e_id+","+e_name+","+e_gen+","+e_gmail+","+e_address+",");
    fobj.close
    pass
def check_todays_income():
    pass
def total_income_on_specific__date():
    pass
def check_total_income_betweens_dates():
    pass
def exit():
    pass
 
while True:
    print("1-def generate_bill")
    print("2-view_all_dish")
    print("3-add_new_dish")
    print("4-update_dish_price")
    print("5-add_new_employee")
    print("6-check todays income")
    print("7-total_income_on_specific__date")
    print("8-check_total_income_betweens_dates")
    print("exit")
    ch=int(input("enter choice:"))
    if ch==1:
        generate_bill()
    if ch==2:
        view_all_dish()
    if ch==3:
        add_new_dish()
    if ch==4:
        update_dish_price()
    if ch==5:
        add_new_employee()
    if ch==6:
        check_todays_income()
    if ch==7:
        total_income_on_specific__date()
    if ch==8:
        check_total_income_betweens_dates()
    if ch==9:
        exit()


        
        
        



        



