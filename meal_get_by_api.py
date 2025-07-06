# meal_get_by_api.py

import requests
import json
def get_meal():
    url='https://api.freeapi.app/api/v1/public/meals/8'
    response=requests.get(url)
    data=response.json()

    if data["success"] and "data" in data:
        meal_Data=data["data"]
        meal_name= meal_Data['strMeal']
        meal_instr= meal_Data['strInstructions']
        print(f"name : {meal_name}")
        print(f"instructions : {meal_instr}")
        for i in range(1, 21):  # strIngredient1 to strIngredient20
            ingredient = meal_Data.get(f"strIngredient{i}")
            measure =meal_Data.get(f"strMeasure{i}")
            
            if ingredient and ingredient.strip():
                print(f"{ingredient} - {measure}")
                

def main():
    try:
        get_meal()
    except Exception as e:
        print(str(e))

if __name__ =="__main__":
    main()