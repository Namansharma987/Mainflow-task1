#LIST
thislist = ["apple","orange","cherry"]
#adding in a list
thislist.append("Banana")
#removing from the list
thislist.remove("apple")
#modifying in a list
thislist[0] = "Grapes"
print("updated list: ",thislist)


#SET
thisset = {"blue","black","red"}
#adding in a set
thisset.add("white")
#removing from the set
thisset.remove("blue")
#modifying from the set
thisset.discard("black")
thisset.add("grey")
print("updated set: ",thisset)


#Dictionary
thisdict = {
    "brand": "ford",
    "model": "Mustang",
    "year": 1928
}
#adding in a dictionary
thisdict["year"] = 2001
#removing from the dictionary
del thisdict["model"]
#modifying in a dictionary
thisdict["brand"] = "ford motor"
print("updated dictionary: ",thisdict)