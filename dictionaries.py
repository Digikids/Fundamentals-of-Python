thisdict = {
	"brand" : "ford", 
    "electric" : False, 
	"model" : "Mustang", 
	"year" : 1969, 
    "colors" : ["red", "white", "black"]
}
print(thisdict)

print(thisdict["year"])

print(len(thisdict))

for key, values in thisdict.items():
    for value in values:
        if value == 1969:
            print(key)