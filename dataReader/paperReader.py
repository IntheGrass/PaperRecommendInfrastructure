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


'''
@功能: 读取指定目录下所有论文文本路径和论文ID
@参数: 
    >target_dir: 指定目录
@返回值:
    >paper_paths: 论文文本文件的路径集
    >paper_ids: 对应的论文ID集
'''


def get_paper_path(target_dir):
    for root, dirs, files in os.walk(target_dir):
        paper_paths = [os.path.join(root, file) for file in files if
                       re.match('^[A-Z]\d{2}-\d{4}(\.txt)$', file) != None]
        paper_ids = [file.rstrip('.txt') for file in files if re.match('^[A-Z]\d{2}-\d{4}(\.txt)$', file) != None]
    return paper_paths, paper_ids

'''
@功能: 获取论文从摘要到引用之间的所有文本（多行转单行）,去除换行符以及单词的多行连接符（即-）
@参数：
    >filePath: 文件路径
@返回值：
    >paper_text：全文文本
'''
def get_paper_text(filePath):
    with open(filePath,'r',encoding='utf-8') as f:
        line = f.readline().rstrip('\n') # 读取时删除尾部的换行符
        paper_text = '' # 摘要文本
        while line:
            # 遇到摘要标题时，将下文文本加入到paper_text中
            if(re.sub(r'[^a-zA-Z]','',line).lower() == 'abstract'):
                line = f.readline().rstrip('\n')
                # 将本行文本用于验证是否到达尾部（references）（删除空格，转小写）
                while line and re.sub(r'[^a-zA-Z]','',line).lower() != 'references' :
                    paper_text += line.rstrip("- ") # 去除单词的多行连接符
                    line = f.readline().rstrip('\n')
                break
            line = f.readline().rstrip('\n')
    return paper_text
