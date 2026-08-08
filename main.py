import json

recipes = []


def save_to_file():
    with open("recipes.json", "w") as f:
        json.dump(recipes, f)


def load_from_file():
    global recipes
    try:
        with open("recipes.json", "r") as f:
            recipes = json.load(f)
    except FileNotFoundError:
        recipes = []


def add_recipe(name, ingredients):
    recipes.append({"name": name, "ingredients": ingredients})


def delete_recipe(name, ingredients):
    recipes.remove({"name": name, "ingredients": ingredients})


def show_recipes():
    for idx, r in enumerate(recipes, 1):
        print(f"Рецепт #{idx}: {r['name']}")
        print(f"Ингредиенты: {', '.join(r['ingredients'])}")
        print()


if __name__ == "__main__":
    load_from_file()
    add_recipe("Омлет", ["яйца", "молоко", "соль"])
    add_recipe("Борщ", ["свекла", "капуста", "картофель", "мясо"])
    show_recipes()
