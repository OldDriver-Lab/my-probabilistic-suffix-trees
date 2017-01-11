import pickle

'''构建概率后缀树
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
        self.P_min = 0.00  # 入树概率阈值
        self.gamma = 0.01  # 节点转移概率阈值
        self.alpha = 0.01  # 另一个阈值 在判断候选节点时起作用
        self.L = 5  # 树最大深度
        self.current_deepth = 0  # 当前树深度

    def add(self, sequence):
        print("------------------ ", sequence, " ------------------")

        def build_pst(node, sequence):
            print("***************************************************************************")
            seq_list = list(sequence)
            dis_seq_list = list(set(seq_list))
            dis_seq_list.sort(key=list(sequence).index)
            dis_seq_list.remove('$')
            print('获取到有序去重字符集:', dis_seq_list)
            node = self.root
            node.totalchild += 1
            for c in dis_seq_list:
                if compute_pro(c, sequence) > self.P_min and self.current_deepth < self.L:  # 如果c的概率大于最小概率
                    print(c, "允许入树")
                    child = TreeNode()
                    node.children[c] = child
                    node = child
                    self.current_deepth += 1
                    build_pst(node, sequence)

        root_node = self.root
        build_pst(root_node, sequence)


def compute_pro(s, total_sequence):
    '''计算s在total_sequence_list中出现的概率'''
    return float(total_sequence.count(s)) / float(len(total_sequence.replace('$', '')))


def gen_tree(input_file):
    '''生成Tree'''
    tree = Tree()
    with open(input_file) as f:
        total_sequence = ''
        for line in f:
            # 增加'$'用来区别是否是完整后缀  todo:PST是否需要？
            line = line.strip() + '$'
            total_sequence += line
        tree.add(total_sequence)
    return tree


if __name__ == '__main__':
    txt = 'pst_data.txt'
    tree = gen_tree(txt)
    # print(tree.count_seq('ANA'))

    # pkl_file = open(pkl, 'rb')
    # result_tree = pickle.load(pkl_file)
    # print(result_tree)
