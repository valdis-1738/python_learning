# mark = int(input("what is the marks?\n"))
# print(mark)
# if mark > 80 :
#     print("ready")
# else :
#     print("not ready")

day = int(input("what day is today?\n"))
print(day)
match day :
    case 1: 
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("thursday")
    case 5:
        print("friday")
    case 6:
        print("saturday")
    case 7:
        print("sunday")
