import pytest
from dataclasses import dataclass, field

import rain

from fixtures import (default_context, new_a_node, existing_a_node, existing_b_node, 
    new_b_a_relationship, created_node)


def test_language_type_registry(default_context):
    assert rain.context.get_type("Node") is rain.Node

def test_language_default_graph(new_a_node):
    assert new_a_node.graph is rain.context.graph

def test_language_key(default_context):
    node_auto_keyed = rain.Node() # not using node fixture, in order to test auto key generation
    assert node_auto_keyed.get_key() != "" and node_auto_keyed.get_key() is not None

def test_node_get_properties(new_a_node):
    assert new_a_node.get_properties() == {"name":"New A node"}

def test_language_set_properties(new_a_node):
    new_a_node.set_properties(name="Ferdinand")
    assert new_a_node.name == "Ferdinand"

def test_language_create(created_node):
    assert "CREATED_NODE" in rain.context.graph

def test_language_merge_new(default_context):
    rain.context.init_empty_graph()
    node_merged = rain.Node.merge("YO")
    assert "YO" in rain.context.graph

def test_language_merge_existing(created_node):
    node_merged = rain.Node.merge("CREATED_NODE", name="[name_new]")
    assert rain.context.graph.get_properties("CREATED_NODE")["name"] == "[name_new]"

def test_language_save(created_node):
    created_node.name="[name_new]"
    created_node.save()
    assert rain.context.graph.get_properties("CREATED_NODE")["name"] == "[name_new]"

def test_language_delete(created_node):
    created_node.delete()
    assert "CREATED_NODE" not in rain.context.graph

def test_language_subclass_properties(default_context):
    @dataclass
    class SubNode(rain.Node):
        sub_name: str = "Ha"
    n = SubNode(name="Yo")
    assert n.get_properties() == {"name":"Yo", "sub_name":"Ha"}

def test_node_subclass_labels(default_context):
    @dataclass
    class SubNode(rain.Node): pass
    @dataclass
    class SubSubNode(SubNode): pass
    n = SubSubNode(name="Yo")
    assert n.get_labels() == ["SubSubNode", "SubNode", "Node"]

def test_relationship_source_key(new_b_a_relationship):
    assert new_b_a_relationship.source_key == "EXISTING_B_NODE"

def test_relationship_target_key(new_b_a_relationship):
    assert new_b_a_relationship.target_key == "EXISTING_A_NODE"

def test_relationship_sublass_properties(default_context):
    @dataclass
    class SubRelationship(rain.Relationship):
        sub_name: str = "Ha"
    r = SubRelationship(name="Yo")
    assert r.get_properties() == {"name":"Yo", "sub_name":"Ha"}

def test_relationship_sublass_type(default_context):
    @dataclass
    class SubRelationship(rain.Relationship): pass
    r = SubRelationship()
    assert r.get_label() == "SUB_RELATIONSHIP"

def test_relationship_from_keys(default_context):
    r = rain.Relationship.from_keys("A_NODE2", "B_NODE2")
    assert r.source_key == "A_NODE2" and r.target_key == "B_NODE2"