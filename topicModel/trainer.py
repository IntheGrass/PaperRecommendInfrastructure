"""
    模型训练
"""
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem import SnowballStemmer

######################文本预处理模块############################

"""
    >功能: 对语料库进行分词，并删除停用词，将每个文本转化为分词列表
    >参数:
        @documents: 文档集，每一项对应一段文本
    >return:
        @corpus: 分词后的语料库，即词向量的列表
"""


def participle(documents):
    corpus = []
    tokenizer = RegexpTokenizer(r'[a-zA-z\']{3,}')
    count = 0
    for text in documents:
        words = tokenizer.tokenize(text)  # 分词，同时过滤掉标点符号(不包含单引号)、数字与少于两个个字符的词
        # 获取删除停用词后的分词表
        filtered_words = [word for word in words if word.lower() not in stopwords.words('english')]
        # 词干提取
        filtered_words = stemming(filtered_words)
        corpus.append(filtered_words)
        count += 1
        if count % 100 == 0:
            print(f'current {count}/{len(documents)}')
    return corpus


"""
    >介绍: 过滤掉语料库中低词频的词
    >参数:
        @corpus: 原语料库
        @min_frequency: 最小词频，小于此词频的将会被过滤掉
    >返回值:
        @filtered_corpus: 过滤低词频词的语料库
"""


def filter_words_by_frequency(corpus, min_frequency):
    count_dict = {}
    for words in corpus:
        for word in words:
            if word in count_dict.keys():
                count_dict[word] += 1
            else:
                count_dict[word] = 1
    filtered_corpus = []
    for words in corpus:
        filtered_corpus.append([word for word in words if count_dict[word] >= min_frequency])
    return filtered_corpus


"""
    >介绍: 词干提取，给定一个词列表，将所有词转化为词的原型（伪）
    >参数:
        @words: 词列表
    >返回值:
        @stemming_words: 词干提取后的词列表
"""


def stemming(words):
    snowball_stemmer = SnowballStemmer('english')
    stemming_words = [snowball_stemmer.stem(word) for word in words]
    return stemming_words


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
    >介绍：根据模型获得主题与词的关系矩阵
    >返回值:
        topics-words的关系矩阵
"""


def topic_word_matrix(topic_model):
    return topic_model.get_topics()
