import pytest

from dataclasses import dataclass, field

import rain

@pytest.fixture
def node():
    return rain.Node("YO", name="Yo")

@pytest.fixture
def relationship():
    return rain.Relationship("A_TO_B", source=rain.Node("A_NODE"), target=rain.Node("B_NODE"))

@pytest.fixture
def node_created():
    # note, must always call clear on rain.DEFAULT_GRAPH before
    # making any changes to graph (to avoid tests interfering with one another)
    rain.DEFAULT_GRAPH.clear()
    return rain.Node.create("YO")

def test_language_type_registry():
    assert rain.get_type("Node") is rain.Node

def test_language_default_grapth(node):
    assert node.graph is rain.DEFAULT_GRAPH

def test_language_key():
    node_auto_keyed = rain.Node() # not using node fixture, in order to test auto key generation
    assert node_auto_keyed.get_key() != "" and node_auto_keyed.get_key() is not None

def test_node_get_properties(node):
    assert node.get_properties() == {"name":"Yo"}

def test_language_set_properties(node):
    node.set_properties(name="Ferdinand")
    assert node.name == "Ferdinand"

def test_language_create(node_created):
    assert "YO" in rain.DEFAULT_GRAPH

def test_language_merge_new():
    rain.DEFAULT_GRAPH.clear()
    node_merged = rain.Node.merge("YO")
    assert "YO" in rain.DEFAULT_GRAPH

def test_language_merge_existing(node_created):
    node_merged = rain.Node.merge("YO", name="[name_new]")
    assert rain.DEFAULT_GRAPH.get_properties("YO")["name"] == "[name_new]"

def test_language_save(node_created):
    node_created.name="[name_new]"
    node_created.save()
    assert rain.DEFAULT_GRAPH.get_properties("YO")["name"] == "[name_new]"

def test_language_delete(node_created):
    node_created.delete()
    assert "YO" not in rain.DEFAULT_GRAPH

def test_language_subclass_properties():
    @dataclass
    class SubNode(rain.Node):
        sub_name: str = "Ha"
    n = SubNode(name="Yo")
    assert n.get_properties() == {"name":"Yo", "sub_name":"Ha"}

def test_node_subclass_labels():
    @dataclass
    class SubNode(rain.Node): pass
    @dataclass
    class SubSubNode(SubNode): pass
    n = SubSubNode(name="Yo")
    assert n.labels == ["SubSubNode", "SubNode", "Node"]

def test_relationship_source_key(relationship):
    assert relationship.source_key == "A_NODE"

def test_relationship_target_key(relationship):
    assert relationship.target_key == "B_NODE"

def test_relationship_sublass_properties():
    @dataclass
    class SubRelationship(rain.Relationship):
        sub_name: str = "Ha"
    r = SubRelationship(name="Yo")
    assert r.get_properties() == {"name":"Yo", "sub_name":"Ha"}

def test_relationship_sublass_type():
    @dataclass
    class SubRelationship(rain.Relationship): pass
    r = SubRelationship()
    assert r.relationship_type == "SubRelationship"

def test_relationship_from_keys():
    r = rain.Relationship.from_keys("A_NODE2", "B_NODE2")
    assert r.source_key == "A_NODE2" and r.target_key == "B_NODE2"