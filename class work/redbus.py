seats ={
    "u1" :{'booking_status':True,'gender':'M','price':1200,'sest_type':'sleeper','name':'suhas','age':23},
    "u2" :{'booking_status':True,'gender':'M','price':1200,'sest_type':'sleeper','name':'bunny','age':22},
    "u3" :{'booking_status':True,'gender':'M','price':1200,'sest_type':'sleeper','name':'manoj','age':21},
    "u4" :{'booking_status':False,'gender':None,'price':1200,'sest_type':'sleeper','name':None,'age':None},
    "u5" :{'booking_status':False,'gender':None,'price':1200,'sest_type':'sleeper','name':None,'age':None},
    "u6" :{'booking_status':True,'gender':'M','price':1200,'sest_type':'sleeper','name':'sanjay','age':35},
    "u7" :{'booking_status':True,'gender':'M','price':1200,'sest_type':'sleeper','name':'paparao','age':66},
    "u8" :{'booking_status':False,'gender':None,'price':1200,'sest_type':'sleeper','name':None,'age':None},
    "u9" :{'booking_status':False,'gender':None,'price':1200,'sest_type':'sleeper','name':None,'age':None},
    "l1" :{'booking_status':False,'gender':None,'price':1200,'sest_type':'sleeper','name':None,'age':None},

    
}
def display_seats():
    for i in seats:
        if seats[i]['booking_status']:
            print(f"Seat {i} is already booked.")
            if seats[i]['gender'] == 'M':
                print(f'**{i}**-M')
            else:
                print(f'**{i}**-F')
        else:
            print(f"Seat {i} is available for booking.price is {seats[i]['price']}")
def book_seat(selected_seat):
    seats[selected_seat]['booking_status'] = True
    seats[selected_seat]['name'] = input("Enter your name: ")
    seats[selected_seat]['age']= int(input("Enter your age: "))
    seats[selected_seat]['gender']= input("Enter your M or F: ").upper()
    if seats[selected_seat]['age'] <5:
        print(f"Seat {selected_seat} is free for children below 5 years.")
    elif seats[selected_seat]['age']>5 and seats[selected_seat]['age']<60:
        payment = int(input("enter the price :"))
        if payment == seats[selected_seat]['price']:
            print(f"Seat {selected_seat} is booked for adults.")            
        else:
            print("Payment failed. Please try again.")
    else:
        discount = seats[selected_seat]['price'] * 0.15
        price = seats[selected_seat]['price'] - discount
        payment = int(input(f"Enter the price after senior citizen discount of 15%: {int(price)}"))
        if payment == int(price):
            print(f"Seat {selected_seat} is booked for senior citizens.")
        else:
            print("Payment failed. Please try again.")
            seats[selected_seat]['booking_status'] = False

def search_seat(selected_seat):
    if selected_seat in seats:
        if seats[selected_seat]['booking_status']:
            print(f"Seat {selected_seat} is already booked.")
        else:
            book_seat(selected_seat)
            display_seats()
    else:
        print("Invalid seat number. Please try again.")
display_seats()

selected_seat=input("enter the seat number:")
search_seat(selected_seat)
        

