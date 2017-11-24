import geopy
from pyzipcode import ZipCodeDatabase
from geopy.distance import great_circle

def getdistance(zipcode1, zipcode2, measure="miles"):
    zcdb = ZipCodeDatabase()
    
    ## get long/lat for zipcodes
    long1 = zcdb[zipcode1].longitude
    lat1 = zcdb[zipcode1].latitude
    long2 = zcdb[zipcode2].longitude
    lat2 = zcdb[zipcode1].latitude
    
    ## create coordinates for zipcodes
    zip1 = (lat1, long1)
    zip2 = (lat2, long2)
    
    ## calculate distance
    distance = great_circle(zip1, zip2)
    
    ## print
    if measure == "miles":
        return distance.miles
    else:
        return distance.km
