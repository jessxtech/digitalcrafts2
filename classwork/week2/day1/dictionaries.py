listOfRestaurants = ["Dominos", "Little Caesars", "Papa Johns", "Pizza Hut", ]
# We access list contents  via index

restaurant = {
    "name": "Pizza Hut",
    "address": "Stables Town Center",
    "phone": "123-123-1232"
}

user1 = {
    "name": "Xavier",
    "height": "5-10",
}

user2 = {
    "name": "Brande",
    "height": "5-8"
}
# You access the values of a dictionary via a key
# print(user1["name"])
# print(user2.get("pet"))
# print(user1.get("pet", []))

# print(restaurant["name"])
# print(restaurant["height"])

joesFavoriteCars = {
    "carList": ["Bmw", "Audi", "Shelby Cobra", "Porsche"],
    "JoesBankBalance": {
        "CurrentBalance": "$0",
        "Dream Balance": "♾️",
        "joesStonks": {
            "TSLA": "5",
            "MSFT": 20
        }
    }
}

print(joesFavoriteCars.get("carList")[3])
print(joesFavoriteCars["carList"][0])
print(str(joesFavoriteCars["JoesBankBalance"]["joesStonks"]["MSFT"]))
# Print out ever car in the car list
for car in joesFavoriteCars["carList"]:
    print(car)
# print(joesFavoriteCars["carList"])