# encoding:utf-8
'''
    从指定list中自动映射
'''
from random import choice

MAPPING_LIST = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def main():
    code_list = ['1', '2', '3', '4', '5', '6', '1', '3', '4', '5', '6']
    mapping_dict = dict()
    code_mapped_list = []
    for code in code_list:
        if code in mapping_dict:
            code_mapped = mapping_dict[code]
        else:
            code_mapped = choice(MAPPING_LIST)
            MAPPING_LIST.remove(code_mapped)
        mapping_dict[code] = code_mapped
        code_mapped_list.append(code_mapped)
    print(code_mapped_list)
    print(MAPPING_LIST)


if __name__ == '__main__':
    main()
