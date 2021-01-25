from time import time


def get_time(function_to_decorate):
    def wrapper(*args):
        t1 = time()
        func = function_to_decorate(*args)  # Сама функция
        t2 = time()
        print(t2-t1)
        return func
    return wrapper


class DataReader():

    def __init__(self, file_name):
        with open(file_name) as rfile:
            self.data = {}
            for string in rfile:
                geonameid, name, asciiname, \
                    alternatenames, latitude, longitude, \
                    feature_class, feature_code, country_code, \
                    cc2, admin1_code, admin2_code, admin3_code, \
                    admin4_code, population, elevation, dem, timezone, \
                    modification_date = string.split('\t')
                self.data[int(geonameid)] = ({'geonameid': geonameid, 'name': name, 'asciiname': asciiname,
                                              'alternatenames': alternatenames,
                                              'latitude': latitude, 'longitude': longitude,
                                              'feature_class': feature_class, 'feature_code': feature_code,
                                              'country_code': country_code, 'cc2': cc2, 'admin1_code': admin1_code,
                                              'admin2_code': admin2_code, 'admin3_code': admin3_code,
                                              'admin4_code': admin4_code, 'population': population,
                                              'elevation': elevation, 'dem': dem, 'timezone': timezone,
                                              'modification_date': modification_date})

    def sort_by_population(self, data: dict) -> dict:
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

    def get_city_from_geonameid(self, geonameid: int) -> dict:
        try:
            return self.data[geonameid]
        except KeyError:
            return None

    def get_city_from_name(self, city: str) -> dict:
        output = []
        for value in self.data.values():
            if city == value['name']:
                output.append(value)
        if len(output) > 1:
            output = self.sort_by_population(output)
        if output:
            return output[0]
        return None

    def get_city_by_page(self, sheet: int, count_per_sheet: int) -> list:
        array = list(self.data.values())
        try:
            return array[(count_per_sheet * sheet):((sheet + 1) * count_per_sheet)]
        except IndexError:
            if len(array) < count_per_sheet * sheet:
                return None
            else:
                return array[(count_per_sheet * sheet):((sheet + 1) * count_per_sheet)]

    def get_simular_cities_from_name(self, city: str) -> dict:
        output = []
        for value in self.data.values():
            if city in value['name']:
                output.append(value)
        return output

    def compare_two_cities(self, city_1: dict, city_2: dict) -> dict:
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
