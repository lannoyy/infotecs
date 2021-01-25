from fastapi import FastAPI, HTTPException
from work_with_data import get_data, get_city_from_geonameid, \
    get_city_from_name, get_city_by_page, compare_two_cities, \
    get_simular_cities_from_name
from typing import Optional

app = FastAPI()

data = get_data()


@app.get("/city/geonameid/{geonameid}")
async def city_by_id(geonameid: int):
    city = get_city_from_geonameid(geonameid, data)
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
    cities = get_city_by_page(data, sheet, count_per_sheet)
    if cities:
        return cities
    raise HTTPException(status_code=404, detail="Item not found")


@app.get("/city/name/{name}")
async def city_by_name(name: str, second_city: Optional[str] = None):
    if second_city:
        city_1 = get_city_from_name(name, data)
        city_2 = get_city_from_name(second_city, data)
        if not city_1 or not city_2:
            raise HTTPException(
                status_code=404, detail="At least one item not found")
        output = compare_two_cities(city_1, city_2)
        if output:
            return output
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        city = get_city_from_name(name, data)
        if city:
            return city
        raise HTTPException(status_code=404, detail="Item not found")


@app.get("/city/like/{name}")
async def cities_like(name: str):
    cities = get_simular_cities_from_name(name, data)
    if cities:
        return cities
    raise HTTPException(status_code=404, detail="Item not found")
