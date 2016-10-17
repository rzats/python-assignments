route_numbers = [1, 2, 3, 5, 6, 7, 10]
routes = {}
for route_number in route_numbers:
    with open('resources/routes/route{0}.txt'.format(route_number), 'r') as fin:
        route_info = fin.read()
        route_set = set()
        for stop in route_info.split('-'):
            route_set.add(stop.strip())
        routes[route_number] = route_set

# Get all stops located in 3 or more routes.
counts = {}
for route in routes:
    for stop in routes[route]:
        if stop in counts:
            counts[stop] += 1
        else:
            counts[stop] = 1

for stop in counts:
    if counts[stop] >= 3:
        print(stop)

# Get all routes containing Ivan Franko St.
franko_routes = set()
for route in routes:
    if 'вул. І. Франка' in routes[route]:
        franko_routes.add(route)
print(franko_routes)

# Get all tram stops connected with Mytna Sqr.
mytna_stops = set()
for route in routes:
    if 'пл. Митна' in routes[route]:
        for stop in routes[route]:
            mytna_stops.add(stop)
print(mytna_stops)
