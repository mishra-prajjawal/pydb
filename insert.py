import json
with open("test_table.json","r+") as src:
    a = json.load(src)
    for i in a.keys():
        valcount = None # count the number of values in the field
        if i == "field2":
            if a[i] == {}:
                print("empty")
                valcount= 1
                a[i][valcount] = "value3"
                break
            else:
                for n in a[i]:
                    a[i]["1"] = "value13"
                    break
                break
    src.seek(0)
    json.dump(a,src,indent=4)

#@  path = "test_table.json"
# command  
