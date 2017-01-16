import PST
from Util import Properties

μ_min = 0.5
lambda_min = 0.6  # 计算异常度阈值


def find_node(node_name, tree):
    node = tree.root
    count = 1
    for index in range(len(node_name)):
        tag = node_name[-count:]
        count += 1
        if tag in node.children:
            node = node.children[tag]
        else:
            node = None
            break
    return node


def detection_sequence(sequence, pst_tree):
    N = len(sequence)
    count_intrusion = 0
    for index in range(len(sequence)):
        current_tag = list(sequence)[index]
        if index == 0:
            pre_str = ""
        else:
            pre_str = sequence[:index]

        if not pre_str:
            node = pst_tree.root
        else:
            node = find_node(pre_str, pst_tree)

        if node:
            pro = node.probability_vector[current_tag]
        else:
            pro = 0
        if pro < μ_min:  # 超过阈值，判断为非法序列
            count_intrusion += 1
    if (count_intrusion / N) > lambda_min:
        print("该序列:%s异常！" % sequence, "异常度:", count_intrusion / N)
    else:
        print("该序列:%s正常。" % sequence, "异常度:", count_intrusion / N)


if __name__ == '__main__':
    txt = 'pst_data.txt'
    pkl = 'pst_result.pkl'
    tree = PST.gen_tree(txt)
    PST.draw_pst(tree)
    sequence_list = ["abrabr", "abcabc"]
    print('----------------------------------计算异常度-------------------------------')
    for sequence in sequence_list:
        detection_sequence(sequence, tree)
    ope_code_dict = Properties("opecode_mapper.properties").getProperties()
