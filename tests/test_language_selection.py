import pytest
import rain

from fixtures import default_context, graph_existing, existing_a_node, existing_b_node
from fixture_graph_food import graph_food

@pytest.fixture
def selection_a(graph_existing):
    return rain.Selection("Node", "EXISTING_A_NODE")

@pytest.fixture
def selection_c_d_by_name(graph_existing):
    return rain.Selection("Node", name="C-D shares name")

@pytest.fixture
def selection_a_b():
    return rain.Selection("Node", "EXISTING_A_NODE", "EXISTING_B_NODE")

# TO DO: add tests that test for selections based keys only, properties only, and keys+properties (without labels)

def test_selection_a_contains_only_a_node(selection_a):
    assert rain.Node("EXISTING_A_NODE") in selection_a and rain.Node("EXISTING_B_NODE") not in selection_a

def test_selection_a_contains_only_a_key(selection_a):
    assert "EXISTING_A_NODE" in selection_a and "EXISTING_B_NODE" not in selection_a

def test_selection_a_b_contains_a_b_nodes(selection_a_b):
    assert rain.Node("EXISTING_A_NODE") in selection_a_b and rain.Node("EXISTING_B_NODE") in selection_a_b

def test_selection_a_b_list(selection_a_b):
    # note that this tests for the ORDER of selection
    # (which should match the order in which keys were specified)

    # TO DO MAYBE: use fixtures here instead of duplicating node instantiation code (if context can work out OK)
    assert list(selection_a_b) == [rain.Node("EXISTING_A_NODE", name="Existing A node"), rain.Node("EXISTING_B_NODE", name="Existing B node")]

def test_selection_c_d_by_name(selection_c_d_by_name):
    assert "EXISTING_C_NODE" in selection_c_d_by_name and "EXISTING_D_NODE" in selection_c_d_by_name and not "EXISTING_A_NODE" in selection_c_d_by_name

# TO DO: test language Relationship set_source and set_target

# ENABLE ONCE len() IMPLEMENTED
# def test_selection_a_b_len(selection_a_b):
#     assert len(selection_a_b) == 2


def test_sub_selection_1(graph_existing):
    # TO DO... better name for this

    rain.Node.create("ANOTHER_CD_NODE", name="C-D shares name")
    base_selection = rain.Selection("Node", name="C-D shares name")
    sub_selection = base_selection("Node", "EXISTING_D_NODE", "ANOTHER_CD_NODE")
    assert "EXISTING_D_NODE" in sub_selection and "ANOTHER_CD_NODE" in sub_selection and not "EXISTING_C_NODE" in sub_selection
 


def test_sub_selection_2(graph_existing):
    # TO DO... better name for this

    rain.Node.create("ANOTHER_CD_NODE", name="C-D shares name")
    base_selection = rain.Selection("Node", name="C-D shares name")
    sub_selection = base_selection(None, "EXISTING_D_NODE", "ANOTHER_CD_NODE")
    assert "EXISTING_D_NODE" in sub_selection and "ANOTHER_CD_NODE" in sub_selection and not "EXISTING_C_NODE" in sub_selection
 

def test_sub_selection_3(graph_existing):
    # TO DO... better name for this

    # ... testing that rogue KEY (non-existant)

    rain.Node.create("ANOTHER_CD_NODE", name="C-D shares name")
    base_selection = rain.Selection("Node", name="C-D shares name")
    sub_selection = base_selection(None, "EXISTING_D_NODE", "ANOTHER_CD_NODE", "BOOHAHA")
    assert "EXISTING_D_NODE" in sub_selection and "ANOTHER_CD_NODE" in sub_selection and not "EXISTING_C_NODE" in sub_selection
 

def test_sub_selection_r_sources_for_count(graph_food):
    select_soba_r_made_with = rain.Selection("Dish", "SOBA").r("->", "MADE_WITH")
    # soba is made with noodles and hondashi, so 2 -> MADE_WITH relationships
    assert(len(list(select_soba_r_made_with))==2)

def test_sub_selection_r_targets_for_count(graph_food):
    select_cuisine_r_in_cuisine = rain.Selection("Cuisine", "PUB_FOOD").r("<-", "IN_CUISINE")
    # burger, fries, pizza, and fish fry are all in cuisine pub food, so 4 <- IN_CUISINE relationships
    assert(len(list(select_cuisine_r_in_cuisine))==4)

def test_sub_selection_r_n_sources_for_nodes(graph_food):
    # cuisines with include pizza, wich is: italian and pub food
    pizza_cuisines = rain.Selection("Dish", "PIZZA").r("->", "IN_CUISINE").n()
    assert len(list(pizza_cuisines))==2 and "ITALIAN" in pizza_cuisines and "PUB_FOOD" in pizza_cuisines

def test_sub_selection_r_n_targets_nodes(graph_food):
    # everything made with cheese, which is: pizza and burgers
    made_with_cheese = rain.Selection("Ingredient", "CHEESE").r("<-", "MADE_WITH").n()
    assert len(list(made_with_cheese))==2 and "PIZZA" in made_with_cheese and "BURGER" in made_with_cheese

def test_tasty_pub_food_sides(graph_food):
    # fancier selection for all sides of pub food, if those sides are tasty (which is only mayonnaise)
    tasty_pub_food_sides = rain.Selection("Cuisine", "PUB_FOOD").r("<-", "IN_CUISINE").n("Dish").r("->", "SERVED_WITH").n(tasty=True)
    assert len(list(tasty_pub_food_sides))==1 and "MAYONNAISE" in tasty_pub_food_sides
