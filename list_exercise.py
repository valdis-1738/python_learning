mylist = ["apple","banana","cherry","orange","lime","melon"]

print(mylist)

print(mylist[-2])

print(mylist[2:5])

print(mylist[:4])

print(mylist[4:])

print(mylist[-4:-1])



# print(len(mylist))

# mylist[0] = "kiwi"
# print(mylist)

# mylist.append("lemon")
# print(mylist)

# mylist.remove("banana")
# print(mylist)

# print(type(mylist))


thislist = ["apple","banana","orange"]
tropical = ["mango","pineapple","papaya"]
thislist.extend(tropical)
print(thislist)


if "apple" in thislist:
    print("yes,it is in the list")