#Python the hard way: excercise 39

# Dictionaries

states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print('-')
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

print('-')
print("Michigan's abbreviation is:", states['Michigan'])
print("Florida's abbreviation is:", states['Florida'])

print('-')
for abbrev, city in cities.items():
    print("%r has the city %r" %(abbrev, city))

print("-")
for state, abbrev in states.items():
    print("%r state is abbreviated %s and has the city %s" %(state, abbrev, cities[abbrev]))

print('-')
state = states.get('Texas', None)

if not state:
    print("Sorry, no Texas in here...")

city = cities.get('TX', 'Does not exist')
print("The city for the state 'TX' is %s" %city)
