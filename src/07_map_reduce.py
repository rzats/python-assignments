import functools
import json
import pprint

laptops = {}
with open('resources/laptops.json', 'r') as fin:
    laptops = json.loads(fin.read())

# Generate a short summary of the purchased laptops (using map/reduce/filter).
summary = list(map(lambda laptop: 'Name: {} | Price: {}'.format(laptop['name'], laptop['cart_price']), laptops))
summary.append('Total price: {}'.format(functools.reduce(lambda a, b: a + b, map(lambda laptop: laptop['cart_price'], laptops))))

# If there are laptops with prices better than the current selection, add info about them to the summary.
better_priced_laptops = filter(lambda laptop: laptop['cart_price'] > functools.reduce(lambda a, b: a if a < b else b, laptop['alternative_prices']), laptops)
summary.extend(list(map(lambda laptop: '{} has a better price: {} ({:.2f}% discount)'
                        .format(laptop['name'], min(laptop['alternative_prices']), 100 * laptop['cart_price'] / min(laptop['alternative_prices']) - 100), better_priced_laptops)))
                    
pp = pprint.PrettyPrinter(indent = 4)
pp.pprint(summary)
