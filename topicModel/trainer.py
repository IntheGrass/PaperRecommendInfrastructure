"""
    模型训练
"""
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

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
    tokenizer = RegexpTokenizer(r'\w{2,}')
    count = 0
    for text in documents:
        words = tokenizer.tokenize(text)  # 分词，同时过滤掉标点符号与单个字符的词
        # 获取删除停用词后的分词表
        filtered_words = [word for word in words if word not in stopwords.words('english')]
        corpus.append(filtered_words)
        count += 1
        if count % 100 == 0:
            print(f'current {count}/{len(documents)}')
    return corpus


"""
    >介绍: 获得所有论文及其对应主题的词典,对应主题为主题id的列表，格式为paper_id: [topic_id1, topic_id2, .....]
    >参数:
        @paper_ids: 所有论文的id列表
        @paper_bow: 所有论文的词袋模型表示，对应的是
"""


def get_paper_topic_dict(paper_ids, paper_bow, topic_model):
    paper_topic_dict = {}
    for i in range(0, len(paper_bow)):
        paper_id = paper_ids[i]
        bow = paper_bow[i]
        topic_distribution = topic_model.get_document_topics(bow)
        topic_ids = [topic_id for topic_id, possibility in topic_distribution]
        paper_topic_dict[paper_id] = topic_ids
    return paper_topic_dict


"""
    （未完成）
    >介绍：根据模型获得主题与词的关系矩阵
"""


def topic_word_matrix(topic_model):
    num_topics = topic_model.num_topics
    for i in range(0, num_topics):
        words_distribution = topic_model.show_topic(i, topn=20)  # 主题的词分布
    pass
