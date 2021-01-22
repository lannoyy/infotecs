from time import time

def get_time(function_to_decorate):
     def wrapper(*args):
         t1 = time()
         func = function_to_decorate(*args) # Сама функция
         t2 = time()
         print(t2-t1)
         return func
     return wrapper


# @get_time
def sort_by_population(data):
    output = []
    max = data[0]['population']
    for city in data:
        if city['population'] > max:
            max = city['population']
            output = []
            output.append(city)
        elif city['population'] == max:
            output.append(city)
    return output
        

# @get_time
def get_data() -> dict:
    with open('RU.txt') as rfile:
        data = {}
        for string in rfile:
            geonameid, name, asciiname, \
            alternatenames, latitude, longitude, \
            feature_class, feature_code, country_code, \
            cc2, admin1_code, admin2_code, admin3_code, \
            admin4_code, population, elevation, dem, timezone, \
            modification_date = string.split('\t')
            data[int(geonameid)] = ({'name': name, 'asciiname': asciiname, 'alternatenames': alternatenames, \
                'latitude': latitude, 'longitude': longitude, 'feature_class': feature_class, 'feature_code': feature_code, \
                'country_code': country_code, 'cc2': cc2, 'admin1_code': admin1_code, 'admin2_code': admin2_code, 'admin3_code': admin3_code, \
                    'admin4_code': admin4_code, 'population': population, 'elevation': elevation, 'dem': dem, 'timezone': timezone, \
                        'modification_date': modification_date})
    return data


# @get_time
def get_city_from_geonameid(geonameid:int, data:dict) -> dict:
    try:
        return data[geonameid]
    except KeyError:
        return None


# @get_time
def get_city_from_name(city:str, data:dict) -> dict:
    output = []
    for element in data.values():
        if city == element['name']:
            output.append(element)
    if len(output) > 1:
        output = sort_by_population(output)
    if output:
        return output[0]
    return None


# @get_time
def get_city_by_page(data:dict, sheet:int, count_per_sheet:int):
    array = list(data.values())
    try:
        return array[(count_per_sheet * sheet):((sheet + 1) * count_per_sheet)]
    except IndexError:
        if len(array) < count_per_sheet * sheet:
            return None
        else:
            return array[(count_per_sheet * sheet):((sheet + 1) * count_per_sheet)]


# @get_time
def get_simular_cities_from_name(city:str, data:dict) -> dict:
    output = []
    for element in data.values():
        if city in element['name']:
            output.append(element)
    return output


# @get_time
def compare_two_cities(city_1:dict, city_2:dict) -> dict:
    output = {}
    if city_1['latitude'] > city_2['latitude']:
        output['northern'] = city_1
    elif city_1['latitude'] < city_2['latitude']:
        output['northern'] = city_2 
    else:
        output['northern'] = 'same'
    if city_1['timezone'] == city_2['timezone']:
        output['timezone'] = True
    else:
        output['northern'] = False 
    return output