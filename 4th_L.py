#lists in python

marks=[ 90,87,98,79,60,50,94,95,95]

print(marks)
print(type(marks))
print(marks[6])
print(len(marks))

student=["lavlesh",87,"satna"]  #it cn store defferent type of elements(int,float,string etc)

print(student[2])

#slicing
marks=[ 90,87,98,79,60,50,94,95,95]

print(marks[2:5]) #from 2 to 4

#list method
list=[ 90,87,98,79,60,50,94,95,95]

print(list.append(5))
print(list.sort())
print(list.sort(reverse=True))
print(list.reverse()) #reverse
print(list.insert(4,99.99))
list.remove(95)
list.pop(6) #

list.sort()
print(list)

#tuples : a built-in data type that lets us create immuable sequencesof values

tuple = (1,2,3,4)
print(type(tuple))
print(tuple[1:3])

print(tuple.index(4))
print(tuple.count(3))
 
 







