"""
    一些常用的方法
"""
import numpy as np

"""
==矩阵的列归一化==
    >功能：
        将矩阵的每一列除以该列的和，是修改后的每一列和为1
    >参数：
        @M: 需要进行列归一化的矩阵
    >返回值：
        @M_normal: 列归一化后的矩阵
"""


def col_normalization(M):
    if len(M) <= 0:
        print("归一化数组长度为0，请检查")
        return M
    M_normal = np.zeros(M.shape)
    n_row = len(M[0])
    for i in range(0, n_row):
        col_sum = M[:, i].sum()
        if col_sum == 0:
            continue
        M_normal[:, i] = M[:, i] / col_sum
    return M_normal


'''
    >功能：
        生成查询向量，即重启随机游走的起点向量
    >参数:
        @query_author: 查询作者
        @query_paper: 查询论文
        @id_dict: 论文ID对应的数字序号字典
    >返回值：
        @q: q*1的列向量，查询论文对应的位置为1，其他为0
'''


def generate_query_vector(query_author, query_paper, paper_dict, author_dict):
    q_author = np.zeros((len(author_dict), 1))
    q_paper = np.zeros((len(paper_dict), 1))
    for author in query_author:
        try:
            order = author_dict[author.lower()]
        except:
            continue
        else:
            q_author[order][0] = 1
    for paper in query_paper:
        order = paper_dict[paper]
        q_paper[order][0] = 1
    return np.vstack((q_author, q_paper))


'''
    >功能:
        给定列表，获得列表中降序排序后得分排在前N位得值的索引
    >参数：
        @scores: 评分列表
        @N: 排名前N位
    >返回值：
        @n_index: 得分排名前n位的索引集合，按照得分的降序排列
'''


def top_n_index(scores, N):
    n_index = scores.argsort()
    return n_index[:-(N + 1):-1]
