## Geoname REST API

## Table of content

1. [Installation dependencies](#installation)
2. [Running](#launch)
3. [API](#apies)
4. [Credits](#credits)

## Installation dependencies <a name="installation"></a>

```bash
$ pip3 install -r requirements.txt
```

## Running the app <a name="launch"></a>

```bash
$ python3 script.py
```

## API <a name="apies"></a>

1) 
    url - localhost:8000/city/geonameid/{geonameid}

    Return city by geonameid
    
    Format:
    ```json
    {
        "geonameid": "451756",
        "name": "Zarech’ye",
        "asciiname": "Zarech'ye",
        "alternatenames": "",
        "latitude": "56.68265",
        "longitude": "34.70984",
        "feature_class": "P",
        "feature_code": "PPL",
        "country_code": "RU",
        "cc2": "",
        "admin1_code": "77",
        "admin2_code": "",
        "admin3_code": "",
        "admin4_code": "",
        "population": "0",
        "elevation": "",
        "dem": "178",
        "timezone": "Europe/Moscow",
        "modification_date": "2011-07-09\n"
    }
    ```
    With status 200

    If city not found, return:
    ```json
        {
            "detail": "Item not found"
        }
    ```
    
    with status 404


2) 
    url - localhost:8000/city/page/{count_per_sheet}/{sheet}

    Return page with cities
    Sheet start with 0!
    
    Format:
    ```json
    [
        {
        "geonameid": "451756",
        "name": "Zarech’ye",
        "asciiname": "Zarech'ye",
        "alternatenames": "",
        "latitude": "56.68265",
        "longitude": "34.70984",
        "feature_class": "P",
        "feature_code": "PPL",
        "country_code": "RU",
        "cc2": "",
        "admin1_code": "77",
        "admin2_code": "",
        "admin3_code": "",
        "admin4_code": "",
        "population": "0",
        "elevation": "",
        "dem": "178",
        "timezone": "Europe/Moscow",
        "modification_date": "2011-07-09\n"
    }
    ]
    ```
    With status 200

    If city not found, return:
    ```json
        {
        "detail": "Item not found"
    }
    ```
    

    With status 404


3) 
    url - localhost:8000/city/name/{city}?second_city={second_city}

    If second city skip return city by name
    
    Format:
    ```json
    {
        "geonameid": "451756",
        "name": "Zarech’ye",
        "asciiname": "Zarech'ye",
        "alternatenames": "",
        "latitude": "56.68265",
        "longitude": "34.70984",
        "feature_class": "P",
        "feature_code": "PPL",
        "country_code": "RU",
        "cc2": "",
        "admin1_code": "77",
        "admin2_code": "",
        "admin3_code": "",
        "admin4_code": "",
        "population": "0",
        "elevation": "",
        "dem": "178",
        "timezone": "Europe/Moscow",
        "modification_date": "2011-07-09\n"
    }
    ```
    With status 200

    If city not found, return:
    ```json
    {
        "detail": "Item not found"
    }
    ```
    
    with status 404


    If second city selected:

    ```json
    {
        "northern": {nothern city}, or "same"
        "timezone": true or false
    }
    ```

    If at least one city not found, return:
    ```json
    {
        "detail": "At least one item not found"
    }
    ```
    
    with status 404


4) 
    url - localhost:8000/city/like/{part_name}

    Return cities, which names contain part_name
    
    Format:
    ```json
    [
        {
        "geonameid": "451756",
        "name": "Zarech’ye",
        "asciiname": "Zarech'ye",
        "alternatenames": "",
        "latitude": "56.68265",
        "longitude": "34.70984",
        "feature_class": "P",
        "feature_code": "PPL",
        "country_code": "RU",
        "cc2": "",
        "admin1_code": "77",
        "admin2_code": "",
        "admin3_code": "",
        "admin4_code": "",
        "population": "0",
        "elevation": "",
        "dem": "178",
        "timezone": "Europe/Moscow",
        "modification_date": "2011-07-09\n"
    }
    ]
    ```
    With status 200

    If city not found, return:
    ```json
    {
        "detail": "Item not found"
    }
    ```
    
    with status 404


## Credits <a name="credits"></a>

- Author - Yury Ledovsky
- [Telegram](https://t.me/lannoyy)
- [Github](https://github.com/lannoyy)