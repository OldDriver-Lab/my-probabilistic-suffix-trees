import pickle

'''构建基础后缀树
'''


class TreeNode(object):
    def __init__(self):
        self.count = 1  # 统计此结点代表的字符串出现的次数
        self.name = 'root'  # 标记node的名称
        self.children = {}
        self.totalchild = 0  # 统计node子节点个数
        self.probability = {}


class Tree(object):
    def __init__(self):
        self.root = TreeNode()

    def add(self, sequence):
        print("------------------ ", sequence, " ------------------")
        node = self.root
        node.totalchild += 1
        for c in sequence:
            print(c)
            print("node.name:", node.name)
            if c not in node.children:
                child = TreeNode()
                node.children[c] = child
                node = child
                node.totalchild += 1
                node.name = c + str(node.count)
            else:
                node = node.children[c]
                node.totalchild += 1
                node.count = node.count + 1
                print("node.count:", node.count)

    def count_seq(self, sequence):
        '''计算序列出现的次数'''
        node = self.root
        for c in sequence:
            if c not in node.children:
                return 0
            else:
                node = node.children[c]
        return node.count


def gen_tree(input_file, output_file):
    '''生成Tree'''
    tree = Tree()
    with open(input_file) as f:
        for line in f:
            # 增加'$'用来区别是否是完整后缀
            # line = line.strip() + '$'
            line = line.strip()
            for i in range(len(line)):
                l = line[i:]
                tree.add(l)

    # 生成Node概率
    with open(input_file) as f:
        source_list = []
        for line in f:  # 获取去重的序列并保持原顺序
            source_list += list(line)
        str_list = list(set(source_list))
        str_list.sort(key=source_list.index)
        if '\n' in str_list:
            str_list.remove()
        print(str_list)

    node = tree.root
    print('root count-----:', node.totalchild)
    for c in str_list:
        print(c)
        if c not in node.children:
            node.probability[c] = 0
        else:
            # todo :增加概率计算
            pass

    print(node.children.keys())
    # 此处已经计算出单个Node的数据量(即分支量,概率计算的被除数)
    print(node.children['A'].children['N'].totalchild)
    # with open(output_file, 'wb') as f:
    # pickle.dump(tree, f)

    return tree


if __name__ == '__main__':
    txt = 'pst_data.txt'
    pkl = 'pst_result.pkl'
    tree = gen_tree(txt, pkl)
    # print(tree.count_seq('ANA'))

    # pkl_file = open(pkl, 'rb')
    # result_tree = pickle.load(pkl_file)
    # print(result_tree)
