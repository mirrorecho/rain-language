import rain

# yo = rain.Node.create("YO", "I am Yo")
yo = rain.Node.from_json('{"key": "YO", "name": "I am Yo"}').create_me()

# mama = rain.Node.create("MAMA", "I am Mama")
mama = rain.Node.from_json('{"key": "MAMA", "name": "I am Mama"}').create_me()

# yo_mama = rain.Relationship.create(source=yo, target=mama)
# yo_mama = rain.Relationship.from_keys(source_key="YO", target_key="MAMA").create_me()
yo_mama = rain.Relationship.from_json('{"name": "", "source_key": "YO", "target_key": "MAMA"}').create_me()

print(yo)
print(mama)
print(yo_mama)
print("---------------------------------------------------")
print(yo.to_json())
print(mama.to_json())
print(yo_mama.to_json())

