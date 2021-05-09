import inspect
import rain

print("============================================================")

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




