"""
    读取论文id与论文引用关系
"""

"""
    >功能: 读取论文id,生成id列表和id字典
    >参数:
        @filename: 文件路径
    >返回值:
        
"""


def read_paper_ids(filename):
    ids_list = []
    ids_dict = {}
    order = 0  # 表示每个论文对应的序号
    with open(filename, 'r') as f:
        line = f.readline()
        while line:
            paper_id = line.rstrip('\n')
            ids_list.append(paper_id)
            ids_dict[paper_id] = order
            order += 1
            line = f.readline()
    return ids_list, ids_dict


"""
    >功能: 读取论文引用关系
        
"""


def read_paper_citation(filename):
    paper_citation_list = []
    with open(filename, 'r') as f:
        line = f.readline()
        while line:
            origin, cited = line.split(',')
            cited = cited.rstrip('\n')
            paper_citation_list.append((origin, cited))
            line = f.readline()
    return paper_citation_list
