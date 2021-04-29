

def likes():
    likes = {
    "Alex" : ["Tall"],
    "Jacob" : ["Short"], 
    "Mark" : ["Tall"], 
    "Max" : ["Short"]
    }
    for key, values in likes.items():
        for value in values:
            if value == "Short":
                print(key) 



likes()