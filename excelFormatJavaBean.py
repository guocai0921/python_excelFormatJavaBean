from jinja2 import Template
import math
import xlrd


def convert(one_string, space_character):  # one_string:输入的字符串；space_character:字符串的间隔符，以其做为分隔标志

    string_list = str(one_string).split(space_character)  # 将字符串转化为list
    first = string_list[0].lower()
    others = string_list[1:]

    others_capital = [word.capitalize() for word in others]  # str.capitalize():将字符串的首字母转化为大写

    others_capital[0:0] = [first]

    hump_string = ''.join(others_capital)  # 将list组合成为字符串，中间无连接符。

    return hump_string


def formatToStr(str):  # 首字母大写

    result = ''
    for i in range(len(str)):
        if i == 0:
            result += str[0].upper()
        else:
            result += str[i]
    return result


try:
    data = xlrd.open_workbook('E:\\formatExcel\\excel\\example-java-templates.xlsx')
except:
    print("fail to open file")
else:
    # 读取第一个sheet
    table = data.sheets()[0]
    # 获取行数
    n = table.nrows
    name = table.name
    contents = []
    for i in range(n):
        data = {}
        # 取第i行第0列的值
        code = table.cell(i, 0).value
        content = table.cell(i, 1).value
        types = table.cell(i, 2).value
        lengths = table.cell(i, 3).value
        data["name"] = code
        data["content"] = content
        code = convert(code, '_')
        data["code"] = code
        data["uname"] = formatToStr(code)
        if types == 'C':
            data["types"] = 'VARCHAR2'
            data["lengths"] = int(math.floor(lengths))
            data["mold"] = 'String'
        elif types == 'N':
            data["types"] = 'NUMBER'
            if isinstance(lengths, float):
                if lengths == int(lengths):  # checking for the integer:
                    data["lengths"] = int(lengths)  # solving your problem and printing the integer
                else:
                    data["lengths"] = lengths
                data["mold"] = 'Integer'
            else:
                data["lengths"] = lengths
                data["mold"] = 'Double'
        contents.append(data)
    print(contents)
    # with open("E:\\formatExcel\\template\\template.json.j4", "r", encoding='UTF-8') as fd:
    # with open("E:\\formatExcel\\template\\template.json.j3", "r", encoding='UTF-8') as fd:
    with open("E:\\formatExcel\\template\\template.json.j2", "r", encoding='UTF-8') as fd:
        template = Template(fd.read())
    config_content = template.render(contents=contents, name=name)

    # with open("E:\\formatExcel\\productFiles\\" + name + ".sql", "w") as fd:
    # with open("E:\\formatExcel\\productFiles\\" + name + ".txt", "w") as fd:
    with open("E:\\formatExcel\\productFiles\\" + name + ".java", "w") as fd:
        fd.write(config_content)
