from fastapi import FastAPI, HTTPException
from work_with_data import DataReader
from typing import Optional

app = FastAPI()

data = DataReader('RU.txt')


@app.get("/city/geonameid/{geonameid}")
async def city_by_id(geonameid: int):
    city = data.get_city_from_geonameid(geonameid)
    if city:
        return city
    raise HTTPException(status_code=404, detail="Item not found")


@app.get("/city/page/{count_per_sheet}/{sheet}")
async def cities_by_page(count_per_sheet: int, sheet: int):
    if count_per_sheet < 1:
        raise HTTPException(
            status_code=400, detail="count_per_sheet must be > 0")
    if sheet < 0:
        raise HTTPException(status_code=400, detail="sheet must be >= 0")
    cities = data.get_city_by_page(sheet, count_per_sheet)
    if cities:
        return cities
    raise HTTPException(status_code=404, detail="Item not found")


@app.get("/city/name/{name}")
async def city_by_name(name: str, second_city: Optional[str] = None):
    if second_city:
        city_1 = data.get_city_from_name(name)
        city_2 = data.get_city_from_name(second_city)
        if not city_1 or not city_2:
            raise HTTPException(
                status_code=404, detail="At least one item not found")
        output = data.compare_two_cities(city_1, city_2)
        if output:
            return output
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        city = data.get_city_from_name(name)
        if city:
            return city
        raise HTTPException(status_code=404, detail="Item not found")


@app.get("/city/like/{name}")
async def cities_like(name: str):
    cities = data.get_simular_cities_from_name(name)
    if cities:
        return cities
    raise HTTPException(status_code=404, detail="Item not found")
