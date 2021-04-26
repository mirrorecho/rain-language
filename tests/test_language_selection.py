import pytest

import rain

from fixtures import default_context, graph_existing, existing_a_node, existing_b_node

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


