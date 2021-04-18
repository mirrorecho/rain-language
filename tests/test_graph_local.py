import pytest
import rain


@pytest.fixture
def new_a_node():
    return rain.Node("NEW_A_NODE", name="New A node")

@pytest.fixture
def new_b_node():
    return rain.Node("NEW_B_NODE", name="New B node")

@pytest.fixture
def existing_a_node():
    return rain.Node("EXISTING_A_NODE", name="Existing A node")

@pytest.fixture
def existing_b_node():
    return rain.Node("EXISTING_B_NODE", name="Existing B node")

@pytest.fixture
def existing_a_b_relationship():
    return rain.Node("EXISTING_A_TO_B", name="Existing relate A to B")

@pytest.fixture
def new_b_a_relationship():
    a = rain.Node("EXISTING_A_NODE", name="Existing A node")
    b = rain.Node("EXISTING_B_NODE", name="Existing B node")
    return rain.Relationship("NEW_B_TO_A", name="New relate B to A", source=b, target=a)

@pytest.fixture
def graph_empty():
    return rain.GraphLocal()

@pytest.fixture
def graph_existing():
    """Creates a LocalGraph instance with two nodes and a relationship between them"""
    graph = rain.GraphLocal()
    a = rain.Node("EXISTING_A_NODE", name="Existing A node")
    b = rain.Node("EXISTING_B_NODE", name="Existing B node")
    graph.create(a)
    graph.create(b)
    relationship = rain.Relationship("EXISTING_A_TO_B", name="Existing relate A to B", source=a, target=b)
    graph.create(relationship)
    return graph

def test_settings():
    assert isinstance(rain.DEFAULT_GRAPH, rain.GraphInterface)

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
