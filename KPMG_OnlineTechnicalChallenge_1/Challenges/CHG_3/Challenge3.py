def get_nested_value(intobj,keys:str):
    if type(intobj) is not dict and type(keys) is not str:
        return None
    else:
        keys=keys.split("/")
        for key in keys:
                intobj=intobj[key]
        return intobj


obj={"a":{"b":{"c":{"d":"e"}}}}
print(get_nested_value(obj,"a/b/c/d"))