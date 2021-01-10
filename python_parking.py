car=[0,0]
def waiting():
    print("Total no of waiting car are : "+str(car[0]))
    print("__________________________")
    return
def parking():
    print("Total no of parked car are : "+str(car[1]))
    return
def new_car_arrive():
    number=int(input('Enter no of car arived :'))
    car[0]+=number
    waiting()
    return 

def check_park():
    if car[0] >0:
        if car[1]<5:
            seet_available=5-car[1]
   
            if seet_available>= car[0]:
                car_parked=car[0]
            else:
                car_parked=seet_available
            car[0]-=car_parked
            print(str(car[0])+" Waiting car")
            car[1]=car_parked+car[1]
            print(str(car[1])+" Total car parked")
            print(str(car_parked)+" New car parked ")
            return()
        else:
            print(" Parking Full")
            print(str(car[0])+" Waiting Car")
    else:
        print(str(car[1])+" Car parked & "+str(car[0])+"  waiting car")

def car_leave():
    while True:
        value=int(input("Enter no of car leave : "))
        if value<=5 and value >= 0 and value <= car[1]:
            print("__________________________")
            break
        else:
            print("Total parked car "+str(car[1]))
            print("Enter value in limit ")
            print("__________________________")
    car[1]-=value
    return()
while True:
    print("---------------------------------------")
    print("---------------------------------------")
    print("1. car entery ")
    print("2. Leave car ")
    print("3. Check Waiting list ")
    print("4. Check Parked list ")
    print(" Press any key for exit ")
    print("__________________________")
    value=int(input("enter Choice from following  :"))
    if value==1:
        new_car_arrive()
        check_park()
    elif value==2:
        car_leave()
        check_park()
    elif value==3:
        waiting()
    elif value==4:
        parking()
    else:
        break