"""
    直接在导入该模块时读取所有数据文件
"""

import os
from . import paperReader, authorReader, metaReader

train_paper_ids_path = '../data/formatData/train_paper_ids.txt'
test_paper_ids_path = '../data/formatData/test_paper_ids.txt'
authors_list_path = '../data/formatData/collaboration_authors_list.txt'
train_paper_citation_path = '../data/formatData/train_paper_citation.txt'
test_paper_citation_path = '../data/formatData/test_paper_citation.txt'
AUTHOR_COLLABORATION_NETWORK_PATH = "../../UnifiedGraph/data/2014/networks/author-collaboration-network.txt"  # 作者协助网络
meta_path = "../../UnifiedGraph/data/2014/acl-metadata-utf8.txt"  # 论文元数据路径

cur_dir = os.path.split(__file__)[0]


#  用于计算绝对路径
def get_target_path(path):
    return os.path.join(cur_dir, path)


#  读取论文id列表
train_paper_list, train_paper_dict = paperReader.read_paper_ids(get_target_path(train_paper_ids_path))
test_paper_list, test_paper_dict = paperReader.read_paper_ids(get_target_path(test_paper_ids_path))
#  读取论文引用信息
train_paper_citation_list = paperReader.read_paper_citation(get_target_path(train_paper_citation_path))
test_paper_citation_list = paperReader.read_paper_citation(get_target_path(test_paper_citation_path))
#  读取作者名列表
authors_list, authors_dict = authorReader.read_authors_list(get_target_path(authors_list_path))
#  读取作者协作网络
author_collaboration_list = authorReader.read_author_collaboration_network(
    get_target_path(AUTHOR_COLLABORATION_NETWORK_PATH))
#  读取论文元信息
papers_meta_dict = metaReader.read_paper_metadata(get_target_path(meta_path))
