import os
import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import FoodForm

def food_form(request):
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            food = form.cleaned_data['food']
            amount = form.cleaned_data['amount']

            file_path = os.path.join(os.path.dirname(__file__), 'my_api.txt')
            with open(file_path, 'r') as f:
                api_data = f.readlines()
            for line in api_data:
                line_data = line.strip().split('=', 1)
                if len(line_data) == 2:
                    key, value = line_data
                    if key == 'apiKey':
                        api_key = value.replace('\\=', '=')
            
            response = requests.get(
                'https://api.nal.usda.gov/fdc/v1/foods/search',
                params={'query': food, 'api_key': api_key}
            )
            response.raise_for_status()
            data = response.json()
            food_nutrients = data['foods'][0]['foodNutrients']
            nutrients = {}
            for nutrient in food_nutrients:
                if nutrient['nutrientName'] == 'Energy':
                    nutrients['calories'] = amount * nutrient['value'] / 1000
                elif nutrient['nutrientName'] == 'Protein':
                    nutrients['protein'] = amount * nutrient['value'] / 100
                elif nutrient['nutrientName'] == 'Carbohydrate, by difference':
                    nutrients['carbs'] = amount * nutrient['value'] / 100
                elif nutrient['nutrientName'] == 'Total lipid (fat)':
                    nutrients['fat'] = amount * nutrient['value'] / 100
            return render(request, 'nutrients.html', {'nutrients': nutrients})
    else:
        form = FoodForm()
    return render(request, 'food.html', {'form': form})