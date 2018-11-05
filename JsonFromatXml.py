import xmltodict


# json转xml函数
def jsontoxml(jsonstr):
    # xmltodict库的unparse()json转xml
    xmlstr = xmltodict.unparse(jsonstr)
    print(xmlstr)


if __name__ == "__main__":
    json = {'student': {'course': {'name': 'math', 'score': '90'},
                        'info': {'sex': 'male', 'name': 'name'}, 'stid': '10213'}}
    jsontoxml(json)
