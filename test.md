Welcome to the my-probabilistic-suffix-trees wiki!

**概率后缀树(PST)**

1. 相关概念理解
    * Trie和后缀树 [链接](http://blog.csdn.net/u013668392/article/details/40451677)
    * Markov Model/Hidden Markov Model [百度百科](http://baike.baidu.com/link?url=VyR86N6UiuDFZdrESMqxMXTo0TV4nZ0mvhoKPmJV2G32--WEXX5KJvacGMfxYtg8EuBgU1IcbH-oCwo0oayLMq)
    * [知乎](https://www.zhihu.com/question/20962240)
    * [Markov Modeling for Reliability Part 2:  Markov Model Fundamentals](http://www.mathpages.com/home/kmath232/part2/part2.htm)


2. PST论文
    * [一种事件序列的加权变阶马尔可夫模型](http://xueshu.baidu.com/s?wd=paperuri:(efe0e6910066df9aaefafa558f32e14c)&filter=sc_long_sign&sc_ks_para=q%3D%E4%B8%80%E7%A7%8D%E4%BA%8B%E4%BB%B6%E5%BA%8F%E5%88%97%E7%9A%84%E5%8A%A0%E6%9D%83%E5%8F%98%E9%98%B6%E9%A9%AC%E5%B0%94%E5%8F%AF%E5%A4%AB%E6%A8%A1%E5%9E%8B&tn=SE_baiduxueshu_c1gjeupa&ie=utf-8&sc_us=2857700676021100435)
    * [概率后缀树在入侵检测中的应用研究](http://xueshu.baidu.com/s?wd=paperuri:(d72edc031648bf9d4ab2e22b175aacdf)&filter=sc_long_sign&sc_ks_para=q%3D%E6%A6%82%E7%8E%87%E5%90%8E%E7%BC%80%E6%A0%91%E5%9C%A8%E5%85%A5%E4%BE%B5%E6%A3%80%E6%B5%8B%E4%B8%AD%E7%9A%84%E5%BA%94%E7%94%A8%E7%A0%94%E7%A9%B6&tn=SE_baiduxueshu_c1gjeupa&ie=utf-8&sc_us=14778630769861013596)
    * [Probabilistic suffix models forAPI sequence analysis of Windows XP applications](http://xueshu.baidu.com/s?wd=paperuri:(bd8a30372a02c6685ef57ecbfae3571a)&filter=sc_long_sign&sc_ks_para=q%3DProbabilistic+suffix+models+for+API+sequence+analysis+of+Windows+XP+applications&tn=SE_baiduxueshu_c1gjeupa&ie=utf-8&sc_us=14435997797425647571)

3. 算法实现

   示例序列 S=abracadabra 构造算法为Build_PST(P_min,gamma,alpha,L)

   1.  语言描述

       a. 初始化根节点(root)，根节点的概率向量值为每个符号在符号序列中出现的概率，所有概率大于
       P_min的符号作为候选子节点

       b.
