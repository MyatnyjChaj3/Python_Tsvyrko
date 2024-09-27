import random

import requests


class Ingredients:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def get_cost(self):
        return self.weight * self.price

class CookingStep:
    def __init__(self, description, time_to_cook):
        self.description = description
        self.time_to_cook = time_to_cook

class Recipe:
    def __init__(self, name, ingredients, steps):
        self.name = name
        self.ingredients = ingredients  # Уже передаем список объектов Ingredients
        self.steps = steps  # Уже передаем список объектов CookingStep

    def get_raw_weight(self):
        #return sum(ingredient.weight for ingredient in self.ingredients)
        total_weight = sum(ingredient.weight for ingredient in self.ingredients)
        if total_weight > 3.0:
            scaling_factor = 3.0 / total_weight
            for ingredient in self.ingredients:
                ingredient.weight *= scaling_factor
        return min(total_weight, 3.0)

    def get_cooked_weight(self):
        return self.get_raw_weight() * 0.9

    def get_cost(self):
        return sum(ingredient.get_cost() for ingredient in self.ingredients)

    def get_total_cooking_time(self):
        return sum(step.time_to_cook for step in self.steps)

class Favorites:
    def __init__(self):
        self.favorite_recipes = []

    def add_to_favorites(self, recipe):
        self.favorite_recipes.append(recipe)
        print(f"Рецепт '{recipe.name}' добавлен в Избранное.")

    def show_favorites(self):
        if not self.favorite_recipes:
            print("В Избранном пока нет рецептов.")
            return []
        print("Рецепты в Избранном:")
        for i, recipe in enumerate(self.favorite_recipes):
            print(f"{i + 1}. {recipe.name}")
        return self.favorite_recipes

class AutomaticCook:
    def __init__(self, recipes, favorites):
        self.recipes = recipes
        self.favorites = favorites

    def choose_recipe(self):
        print("Выберите рецепт для приготовления:")
        for i, recipe in enumerate(self.recipes):
            print(f"{i + 1}. {recipe.name}")
        choice = int(input("Введите номер рецепта: ")) - 1
        return self.recipes[choice]

    def simulate_cooking(self, num_dishes=1):
        recipe = self.choose_recipe()
        print(f"Начинаем приготовление блюда: {recipe.name}\n")
        print(f"Вес сырого продукта: {recipe.get_raw_weight() * num_dishes:.2f} кг")
        print(f"Вес готового продукта: {recipe.get_cooked_weight() * num_dishes:.2f} кг")
        print(f"Себестоимость одного блюда: {recipe.get_cost():.2f} руб.")
        print(f"Себестоимость {num_dishes} блюд: {recipe.get_cost() * num_dishes:.2f} руб.")
        print(f"Общее время приготовления: {recipe.get_total_cooking_time()} минут\n")

        for step in recipe.steps:
            print(step.description)

    def add_to_favorites(self, recipe):
        self.favorites.add_to_favorites(recipe)

    def show_favorites(self):
        return self.favorites.show_favorites()


def fetch_recipes(query):
    api_key = "4ed51e21d52d43e79655bd1032d3a4f5"
    offset = random.randint(0, 300)
    url = f"https://api.spoonacular.com/recipes/complexSearch?query={query}&number=5&offset={offset}&apiKey={api_key}"
    
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Ошибка при запросе данных: {response.status_code}")
        return []
    
    data = response.json()

    if 'results' not in data:
        print("Ключ 'results' не найден в ответе API.")
        print("Ответ от сервера:", data)
        return []
    
    recipes = []
    for item in data['results']:
        recipe_id = item['id']
        recipe_url = f"https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey={api_key}"
        recipe_response = requests.get(recipe_url)
        recipe_data = recipe_response.json()

        ingredients = []
        for ingredient in recipe_data.get('extendedIngredients', []):
            name = ingredient.get('name', 'Неизвестный ингредиент')
            amount = ingredient.get('amount', 0)
            price = 100  # Условная цена
            ingredients.append(Ingredients(name, amount, price))

        steps = []
        for step in recipe_data.get('analyzedInstructions', []):
            for instruction in step.get('steps', []):
                description = instruction.get('step', 'Нет описания шага')
                time_to_cook = instruction.get('length', {}).get('number', 0)
                steps.append(CookingStep(description, time_to_cook))

        recipes.append(Recipe(recipe_data['title'], ingredients, steps))
    
    return recipes

favorites = Favorites()
recipes = fetch_recipes("carrot")

if recipes:
    cooker = AutomaticCook(recipes, favorites)

    while True:
        choice = input("Выберите действие:\n1. Готовить новое блюдо\n2. Посмотреть Избранное\n3. Добавить в Избранное\n0. Выйти\n")
        if choice == '1':
            cooker.simulate_cooking(num_dishes=2)
        elif choice == '2':
            cooker.show_favorites()
        elif choice == '3':
            recipe = cooker.choose_recipe()
            cooker.add_to_favorites(recipe)
        elif choice == '0':
            break
        else:
            print("Неверный ввод, попробуйте снова.")
else:
    print("Рецепты не были найдены.")
