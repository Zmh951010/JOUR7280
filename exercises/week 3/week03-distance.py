from math import radians, cos, sin, asin, sqrt
def haversine(lon1,lat1,lon2,lat2):
    lon1, lat1, lon2,lat2 = map(float, [lon1,lat1,lon2,lat2])
    dlon=abs(lon2-lon1)
    dlat=abs(lat2-lat1)
    a=sin(dlat/2)**2+cos(lat1)*cos(lat2)*sin(dlon/2)**2
    c=2*asin(sqrt(a))
    r=6371
    return c*r
print('distance from New York to Hongkong is: ', haversine(114.15,22.33,-74.00,40.71))
print('distance from Vancouver to Hongkong is: ', haversine(114.15,22.33,-123.12,49.28))
print('distance from Stockholm to Hongkong is: ', haversine(114.15,22.33,18.06,59.33))
print('distance from Buenos Aires to Hongkong is: ', haversine(114.15,22.33,-58.40,-34.60))
print('distance from Perth to Hongkong is: ', haversine(114.15,22.33,115.86,-31.88))
