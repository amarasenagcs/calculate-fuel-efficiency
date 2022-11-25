valid_type = ["1", "2", "3"]

user_name = input("User Name: ")
vehicle_type = input("User Vehicle Type (1-Car, 2-Bike, 3-SUV): ")
while vehicle_type not in valid_type:
    print('Invalid Input, Please Choose 1, 2 or 3')
    vehicle_type = input("User Vehicle Type (1-Car, 2-Bike, 3-SUV): ")

while True:
    try:
        tank_capacity = float(input("Vehicle Fuel Tank Capacity (L): "))
        if tank_capacity > 0 :
            break
        else:
            print("Please enter valid Tank Capacity (L)!")
    except ValueError:
        print("Please enter valid Tank Capacity (L)")
fuel_type = input("Fuel Type (1-92 Petrol, 2-95 Petrol, 3-Super Diesel): ")

while fuel_type not in valid_type:
    print('Invalid Input, Please Choose 1, 2 or 3')
    fuel_type = input("Fuel Type (1-92 Petrol, 2-95 Petrol, 3-Super Diesel): ")

while True:
    try:
        fuel_price = float(input("Fuel Price (Per L): "))
        if fuel_price > 0 :
            break
        else:
            print("Please enter valid Fuel Price!")
    except ValueError:
        print("Please enter valid fuel price!")
        
while True:
    try:
        pre_meter_reading = float(input("Previous Meter Reading (Km): "))
        if pre_meter_reading >= 0 :
            break
        else:
            print("Please enter valid Previous Meter Reading(km)!")
    except ValueError:
        print("Please enter valid Meter Reading(km)!")

while True:
    try:
        curr_meter_reading = float(input("Current Meter Reading (Km): "))
        if curr_meter_reading > 0 and curr_meter_reading > pre_meter_reading:
            break
        else:
            print("Please enter valid Current Meter Reading(km)!")
    except ValueError:
        print("Please enter valid Current Meter Reading (Km)!")


while True:
    try:
        fuel_pumped = float(input("How many Fuel you pumped Now (L): "))
        if fuel_pumped > 0 and fuel_pumped <= tank_capacity:
            break
        else:
            print("Please enter valid Fuel you pumped Now (L)!")
    except ValueError:
        print("Please enter valid Fuel you pumped Now (L)!")

confirm = input("Confirm or No (y-Confirm, n-No): ")

if confirm =='y' :
    distance = curr_meter_reading - pre_meter_reading
    fuel_eff = distance/fuel_pumped
    total_fuel_price = fuel_price*fuel_pumped

    def get_fuel_type(fuel_type):
        if fuel_type == '1':
            return '92 Petrol'
        elif fuel_type == '2':
            return '95 Petrol'
        else:
            return 'Super Diesel'

    print(f'''
    Hi {user_name}
    Previous Meter reading: {pre_meter_reading} Km
    Current Meter Reading: {curr_meter_reading} Km
    Pumped Fuel Type: {get_fuel_type(fuel_type)}
    Fuel Price (Per 1 L): {fuel_price:.2f} LKR
    Total Price: {total_fuel_price:.2f} LKR
    Fuel Efficiency (Per 1L): {fuel_eff} Km 
    Cost (Per 1L): {fuel_price:.2f} LKR
    ''')
    
else:
    print("Thank you, try this next time")