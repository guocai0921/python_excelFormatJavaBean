import json

import xmltodict


def XTJ():
    # 打开指定目录 文件为gb2312编码  
    file_object = open('e:\\src\\xml\\student.xml', encoding='gb2312')
    try:
        all_the_xmlStr = file_object.read()
    finally:
        file_object.close()
    # xml To dict   
    convertedDict = xmltodict.parse(all_the_xmlStr)
    # ensure_ascii 设置为False 中文可以转换  
    jsonStr = json.dumps(convertedDict, ensure_ascii=False)
    # 写入文件 写入为utf-8编码  
    with open('E:\\src\\json\\test.json', 'w', encoding='utf-8')as f:
        # 除去xmltodict 转换时默认添加的'@' 符号  
        f.write(jsonStr.replace('@', ''))


if __name__ == '__main__':
    XTJ()
