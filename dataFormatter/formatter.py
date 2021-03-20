import paperFormatter
import authorFormatter

PAPER_IDS_PATH = "../../UnifiedGraph/data/2014/paper_ids.txt"  # 论文ID集路径
PAPER_CITATION_PATH = "../../UnifiedGraph/data/2014/acl.txt"  # 论文引用网络
author_collaboration_network_path = "../../UnifiedGraph/data/2014/networks/author-collaboration-network.txt"  # 作者协助网络
OUTPUT_DIR = '../data/formatData/'  # 输出目录

if __name__ == '__main__':
    paperFormatter.train_test_paper_data_split(PAPER_IDS_PATH, OUTPUT_DIR)
    paperFormatter.train_test_paper_citation_split(PAPER_CITATION_PATH, OUTPUT_DIR)
    authorFormatter.extract_collaboration_authors_list(author_collaboration_network_path, OUTPUT_DIR)