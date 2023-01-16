def obtainKey(obj:dict):
    keys=list(obj)
    if (len(keys)!=1):
        raise Exception('Either empty dictionary or Multiple Keys')
    else:
        return keys[0]

def getNestedValue(obj:dict,key:str,Found=False):
    if type(obj) is not dict and not Found:
        return None
    if (Found or (key in obj.keys())):
        if type(obj[key]) is dict:
            return getNestedValue(obj[key],obtainKey(obj[key]),True)
        else:
            return obj[obtainKey(obj)]
    else:
        nestedkey=obtainKey(obj)
        return getNestedValue(obj[nestedkey],key,False)

if __name__== '__main__':
    obj={"a":{"b":{"c":{"d":"e"}}}}
    value=getNestedValue(obj,'b')
    print(value)
    print(obtainKey(obj))






