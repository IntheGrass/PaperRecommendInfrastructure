from dataReader import localReader as data
import preprocess
import util


if __name__ == "__main__":
    PP = preprocess.selfRelationToMatrix(data.train_paper_citation_list, data.train_paper_dict) # 获取
    AA = preprocess.selfRelationToMatrix(data.author_collaboration_list, data.authors_dict, symmetric=True)
    PA, AP = preprocess.paper_connect_author(data.papers_meta_dict, data.train_paper_list, data.train_paper_list)
    test_citation_dict = preprocess.get_test_citation_dict(data.test_paper_citation_list)




