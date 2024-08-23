#dictionary_in python : are used to store data in key-value pairs
#  ther are unordered,mutable(changable)& dont allow  duplicate keys
info={
 "manraj":7.9,
 "vikash" : 7.4,
 "op":6.1  , 
 "lavlesh":6.3,
 "sourabha":6.5,
 "sameer":6.8,
 }
info["manraj"]=8
print (info)
print(info["manraj"])
data={

}
data["name"]="Manraj kewat"
data["subjects"]={    #nested dictionary

    "physics":90,
    "chemistry":91,
    "hindi":92,
    "englishing":93,
}
print (data)
print(data["subjects"]["physics"])

print(data.keys())
print(data.values())
print(data.keys())
print(data.items())


print(data.get("name"))
# print(data("name"))#error


data.update({"my ns":45})


print (data)



#set's in python: collection of unordered items 
# each element must be unique & immutable


collection = { 1,2,3,4,5,6,7,8,9,"physics","hindi",1,2}
print (collection)
print(type(collection))
print(len(collection))

#methods of set

collection.add("mnrj")

# Create an empty set
my_set = set()

# Add elements to the set
my_set.add(1)
my_set.add(2)
my_set.add(3)
print(my_set)  # Output: {1, 2, 3}

# Remove an element from the set
my_set.remove(2)
print(my_set)

my_set.add((3,6,9)) # Output: {1, 3}



#print(my_set)  # Output: set()
my_set.pop()
print(my_set)

#union 
set1={1,2,3,4}
set2={6,7,3,4}

print(set1.union(set2))
print(set2.union(set1))
print(set1.intersection(set2))



