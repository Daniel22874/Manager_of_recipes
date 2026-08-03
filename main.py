recipes = []


def add_recipe(name, ingredients):
    recipes.append({"name": name, "ingredients": ingredients})


def show_recipes():
    for r in recipes:
        print(f"{r['name']}: {', '.join(r['ingredients'])}")


if __name__ == "__main__":
    add_recipe("Омлет", ["яйца", "молоко", "соль"])
    add_recipe("Борщ", ["свекла", "капуста", "картофель", "мясо"])
    show_recipes()
