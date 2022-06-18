from time import sleep

class mhotel_manage:
    def __init__(self, clean_fund=0, room_rnt=0, f_cost=0, name="", addr="", checkin_d="", checkout_d="", room_no=1, sub_total=0, tip_amount=0, gst_tax=0):
        self.room_rnt = room_rnt
        self.f_cost = f_cost
        self.name = name
        self.addr = addr
        self.checkin_d = checkin_d
        self.checkout_d = checkout_d
        self.room_no = room_no
        self.sub_total = sub_total
        self.tip_amount = tip_amount
        self.clean_fund = clean_fund

        gst_tax = (self.sub_total*5)/100
        self.gst_tax = gst_tax

    def inp_data(self):
        self.name = input("\nEnter your full name: ")

        self.addr = input("\nEnter Your Address: ")

        self.checkin_d = input("\nEnter check in date: ")

        self.checkout_d = input("\nEnter check out date: ")

        print("\nCongrat's your entry has been taken, you will be assigned a room shortly.")

        print("\n\t Your room no. is: ", self.room_no)
        
    def room_manage(self):
        print("\nWe have following classes/categories in room service ! \n\t please choose right one for you:")

        print("\n1. Class A -- 6000$")

        print("\n2. Class B -- 4000$")

        print("\n3. Class C -- 2000$")

        print("\n4. Class D -- 1000$")

        room_choice = int(input("\nEnter your choice 1/2/3/4 ? "))

        n = int(input("\nEnter count of Days/Nights you have to stay ? "))

        if (room_choice == 1):
            print("\nYou have choosed class A")
            self.room_rnt = n*6000
        elif (room_choice == 2):
            print("\nYou have choosed class B")
            self.room_rnt = n*4000
        elif (room_choice == 3):
            print("\nYou have choosed class C")
            self.room_rnt = n*2000
        elif (room_choice == 4):
            print("\nYou have choosed class D")
            self.room_rnt = n*1000
        else:
            print("\nplease choose a room !")

        print("\nYour room rent for choosen category will be: ", self.room_rnt)

    def food_manage(self):
        print("|-------- Delicious Menu --------|")

        print("|--------------------------------|")
        print("|-------- 1. Dessert-100 --------|")
        print("|-------- 2. Namkeens-150 -------|")
        print("|-------- 3. Drinks-150 ---------|")
        print("|-------- 4. Soup-400 -----------|")
        print("|-------- 5. Noodals-50 ---------|")
        print("|-------- 6. Breakfast-80 -------|")
        print("|-------- 7. Lunch-75 -----------|")
        print("|-------- 8. Dinner-150 ---------|")
        print("|-------- 9. Snacks-80 ----------|")
        print("|-------- 10. Nonveg-600 --------|")
        print("|-------- 11. Exit or N/A -------|")
        print("|--------------------------------|")

        while(1):
            ch_ice = int(input("\nEnter the choise: "))

            if(ch_ice == 1):
                qntty = int(input("\nEnter the quantity: "))
                self.f_cost = self.f_cost + qntty*100
                break

            elif(ch_ice == 2):
                qntty = int(input("\nEnter the quantity: "))
                self.f_cost = self.f_cost + qntty*150
                break

            elif(ch_ice == 3):
                qntty = int(input("\nEnter the quantity: "))
                self.f_cost = self.f_cost + qntty*150
                break

            elif(ch_ice == 4):
                qntty = int(input("\nEnter the quantity: "))
                self.f_cost = self.f_cost + qntty*400
                break

            elif(ch_ice == 5):
                qntty = int(input("\nEnter the quantity: "))
                self.f_cost = self.f_cost + qntty*50
                break

            elif(ch_ice == 6):
                qntty = int(input("\nEnter the quantity: "))
                self.f_cost = self.f_cost + qntty*80
                break

            elif(ch_ice == 7):
                qntty = int(input("\nEnter the quantity: "))
                self.f_cost = self.f_cost + qntty*75
                break

            elif(ch_ice == 8):
                qntty = int(input("\nEnter the quantity: "))
                self.f_cost = self.f_cost + qntty*150
                break

            elif(ch_ice == 9):
                qntty = int(input("\nEnter the quantity: "))
                self.f_cost = self.f_cost + qntty*80
                break

            elif(ch_ice == 10):
                qntty = int(input("\nEnter the quantity: "))
                self.f_cost = self.f_cost + qntty*600
                break

            elif(ch_ice == 11):
                break
            else:
                print("\nPlease Enter a valid key: ")

        print("\nOverall cost of food is: ", self.f_cost)

    def mbill_display(self):
        print("\n|------- HOTEL AREA.95 -------|")

        print("|-----------------------------|")
        print("|--------- hotel bill --------|")
        print("|-----------------------------|")
        print("|----- |Customer Details| ----|")
        print("|-----------------------------|")

        print("\n----> Name: ", self.name)
        print("\n----> Address: ", self.addr)
        print("\n----> Check-in Date: ", self.checkin_d)
        print("\n----> Check-out Date: ", self.checkout_d)
        print("\n----> Room No.: ", self.room_no)
        print("\n----> Room Rent: ", self.room_rnt)
        print("\n----> Food cost: ", self.f_cost)

        tip_ch = input("\nDo you want to give tip for hotel staff ? y/n: ")
        tip_ch = tip_ch.lower()
        if (tip_ch == "y"):
            self.tip_amount = int(input("\nEnter tip amount: "))
            print('\nthanks sir ! please come again.')
        else:
            print("thanks")

        self.sub_total = self.room_rnt + self.f_cost + self.tip_amount + self.clean_fund

        print("\n------------------------------------")
        print("\n----> Sub total: ", self.sub_total)
        print("\n----> gst charges: ", self.gst_tax)

        print("\n----> grand total: ", (self.sub_total + self.gst_tax))
        print("\n------------------------------------")


        print("Thanks for choosing our services, please come again.")

        self.room_no += 1 # to update room no. after a booked room understand the code carefully

def main():


    objct = mhotel_manage()

    while(1):
        print("\n|----------------------------------|")
        print("|---------- HOTEL AREA.95 ---------|")
        print("|----------------------------------|\n")

        print("\n1. Customer Entry/Customer data.")

        print("\n2. Calculate room rent.")

        print("\n3. Calculate food cost.")

        print("\n4. Show grand total.")

        print("\n5. EXIT.")

        ch_main = int(input("\nEnter the choice: "))

        if (ch_main == 1):
            objct.inp_data()
            sleep(2)
        elif (ch_main == 2):
            objct.room_manage()
            sleep(2)
        elif (ch_main == 3):
            objct.food_manage()
            sleep(2)
        elif (ch_main == 4):
            objct.mbill_display()
            sleep(6) # sleep 6 seconds for new action
        elif (ch_main == 5):
            quit()


if __name__ == "__main__":
    main()