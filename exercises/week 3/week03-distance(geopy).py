import geopy
from geopy.distance import great_circle
destination=[(40.71,-74.00),(49.28,-123.12),(59.33,18.06),(-34.60,-58.40),(-31.89,115.86)]
departure=(22.33,114.15)
print('New York:{}'.format(great_circle(destination[0],departure).miles))
print('Vancouver:{}'.format(great_circle(destination[1],departure).miles))
print('Stockholm:{}'.format(great_circle(destination[2],departure).miles))
print('Buenos Aires:{}'.format(great_circle(destination[3],departure).miles))
print('Perth:{}'.format(great_circle(destination[4],departure).miles))