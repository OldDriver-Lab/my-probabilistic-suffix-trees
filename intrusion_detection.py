import PST

μ_min = 0.5
lambda_min = 0.5  # 计算异常度阈值


def detection_sequence(sequence, pst_tree):
    print(sequence, pst_tree)
    for single_tag in list(sequence):
        print(single_tag)


if __name__ == '__main__':
    txt = 'pst_data.txt'
    pkl = 'pst_result.pkl'
    tree = PST.gen_tree(txt)
    PST.draw_pst(tree)
    sequence = "tactat"
    print('----------------------------------计算异常度-------------------------------')
    detection_sequence(sequence, tree)
