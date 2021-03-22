import textReader
import trainer
import numpy as np

from gensim import corpora
from gensim.models import LdaModel
import pickle


if __name__ == '__main__':
    (paper_paths, paper_ids) = textReader.get_paper_path('../../data/aan/papers_text/')
    abstract_documents = [textReader.get_abstract_text(path) for path in paper_paths]
    abstract_corpus = trainer.participle(abstract_documents)  # 分词
    word_dictionary = corpora.Dictionary(abstract_corpus)   # 字典
    abstract_bow = [word_dictionary.doc2bow(text) for text in abstract_corpus]  # 转词袋向量模型
    abstract_lda_model = LdaModel(corpus=abstract_bow, id2word=word_dictionary, num_topics=100)  # 训练模型
    # 载入缓存
    with open('./storage/abstract_corpus.data', 'wb') as f:
        pickle.dump(abstract_corpus, f)
    word_dictionary.save('./storage/abstract_dictionary.data')
    abstract_lda_model.save('./storage/abstract_lad_model.data')


