import os
import json
import shutil 

if os.path.isdir('output_data'):
    shutil.rmtree('output_data')

vehicles = []
header = []
slow_cars = []
fast_cars = []
sport_cars = []
cheap_cars = []
medium_cars = []
expensive_cars = []
cars = {}
brands = {}

# Parse the data
with open('input.csv', 'r') as file_csv:
    for nr_line, line in enumerate(file_csv.readlines()):
        if line.endswith('\n'):
            line = line[:-1]
        if nr_line == 0:
            header = line.split(', ')
        else:
            vehicles.append(line.split(', '))

# Categorize the data
for indx, x in enumerate(vehicles):
    car = f'{vehicles[indx][0]} {vehicles[indx][1]}'
    car_infos = {key:value for key,value in zip(header, vehicles[indx])}
    car_infos['id'] = indx + 1
    brand = car_infos['brand']
    cars[car] = car_infos
    price = int(cars[car]['price']) 
    if price < 1000:
        cheap_cars.append(car_infos)
    elif price < 5000:
        medium_cars.append(car_infos)
    else:
        expensive_cars.append(car_infos)
    hp = int(cars[car]['hp'])
    if hp < 120:
        slow_cars.append(car_infos)
    elif hp < 180:
        fast_cars.append(car_infos)
    else:
        sport_cars.append(car_infos)

    if brand in brands:
        car_list = brands[brand]
        car_list.append(car_infos)
        brands[brand] = car_list
    else:
        brands[brand] = [car_infos]

# Create categorized output
os.mkdir('output_data')
with open(os.path.join('output_data', 'slow_cars.json'), 'w') as json_file:
    json_file.write(json.dumps(slow_cars))

with open(os.path.join('output_data','fast_cars.json'), 'w') as json_file:
    json_file.write(json.dumps(fast_cars))

with open(os.path.join('output_data', 'sport_cars.json'), 'w') as json_file:
    json_file.write(json.dumps(sport_cars))

with open(os.path.join('output_data','cheap_cars.json'), 'w') as json_file:
    json_file.write(json.dumps(cheap_cars))

with open(os.path.join('output_data','medium_cars.json'), 'w') as json_file:
    json_file.write(json.dumps(medium_cars))

with open(os.path.join('output_data','expensive_cars.json'), 'w') as json_file:
    json_file.write(json.dumps(expensive_cars))

for brand in brands:
    with open(os.path.join('output_data', f'{brand}.json'), 'w') as brand_file:
        brand_file.write(json.dumps(brands[brand]))
    
print('Data categorization complete!')
