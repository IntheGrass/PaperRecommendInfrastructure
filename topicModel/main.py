import textReader
import trainer

from gensim import corpora
from gensim.models import LdaModel

if __name__ == '__main__':
    (paper_paths, paper_ids) = textReader.get_paper_path('../../data/aan/papers_text/')
    abstract_documents = [textReader.get_abstract_text(path) for path in paper_paths]
    abstract_corpus = trainer.participle(abstract_documents)
    word_dictionary = corpora.Dictionary(abstract_corpus)
    abstract_bow = [word_dictionary.doc2bow(text) for text in abstract_corpus]
    abstract_lda_model = LdaModel(corpus=abstract_bow, id2word=word_dictionary, num_topics=100)
