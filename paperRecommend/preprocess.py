"""
    数据的预处理库，主要是将列表、字典等数据转为矩阵
"""
import numpy as np

"""
    >功能: 将同类关系(即行和列对应同一类实体)转为矩阵形式，如论文引用，作者协助网络
    >参数:
        @relation_list: 关系列表，每一项应为一个元组（a,b）表示a和b之间的关系
        @name_dict: 表示元组中每个名字所在的序号位置，如{a:0,b:1}表示a，b在矩阵的位置分别为0，1
        @symmetric: 表示关系是否是双向的，即输出对称矩阵
    >返回值:
        @relation_matrix:  关系矩阵
"""


def selfRelationToMatrix(relation_list, name_dict, symmetric=False):
    n = len(name_dict)
    relation_matrix = np.zeros((n, n))
    for relation in relation_list:
        first_name = relation[0]  # 表示引用者
        second_name = relation[1]  # 表示被引用者
        if first_name in name_dict.keys() and second_name in name_dict.keys():
            first_order = name_dict[first_name]
            second_order = name_dict[second_name]
            relation_matrix[second_order][first_order] = 1
            if symmetric:
                relation_matrix[first_order][second_order] = 1
    return relation_matrix


"""
    >功能: 将不同类关系(即行和列对应不同实体)转为矩阵形式，如论文-作者
    >参数:
        @relation_list: 关系列表，每一项应为一个元组（a,b）表示a和b之间的关系
        @row_dict: 表示元组中关系第一个名字所在的序号位置，如{a:0,b:1}表示a，b在矩阵的位置分别为0，1
        @column_dict: 表示元组中关系第二个名字所在的序号位置
    >返回值:
        @relation_matrix:  关系矩阵
"""


def diffRelationToMatrix(relation_list, row_dict, column_dict):
    row = len(row_dict)
    column = len(column_dict)
    relation_matrix = np.zeros((row, column))
    for relation in relation_list:
        first_name = relation[0]  # 表示引用者
        second_name = relation[1]  # 表示被引用者
        if first_name in row_dict.keys() and second_name in column_dict.keys():
            row_order = row_dict[first_name]
            column_order = column_dict[second_name]
            relation_matrix[row_order][column_order] = 1
    return relation_matrix


"""
    >功能：
        根据论文元信息，连接作者和论文的关系，生成作者和论文的关系矩阵
    >参数：
        @paper_meta: 论文元数据的字典
        @paper_list: 论文列表
        @author_lsit: 作者列表
    >返回值：
        @PA: paper-author矩阵
        @PA.T: author-paper矩阵 (因为作者和论文的关系是对称的，所以直接取转置        
"""


def paper_connect_author(paper_meta, paper_list, author_list):
    paper_num = len(paper_list);
    author_num = len(author_list);
    PA = np.zeros((paper_num, author_num))  # paper-author矩阵
    for i in range(0, paper_num):
        paper_order = i  # paper对应的数字序号
        paper_id = paper_list[paper_order]
        if paper_id not in paper_meta.keys():
            print(paper_id, 'is not exist')
            continue
        meta_item = paper_meta[paper_id]
        author_text = meta_item["author_text"]
        authors = meta_item["author"]
        for i in range(0, author_num):
            author_order = i  # author对应的数字序号
            author = author_list[author_order]  # 作者名
            # 注意，这里多加一个判断条件是因为authors是通过'; '分割的，有些作者名自带'; '导致被分割
            # 因此如果作者名不在的话，需要在判断是不是子字符串来确定是否为其作者
            if author in authors or (author in author_text):
                PA[paper_order][author_order] = 1
    return PA, PA.T


'''
    >功能: 把测试引用关系转化为引用字典，每个键对应一篇论文，值对应引用论文数组
    >参数:
'''


def get_test_citation_dict(test_paper_citation_list):
    citation_dict = {}
    for citation in test_paper_citation_list:
        origin = citation[0]
        cited = citation[1]
        if origin not in citation_dict.keys():
            citation_dict[origin] = [cited]
        else:
            citation_dict[origin].append(cited)
    return citation_dict
