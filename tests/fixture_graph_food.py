from dataclasses import dataclass
import pytest
import rain

from fixtures import default_context, setup_empty_context

@pytest.fixture
def graph_food(default_context):
    """
    A graph model/data with enough complexity to test more sophisticated operations...
    but still simple enough to be able to understand quickly in its entirety.
    """
    setup_empty_context()

    @dataclass
    class Cuisine(rain.Node):
        country:str = None
        description:str = None

    @dataclass
    class Food(rain.Node):
        tasty:bool = None
        description:str = None
    
    @dataclass
    class Dish(Food):
        difficulty:int = 3 #1-5 rating level of how diffult to make

    @dataclass
    class Ingredient(Food):
        color:str = None

    @dataclass
    class InCuisine(rain.Relationship):
        iconic:bool = False

    @dataclass
    class MadeWith(rain.Relationship):
        required:bool = True
        # percent_volume: int = None # TO CONSIDER... if need more sophistication in tests (weighting)

    @dataclass
    class ServedWith(rain.Relationship):
        pass

    rain.context.register_types(Cuisine, Food, Dish, Ingredient, InCuisine, MadeWith, ServedWith)

    japanese = Cuisine.create("JAPANESE", name="Japanese", country="Japan")
    italian = Cuisine.create("ITALIAN", name="Italian", country="Italy")
    pub_food = Cuisine.create("PUB_FOOD", name="Pub food", 
        description="Only the best bar food."
        )
    # test for edge case: cuisine with no dishes:
    olympian = Cuisine.create("Olympian", name="Olympian", country="Greece",
        description = "Olympians don't eat food. They eat Ambrosia!"
        ) 

    sashimi = Dish.create("SASHIMI", name="Sashimi", tasty=True, difficulty=5)
    soba = Dish.create("SOBA", name="Soba noodles", tasty=True, difficulty=1)
    pizza = Dish.create("PIZZA", name="Pizza", tasty=True, difficulty=4)
    pasta = Dish.create("PASTA", name="Pasta with red sauce", tasty=True, difficulty=1)
    burger = Dish.create("BURGER", name="Burger") # test with default tasty (undefined) and difficulty (3)
    fries = Dish.create("FRIES", name="French Fries") # another test with default tasty (undefined) and difficulty (3)
    tuna_salad = Dish.create("TUNAFISH", "Tunafish \"salad\"", tasty=False, difficulty=1)
    fish_fry = Dish.create("FISH_FRY", name="Deep fried fish", difficulty=2) # with default tasty (undefined)
    # test for edge case with dish that has no cuisines or defined ingredients:
    mystery_mash = Dish.create("MASH", name="Mystery Mash", tasty=False, difficulty=1)

    fish = Ingredient.create("FISH", name="Fish")
    noodles = Ingredient.create("NOODLES", "Noodles or pasta")
    hondashi = Ingredient.create("HONDASHI", name="Hondashi")
    cheese = Ingredient.create("CHEESE", name="Cheese", tasty=True)
    sauce = Ingredient.create("TOMATO_SAUCE", name="Tomato sauce", color="red")
    tomato = Ingredient.create("TOMATO", name="Tomato", color="red")
    onion = Ingredient.create("ONION", name="Onion", color="white")
    crust = Ingredient.create("CRUST", name="Pizza crust", color="brown", tasty=False)
    pepperoni = Ingredient.create("PEPPERONI", name="Pizza crust", color="red", tasty=True)
    bun = Ingredient.create("BUN", name="Fancy brioche bun", color="brown", tasty=False)
    venison = Ingredient.create("VENISON", name="Ground venison", color="red")
    bacon = Ingredient.create("BACON", name="Bacon", color="red", tasty=True)
    potato = Ingredient.create("POTATO", name="Potato", color="white")
    mayonnaise = Ingredient.create("MAYONNAISE", name="Mayonnaise", tasty=True)
    tartar_sauce = Ingredient.create("TARTAR_SAUCE", name="Tartar sauce", tasty=False)
    # test for edge case: ingredient never used in dish
    # add peach tartar!
    stone = Ingredient.create("STONE", name="Stone", color="grey",
        description = "Should I eat the stones in stone soup?"
        ) 

    InCuisine.create(source=sashimi, target=japanese, iconic=True)
    InCuisine.create(source=soba, target=japanese)
    InCuisine.create(source=pizza, target=italian, iconic=True)
    InCuisine.create(source=pasta, target=italian, iconic=True)
    InCuisine.create(source=burger, target=pub_food, iconic=True)
    InCuisine.create(source=fries, target=pub_food, iconic=True)
    InCuisine.create(source=pizza, target=pub_food)
    InCuisine.create(source=fish_fry, target=pub_food)

    MadeWith.create(source=sashimi, target=fish)
    MadeWith.create(source=soba, target=noodles)
    MadeWith.create(source=soba, target=hondashi)
    MadeWith.create(source=pizza, target=pepperoni)
    MadeWith.create(source=pizza, target=cheese)
    MadeWith.create(source=pizza, target=sauce)
    MadeWith.create(source=pizza, target=crust)
    MadeWith.create(source=pizza, target=onion, required=False)
    MadeWith.create(source=pizza, target=tomato, required=False)
    MadeWith.create(source=pizza, target=bacon, required=False)
    MadeWith.create(source=pasta, target=noodles)
    MadeWith.create(source=pasta, target=sauce)
    MadeWith.create(source=burger, target=bun)
    MadeWith.create(source=burger, target=venison)
    MadeWith.create(source=burger, target=bacon, required=True) # just to emphasize: bacon is REQUIRED on burgers
    MadeWith.create(source=burger, target=cheese, required=True) # ditto for cheese
    MadeWith.create(source=burger, target=onion, required=False)
    MadeWith.create(source=burger, target=tomato, required=False)
    MadeWith.create(source=burger, target=mayonnaise, required=False)
    MadeWith.create(source=fries, target=potato)
    MadeWith.create(source=tuna_salad, target=fish)
    MadeWith.create(source=tuna_salad, target=mayonnaise)
    MadeWith.create(source=fish_fry, target=fish)

    # ingredients made with other ingredients
    MadeWith.create(source=hondashi, target=fish)
    MadeWith.create(source=sauce, target=tomato)
    MadeWith.create(source=sauce, target=onion, required=False)
    MadeWith.create(source=tartar_sauce, target=mayonnaise)

    ServedWith.create(source=pasta, target=cheese)
    ServedWith.create(source=fish_fry, target=tartar_sauce)
    ServedWith.create(source=burger, target=fries)
    ServedWith.create(source=fries, target=mayonnaise)

    return rain.context.graph