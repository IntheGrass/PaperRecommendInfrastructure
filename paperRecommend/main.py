from dataReader import localReader as data
import preprocess
import numpy as np
from gensim.models import LdaModel
from gensim import corpora
import pickle
'''
    >描述: 一般的随机游走，直接使用一个矩阵计算排名
    >参数：
        @matrix: 关系矩阵，类型为numpy里的ndarray
        @query: 查询向量
        @a: 重启概率
        @max_iteration: 最大的迭代次数
    >返回值：
        @scores: 评分的行向量(列向量转化为行向量)
'''


def general_RWR(matrix, query, a=0, max_iteration=1000, is_print=False):
    if len(query) != len(matrix):
        print('error: 查询向量与关系矩阵长度不匹配!')
        return
    scores = np.ones((len(query), 1)) / len(query)  # 初始化评分向量
    square_sum = 0  # 两次迭代的评分向量差的平方和
    for i in range(0, max_iteration):
        scores_new = (1 - a) * matrix.dot(scores) + a * q  # 重启随机游走的核心公式
        # 计算新旧评分差的平方和
        diff = scores_new - scores
        square_sum_new = np.sum(diff * diff)
        if is_print and i % 50 == 0:
            print("第", i, "次迭代==> ", "两向量之差的平方和：", square_sum_new)
        if square_sum_new == 0 or square_sum == square_sum_new:
            print("成功收敛, ", "迭代次数为：", i)
            break
        scores = scores_new
    return scores[:, 0]  # 转为行向量


if __name__ == "__main__":
    PP = preprocess.selfRelationToMatrix(data.train_paper_citation_list, data.train_paper_dict)  # 获取
    AA = preprocess.selfRelationToMatrix(data.author_collaboration_list, data.authors_dict, symmetric=True)
    PA, AP = preprocess.paper_connect_author(data.papers_meta_dict, data.train_paper_list, data.authors_list)
    test_citation_dict = preprocess.get_test_citation_dict(data.test_paper_citation_list)
    # 读取主题模型
    topic_model = LdaModel.load('../../test/abstract_lad_model.data')
    with open('../../test/abstract_corpus.data') as f:
        abstract_corpus = pickle.load('../../test/abstract_corpus.data')
    word_dictionary = corpora.Dictionary.load('../../test/abstract_dictionary.data')
    abstract_bow_corpus = [word_dictionary.doc2bow(text) for text in abstract_corpus]

