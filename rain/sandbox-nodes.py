import uuid

from dataclasses import dataclass


class Node(RainData): 
    # TO DO: auto-set type_key based on class name
    type_key: str = "Node"
    relationships: QuerySet = None



# =========================================================

g = LocalGraph()
g.register_type(Character)
g.register_type(Action)
g.register_type(Expression)
g.register_type(Relationship)

awn = Character("AWN")


awn = g.create_node("Character", "AWN")
cep = g.create_node("Character", "CEP")
loving = g.create_node("Action", "LOVING")
exp = g.create_node("Expression", "AWN_LOVING_CEP")
r = g.create_relationship("Relationship", "AWN_LOVING_CEP", "LOVING")

