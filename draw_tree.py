from graphviz import Digraph

dot = Digraph(comment='The Round Table')

# 添加圆点 A, A的标签是 King Arthur
dot.node('A', 'root')
# dot.view()  # 后面这句就注释了，也可以使用这个命令查看效果

# 添加圆点 B, B的标签是 Sir Bedevere the Wise
dot.node('B', 'left1')
# dot.view()

# 添加圆点 L, L的标签是 Sir Lancelot the Brave
dot.node('L', 'right1')
# dot.view()

# 创建一堆边，即连接AB的边，连接AL的边。
#dot.edges(['AB', 'AL'])
dot.edge('A', 'B', constraint='true')
dot.edge('A', 'L', constraint='true')
# dot.view()

# 在创建两圆点之间创建一条边
# dot.edge('B', 'L', constraint='false')
# dot.view()

# 获取DOT source源码的字符串形式
# print(dot.source)
# doctest: +NORMALIZE_WHITESPACE
# The Round Table
# digraph {
#    A [label="King Arthur"]
#    B [label="Sir Bedevere the Wise"]
#    L [label="Sir Lancelot the Brave"]
#        A -> B
#        A -> L
#        B -> L [constraint=false]
# }

# 保存source到文件，并提供Graphviz引擎
dot.render('test-output/round-table.gv', view=True)
