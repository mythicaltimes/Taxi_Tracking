import gmaps
from csv import reader

coordinates = {}
gmaps.configure(api_key='KEY_GOES_HERE')
with open("Taxi_Data.csv") as file:
    csv_reader = reader(file)

    #skip the header row of CSV
    next(csv_reader, None)

    for locations in csv_reader:
        pickup = float(locations[1]), float(locations[0])
        dropoff = float(locations[3]), float(locations[2])

fig = gmaps.figure()
layer = gmaps.directions.Directions(pickup, dropoff, mode='car')
fig.add(layer)
fig
