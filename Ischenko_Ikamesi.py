
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
        self.ingredients = [Ingredients(*ingredient) for ingredient in ingredients]
        self.step = [CookingStep(*step) for step in steps]
    
    def get_raw_weight(self):
        return sum(ingredient.weight for ingredient in self.ingredients)

    def get_cooked_weight(self):
        return self.get_raw_weight() * 0.9

    def get_cost(self):
        return sum(ingredient.get_cost() for ingredient in self.ingredients)

    def get_total_cooking_time(self):
        return sum(step.time_to_cook for step in self.step)

class AutomaticCook:
    def __init__(self, recipe):
        self.recipe = recipe

    def simulate_cooking(self, num_dishes=1):
        print(f"Начинаем приготовление блюда: {self.recipe.name}\n")
        print(f"Вес сырого продукта: {self.recipe.get_raw_weight() * num_dishes:.2f} кг")
        print(f"Вес готового продукта: {self.recipe.get_cooked_weight() * num_dishes:.2f} кг")
        print(f"Себестоимость одного блюда: {self.recipe.get_cost():.2f} руб.")
        print(f"Себестоимость {num_dishes} блюд: {self.recipe.get_cost() * num_dishes:.2f} руб.")
        print(f"Общее время приготовления: {self.recipe.get_total_cooking_time()} минут\n")

        for step in self.recipe.step:
            print(step.description)
            

#рецепт блюда, вес в кг или литрах, цена руб за кг/л
ikamesi_recipe = {
    "name": "Икамэси",
    "ingredients": [
        ("Кальмар", 0.4, 500),
        ("Рис", 0.2, 100),
        ("Соевый соус", 0.05, 300),
        ("Сахар", 0.01, 50),
        ("Мирин", 0.05, 400)
    ],
    "steps": [
        ("Очистить кальмаров и приготовить рис", 15),
        ("Фаршировать кальмаров готовым рисом", 5),
        ("Смешать соевый соус, мирин и сахар, довести до кипения", 5),
        ("Добавить фаршированных кальмаров в соус и варить на медленном огне 20 минут", 25),
        ("Дать кальмарам настояться в соусе 10 минут", 10)
    ]
}

recipe = Recipe(ikamesi_recipe["name"], ikamesi_recipe["ingredients"], ikamesi_recipe["steps"])


cooker = AutomaticCook(recipe)


cooker.simulate_cooking(num_dishes=2)
