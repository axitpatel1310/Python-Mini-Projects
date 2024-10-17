def km_to_miles(km):
    return km * 0.6213171

def miles_to_km(miles):
    return miles / 0.6213171

def meter_to_cm(meter):
    return meter * 100

def cm_to_meter(cm):
    return cm / 100

def unit_converter():
    print("Unit Converter")
    print("1). Kilometer To Miles")
    print("2). Miles To Kilometer")
    print("3). Meter To Centimeter")
    print("4). Centimeter To Meter")
    choice = input("Choose Conversion (1/2/3/4): ")
    
    if choice == '1':
        km = float(input("Enter Kilometer: "))
        print(f'{km} kilometer is equal to {km_to_miles(km):.4f} miles')
    
    elif choice == '2':
        miles = float(input("Enter Miles: "))
        print(f'{miles} miles is equal to {miles_to_km(miles):.4f} km')
    
    elif choice == '3':
        meter = float(input("Enter Meter: "))
        print(f'{meter} meter is equal to {meter_to_cm(meter):.4f} cm')
    
    elif choice == '4':
        cm = float(input("Enter Cm: "))
        print(f'{cm} CM is equal to {cm_to_meter(cm):.4f} meter')
    
    else:
        print("invalid choice")
        
unit_converter()