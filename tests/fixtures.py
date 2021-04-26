import pytest
import rain

def setup_empty_context():
    # often call rain.context.init_empty_graph() to create a new empty graph 
    # with no data before making any changes to the default graph in tests
    # (to avoid data in the graph from previous tests interfering)
    rain.context.init_empty_graph()


@pytest.fixture(scope="session")
def default_context():
    """
    Use as a fixture on ALMOST EVERYTHING to ensure that at we're always 
    starting with an empty graph (as opposed to the real graph with data)
    """
    setup_empty_context()


@pytest.fixture
def graph_empty():
    setup_empty_context()
    return rain.context.graph


@pytest.fixture
def new_a_node(default_context):
    return rain.Node("NEW_A_NODE", name="New A node")


@pytest.fixture
def new_b_node(default_context):
    return rain.Node("NEW_B_NODE", name="New B node")


@pytest.fixture
def existing_a_node(default_context):
    return rain.Node("EXISTING_A_NODE", name="Existing A node")


@pytest.fixture
def existing_b_node(default_context):
    return rain.Node("EXISTING_B_NODE", name="Existing B node")

# TO CONSIDER... maybe create separate fixtures (or just create data in the tests)
# to cut the fat from this ...
@pytest.fixture
def graph_existing(default_context):
    """Creates a LocalGraph instance with two nodes and a relationship between them"""
    setup_empty_context()
    graph = rain.context.graph
    a = rain.Node("EXISTING_A_NODE", name="Existing A node")
    b = rain.Node("EXISTING_B_NODE", name="Existing B node")
    c = rain.Node("EXISTING_C_NODE", name="C-D shares name")
    d = rain.Node("EXISTING_D_NODE", name="C-D shares name")
    graph.create(a)
    graph.create(b)
    graph.create(c)
    graph.create(d)
    relationship = rain.Relationship("EXISTING_A_TO_B", name="Existing relate A to B", source=a, target=b)
    graph.create(relationship)
    return rain.context.graph


@pytest.fixture
def new_b_a_relationship(default_context, existing_a_node, existing_b_node):
    return rain.Relationship("NEW_B_TO_A", 
        name="New relate B to A", 
        source=existing_b_node, 
        target=existing_a_node
        )


@pytest.fixture
def existing_a_b_relationship(default_context):
    return rain.Relationship("EXISTING_A_TO_B", name="Existing relate A to B")


@pytest.fixture
def created_node():
    setup_empty_context()
    return rain.Node.create("CREATED_NODE")

