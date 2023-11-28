"""
1. Load the JSON file below into Python as a dictionary

2. Convert it to a list

3. Calculate the maximum velocity and maximum height using recursion.
"""
#import the module
import json
import pprint

with open('telemetry2.json') as file:
    data = json.load(file)

pprint.pprint(data)



