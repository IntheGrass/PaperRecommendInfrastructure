"""
    模型训练
"""
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


######################预处理模块############################

"""
    >功能: 对语料库进行分词，并删除停用词，将每个文本转化为分词列表
    >参数:
        @documents: 文档集，每一项对应一段文本
    >return:
        @corpus: 分词后的语料库，即词向量的列表
"""


def participle(documents):
    corpus = []
    count = 0
    for text in documents:
        words = word_tokenize(text)
        # 获取删除停用词后的分词表
        filtered_words = [word for word in words if word not in stopwords.words('english')]
        corpus.append(filtered_words)
        count += 1
        if count % 100 == 0:
            print(f'current {count}/{len(documents)}')
    return corpus

