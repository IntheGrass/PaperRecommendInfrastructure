import textReader
import trainer
import numpy as np

from gensim import corpora
from gensim.models import LdaModel
import pickle


if __name__ == '__main__':
    (paper_paths, paper_ids) = textReader.get_paper_path('../../../data/aan/papers_text/')  # 路径要修改为对应的文本数据路径
    #  读取摘要文本
    abstract_documents = [textReader.get_abstract_text(path) for path in paper_paths]
    abstract_corpus = trainer.participle(abstract_documents)  # 分词
    filtered_abstract_corpus = trainer.filter_words_by_frequency(abstract_corpus, 10) # 过滤掉词频低于10的词
    word_dictionary = corpora.Dictionary(filtered_abstract_corpus)   # 生成字典
    abstract_bow = [word_dictionary.doc2bow(text) for text in filtered_abstract_corpus]  # 转词袋向量模型
    abstract_lda_model = LdaModel(corpus=abstract_bow, id2word=word_dictionary, num_topics=200)  # 训练模型
    # 载入缓存
    with open('./storage/abstract_corpus.data', 'wb') as f:
        pickle.dump(abstract_corpus, f)
    word_dictionary.save('./storage/abstract_dictionary.data')
    abstract_lda_model.save('./storage/abstract_lad_model.data')


