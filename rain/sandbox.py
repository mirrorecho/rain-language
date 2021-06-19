from dataclasses import dataclass
from typing import Callable, Iterable
# import inspect
import rain
from itertools import cycle, repeat


print("============================================================")

# c1 = rain.NotatedMusicCell("C1")

# mp = rain.Palette(*rain.Machine.select())

# c1.render()


# @dataclass
# class TP(rain.Node):
#     pitch:Iterable=()
#     dur:Iterable=()
#     instrument:Iterable=()

#     def __iter__(self):
#         # for n,v in self.get_properties():
#         # yield from self.get_properties().items()
        
#         keys, values = zip(*(
#             (k, getattr(self, k))
#             for k in self._properties_keys if k!= "name"
#             ))
#         for zipped_values in zip(*values):
#             yield {k:v for k, v in zip(keys, zipped_values)}

#     def iter_func(self, func:Callable):
        
#         keys, values = zip(*(
#             (k, getattr(self, k))
#             for k in self._properties_keys if k!= "name"
#             ))
        
#         return map(
#             lambda zipped_values:func(**{k:v for k, v in zip(keys, zipped_values)}), 
#             zip(*values))

#         # for {k:getattr(self,k) for k in self.__dataclass_fields__.keys() if k not in self._properties_exclude_fields}:
#         #     yield my_properties[key]
#         # yield from zip(self.get_properties())

#         # keys = prop.keys()
        
#         # for values in zip(*prop.values()):
#         #     yield {k:v for k, v in zip(keys, values)}

# tp = TP(
#     pitch=(0,2,5,4),
#     dur=cycle((2,1)),
#     instrument=cycle(("flute",))
# )

# def my_print(**kwargs):
#     print(kwargs)

# print(tp._properties_keys)

# for x in tp.iter_func(my_print):
#     pass

# # d = dict(
#     a=(1,2,3,4),
#     b=(10,20,30),
#     c=cycle((0,1))
# )

# def yo(prop):
#     keys = prop.keys()

#     for values in zip(*prop.values()):
#         yield {k:v for k, v in zip(keys, values)}

    # for i in prop.items():
    #     yield i

    # for v in zip(*prop.values()):
    #     yield {kv[0]:kv[1] for kv in zip(keys, v)}

    # yield from prop.values()
    # yield from zip(
    #     prop.keys(),
    #     *prop.values()
    # )

# HEY FOR LOOP IS NOT COOL HERE!
# for v in yo(d):
#     print(v)


print("============================================================")


# for z in zip(
#     (-3,-1,0), 
#     ("a","b","c"),
#     cycle(("YO","ha"))):
#     print(z)

# def get_thingy(**kwargs):
#     print("YO MAMA")
#     return (

#         )


# def ya_iter(thingy):
#     yield from zip(get_thingy(pitch=(-3,-1,0), 
#     name=("a","b","c"),
#     yo=cycle(("YO","ha")
#     ))

# th1 = 

# for ta in ya_iter(

# t1 = ("yo1", 
#     ("yo2", 
#         ("yo3", ())
#     )
# )

# def yo_iter(t) -> Iterable:
#     if my_child := t:
#         yield my_child[0]
#         while my_child := my_child[1]:
#             yield my_child[0]

# yi = yo_iter(t1)
# for y in yi:
#     print(y)

# awn = rain.Node.create(name="Awn Fancy", key="AWN")
# cep = rain.Node.create(name="Fancy", key="CEP")
# kir = rain.Node.create(name="Fancy", key="KIR")

# awn_to_cep = rain.Relationship.create(source=awn, target=cep, key="AWN_TO_CEP")

# for d in rain.DEFAULT_GRAPH.select("Node", "AWN", "CEP", name="Fancy"):
#     print(d.key)


# print(awn.graph._data)
# # awn.save_me()


# print(awn)
# print(awn.labels)




# l = rain.Language(name="Mama", key="YO")
# l.set_properties(name="fatty")
# print(l.name)

# import uuid
# import time
# from collections import OrderedDict

# x = 1000000

# tic = time.perf_counter()
# l = [uuid.uuid4().hex for i in range(x)]
# toc = time.perf_counter()
# print(f"Created list in {toc - tic:0.4f} seconds")

# tic = time.perf_counter()
# d = OrderedDict((uuid.uuid4().hex, i) for i in range(x))
# toc = time.perf_counter()
# print(f"Created dictionary in {toc - tic:0.4f} seconds")

# # =========================================================================

# tic = time.perf_counter()
# for i in range(x):
#     yo  = l[i]

# print("--------------------------------------------")
# toc = time.perf_counter()
# print(f"Accessed list in {toc - tic:0.4f} seconds")

# # =========================================================================


# tic = time.perf_counter()

# for i in range(x):
#     yo  = d.values()

# print("--------------------------------------------")
# toc = time.perf_counter()

# print(f"Accessed dict in {toc - tic:0.4f} seconds")
# # print(d)

# # d = {uuid.uuid4().hex:i for i in range(x)}




