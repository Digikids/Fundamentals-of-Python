
friends = {
    "Max" : ["Masculine", "Charming", "Not_Creative"],
    "Steve": ["Masculine", "Not_Charming", "Creative"],
    "Sheddy": ["Not_Masculine", "Charming", "Creative"], 
    "George": ["Masculine", "Charming", "Not_Creative"],
}

for key, values in friends.items():
    for value in values:
        if value == "Creative" and value == "Not_Charming":
            print("Conglatulations " + key + "! you can fuck Veronica")