import os
import json
import shutil 

output_folder = 'output_data'

if os.path.isdir(output_folder):
    shutil.rmtree(output_folder)

vehicles = {}
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
            vehicles[f'{nr_line}'] = {key:value for key,value in zip(header, line.split(', '))}

# Categorize the data
for car_id in vehicles:
    car_name = f'{vehicles[car_id]["brand"]} {vehicles[car_id]["model"]}'
    car_infos = vehicles[car_id]
    car_infos['id'] = int(car_id)
    brand = car_infos['brand']
    cars[car_name] = car_infos

    price = int(cars[car_name]['price']) 
    if price < 1000:
        cheap_cars.append(car_infos)
    elif price < 5000:
        medium_cars.append(car_infos)
    else:
        expensive_cars.append(car_infos)

    hp = int(cars[car_name]['hp'])
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
os.mkdir(output_folder)

with open(os.path.join(output_folder, 'slow_cars.json'), 'w') as json_file:
    json_file.write(json.dumps(slow_cars))

with open(os.path.join(output_folder,'fast_cars.json'), 'w') as json_file:
    json_file.write(json.dumps(fast_cars))

with open(os.path.join(output_folder, 'sport_cars.json'), 'w') as json_file:
    json_file.write(json.dumps(sport_cars))

with open(os.path.join(output_folder,'cheap_cars.json'), 'w') as json_file:
    json_file.write(json.dumps(cheap_cars))

with open(os.path.join(output_folder,'medium_cars.json'), 'w') as json_file:
    json_file.write(json.dumps(medium_cars))

with open(os.path.join(output_folder,'expensive_cars.json'), 'w') as json_file:
    json_file.write(json.dumps(expensive_cars))

for brand in brands:
    with open(os.path.join(output_folder, f'{brand}.json'), 'w') as brand_file:
        brand_file.write(json.dumps(brands[brand]))
    
print("Data categorization complete!")
