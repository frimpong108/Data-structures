# Brandes of cars and their prices
Car={ 'Toyota': '$1000', 'Lexus': '$1500', 'Nissan': '$2000', 'Ford':'$2500',\
      'Acura':'$3000', 'Bentley':'$3500', 'BMW':'$4000', 'Bugati':'$4500',\
      'Chevrolet':'$5000', 'Cadillac':'$5500', 'Corvette':'$6000', 'Dodge':'$6500',\
      'Fiat':'$7000', 'Ferrari':'$7500', 'GMC':'$8000', 'Honda':'$8500',\
      'Hyundai':'$9000', 'Isuzu':'$9500', 'Jeep':'$10000', 'Jaguar':'$10500',\
    'Mazda':'$11000', 'Mercedes Benz':'$11500', 'McLaren':'$12000', 'Opel':'$12500',\
  'Peugeot':'$13000', 'Pagani':'$13500', 'Porsche':'$14000', 'Renault':'$14500',\
     'Scion':'$15000', 'Suzuki':'$15500', 'Tesla':'$16000'}
  
carName=input('Which type of car do you want:')  
if carName in Car:
    print('The price of the ' +  carName  +  'is'  +  Car[carName])
else:
    print('Car is not in stock please visit yaantwi motors')
#https://github.com/frimpong108/Data-structures    

    
