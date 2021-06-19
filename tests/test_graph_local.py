import pytest
import rain

from fixtures import (default_context, new_a_node, new_b_node, new_b_a_relationship, 
    existing_a_node, existing_b_node, existing_a_b_relationship, 
    graph_empty, graph_existing)


def test_context_graph(default_context):
    assert isinstance(rain.context.graph, rain.GraphInterface)

def test_create_node(graph_empty, new_a_node):
    graph_empty.create(new_a_node)
    assert new_a_node.key in graph_empty

def test_read_node(graph_existing, existing_a_node):
    existing_a_node.name = "[name to be replaced on read]"
    graph_existing.read(existing_a_node)
    assert existing_a_node.name == "Existing A node"

def test_save_node(graph_existing, existing_a_node):
    existing_a_node.name = "[giving node A a new name]"
    graph_existing.save(existing_a_node)
    assert graph_existing.get_properties(existing_a_node.key)["name"] == "[giving node A a new name]"

def test_merge_new_node(graph_empty, new_a_node):
    graph_empty.merge(new_a_node)
    assert new_a_node.key in graph_empty
    
def test_merge_existing_node(graph_existing, existing_a_node):
    existing_a_node.name = "[giving node A a new name]"
    graph_existing.merge(existing_a_node)
    assert graph_existing.get_properties(existing_a_node.key)["name"] == "[giving node A a new name]"

def test_delete_node(graph_existing, existing_a_node):
    a_existed_before_delete = (existing_a_node.key in graph_existing)
    graph_existing.delete(existing_a_node.key)
    assert a_existed_before_delete and (existing_a_node.key not in graph_existing)

def test_delete_node_deletes_source_relationships(graph_existing, existing_a_node, existing_a_b_relationship):
    rel_existed_before_delete = (existing_a_b_relationship.key in graph_existing)
    graph_existing.delete(existing_a_node.key)
    assert rel_existed_before_delete and (existing_a_b_relationship.key not in graph_existing)

def test_delete_node_deletes_target_relationships(graph_existing, existing_b_node, existing_a_b_relationship):
    rel_existed_before_delete = (existing_a_b_relationship.key in graph_existing)
    graph_existing.delete(existing_b_node.key)
    assert rel_existed_before_delete and (existing_a_b_relationship.key not in graph_existing)

def test_create_relationship(graph_existing, new_b_a_relationship):
    graph_existing.create(new_b_a_relationship)
    assert new_b_a_relationship.key in graph_existing

def test_read_relationship(graph_existing, existing_a_b_relationship):
    graph_existing.read_relationship(existing_a_b_relationship)
    assert existing_a_b_relationship.source_key == "EXISTING_A_NODE" and existing_a_b_relationship.target_key == "EXISTING_B_NODE"

def test_read_relationship(graph_existing, existing_a_b_relationship):
    existing_a_b_relationship.name = "[name to be replaced on read]"
    graph_existing.read(existing_a_b_relationship)
    assert existing_a_b_relationship.name == "Existing relate A to B"

def test_save_relationship(graph_existing, existing_a_b_relationship):
    existing_a_b_relationship.name = "[giving relationship A to B a new name]"
    graph_existing.save(existing_a_b_relationship)
    assert graph_existing.get_properties(existing_a_b_relationship.key)["name"] == "[giving relationship A to B a new name]"

def test_merge_new_relationship(graph_existing, new_b_a_relationship):
    graph_existing.merge(new_b_a_relationship)
    assert new_b_a_relationship.key in graph_existing

def test_merge_existing_relationship(graph_existing, existing_a_b_relationship):
    existing_a_b_relationship.name = "[giving relationship A to B a new name]"
    graph_existing.merge(existing_a_b_relationship)
    assert graph_existing.get_properties(existing_a_b_relationship.key)["name"] == "[giving relationship A to B a new name]"

def test_delete_relationship(graph_existing, existing_a_b_relationship):
    rel_existed_before_delete = (existing_a_b_relationship.key in graph_existing)
    graph_existing.delete(existing_a_b_relationship.key)
    assert rel_existed_before_delete and (existing_a_b_relationship.key not in graph_existing)

def test_clear(graph_existing):
    size_before = graph_existing.size
    graph_existing.clear()
    assert size_before > 0 and graph_existing.size == 0
