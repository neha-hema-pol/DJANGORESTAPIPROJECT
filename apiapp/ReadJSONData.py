import json

myjsonfile = open('apiapp\JSON_Data\JSON_Data_1.json', 'r')
jsondata = myjsonfile.read()


obj = json.loads(jsondata)

#print(str(obj['comments']))
#print(str(obj['total']))
#print(str(obj['skip']))
#print(str(obj['limit']))

list = obj['comments']

#print(list)
#print(len(list))


#for i in range(len(list)):
    #print("..........................")
    #print("Address of",i,"is :")
    #print("..........................")
    #print("Id:",list[i].get("id"))
    #print("body:",list[i].get("body"))
    #print("postId:",list[i].get("postId"))
    #print("user:",list[i].get("user"))
    #print()



