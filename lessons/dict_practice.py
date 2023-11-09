"""Practice with dicitonaries."""
# Constructing a dictionary

ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
print("Made my dictionary.")
print(ice_cream)

# Adding a key, value pair to a dicitonary
ice_cream["mint"] = 3
print("After adding mint.")
print(ice_cream)

# Removing a key, value pair form a dictionary
ice_cream.pop("mint")
print("after removing mint")
print(ice_cream)

print(ice_cream["chocolate"])
ice_cream["vanilla"] = 10