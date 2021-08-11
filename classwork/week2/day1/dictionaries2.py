superhero = {
    "name": "Wonder Woman",
    "alias": "Diana Prince",
    "club": "Science Club",
    "gear": [
        "Lasso of Truth",
        "Bracelets of Submission"
    ],
    "vehicle": {
        "title": "Invisible Jet",
        "speed": "2000 mph",
    }
}
# If superhero is not in a club (aka it does not exist), lets create the club key, and then assign a value
# print(superhero)

# Example 1 to check if values are in a dictionary
# if superhero.get("club") == None:
#     superhero["club"] = "Justice League"
# else:
#     print("Shes' in a club")

# Example 2
for key, value in superhero.items():
    # print(key, value)
    if value == "Science Club":
        value = "Justice League"
        # print(key, value)

#  Example 3
if "hobbies" not in superhero:
    superhero["hobbies"] = "Saving the world"
# print(superhero)

# Example 4
print(superhero.items())

wonderwoman = {
    "name": "Wonder Woman",
    "alias": "Diana Prince",
    "club": "Science Club",
    "gear": [
        "Lasso of Truth",
        "Bracelets of Submission"
    ],
    "vehicle": {
        "title": "Invisible Jet",
        "speed": "2000 mph",
    }
}
# Example 5
wonderwoman["vehicle"]["title"] = wonderwoman["vehicle"]["title"] + "racecar"
print(wonderwoman["vehicle"])
print(wonderwoman)


# We see how a dictionary is a more complex data type
# We see that we can access values inside of a dictionary if we refer to a key that is in the dictionary
# We see that dictionaries can contain many different data types.  A dictionary value can be either a [],(), "", {}, int, boolean, float, etc.
# We can access specific methods that are designed for dictionaries (such as .items)
# We can reassign or create keys inside of a dictionary by referring to the key such as
# superhero["club"] and then we can assign it a value
# We can use the keyword del to delete a key or value from a dictionary


schools = {
    "schoolList": [
        {"name": "Spring"}, {"name": "Kleien Cane"}, {"name": "Tomball"}
    ]
}
# print(schools)


def loopOverFunction(schoolList):
    for school in schoolList["schoolList"]:
        if school["name"] == "Klein Cane":
            print("We found %s" % school["name"])
        elif school["name"] == "Tomball":
            print("We found %s" % school["name"])
    return


# loopOverFunction(schools)