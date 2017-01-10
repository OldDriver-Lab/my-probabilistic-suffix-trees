# encoding:utf-8
import re

'''构建概率后缀树
'''


class TreeNode(object):
    def __init__(self):
        self.count = 1  # 统计此结点代表的字符串出现的次数
        self.name = 'root'  # 标记node的名称
        self.children = {}
        self.totalchild = 0  # 统计node子节点个数
        self.probability_vector = {}  # 概率向量


class Tree(object):
    def __init__(self):
        self.root = TreeNode()
        self.P_min = 0.00  # 入树概率阈值
        self.gamma = 0.01  # 节点转移概率阈值
        self.alpha = 0.01  # 另一个阈值 在判断候选节点时起作用
        self.L = 5  # 树最大深度

    def build(self, sequence):
        print("------------------ line:", sequence, " ------------------")
        node = self.root
        node.totalchild += 1
        seq_list = list(sequence)
        dis_seq_list = list(set(seq_list))
        dis_seq_list.sort(key=list(sequence).index)
        # 此时获取到去重后的字符数组，c为单个字符
        for c in dis_seq_list:
            # 第一步验证候选节点，如果频率超过P_min，则作为候选节点
            if compute_pro(c, seq_list) > self.P_min:
                print(compute_pro(c, seq_list))


def compute_pro(s, list):
    return float(list.count(s)) / float(len(list))


def get_suffix(seq, length, str):
    '''返回在str中，长度为1，起始字符为seq的字符串'''
    for i in range(length - 1):
        seq = seq + '.'
    print(seq)
    result = re.findall(seq, str)
    result = map(lambda x: x[-1], result)
    return list(result)


def gen_tree(input_file, output_file):
    '''生成PST'''
    tree = Tree()
    with open(input_file) as f:
        for line in f:
            # 增加'$'用来区别是否是完整后缀  todo:PST是否需要？
            # line = line.strip() + '$'
            line = line.strip()
            tree.build(line)

    return tree


if __name__ == '__main__':
    txt = 'pst_data.txt'
    pkl = 'pst_result.pkl'
    tree = gen_tree(txt, pkl)

    # print(tree.count_seq('ANA'))

    # pkl_file = open(pkl, 'rb')
    # result_tree = pickle.load(pkl_file)
    # print(result_tree)
