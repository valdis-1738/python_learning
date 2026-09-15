myCarinfo = {
    "name":"Mercedes",
    "model":2026,
    "type": "S-class",
    "release": True

}

myCarinfo["model"] = 2019
myCarinfo["color"] = "red"
myCarinfo.pop("type")

print(myCarinfo)

myCarname = myCarinfo["name"]
print(myCarname)


classinfo = {
    "discription" : "Learn industry-level",
    "icon_code" : "developer_program",
    "id" : 1,
    "name" : "Profesional Software Developer Program",
    "popular" : False,
    "recommended_age" : "16-45 Years"
}

classinfo.pop("id")

print(classinfo)

classdiscription = classinfo["discription"]
print(classdiscription)

classicon_code = classinfo.get("icon_code")
print(classicon_code)


