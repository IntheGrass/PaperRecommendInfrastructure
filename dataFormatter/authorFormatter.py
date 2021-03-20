"""
    从作者数据中提取
"""
from os.path import join


"""
    >功能: 从作者协助网络中读取所有作者信息
    >参数:
        @path: 
"""


def extract_collaboration_authors_list(path, output_dir):
    author_set = set()  # 作者集合
    with open(path, 'r', encoding='utf-8') as f:
        line = f.readline()
        while line:
            first_a, second_a = line.split('==>')
            line = f.readline()
            # 读取两个作者名及其对应序号
            first_a = first_a.strip()
            second_a = second_a.strip()
            author_set.add(first_a)
            author_set.add(second_a)
    author_list = list(author_set)
    author_list.sort()
    authors_path = join(output_dir, 'collaboration_authors_list.txt')
    with open(authors_path, 'w', encoding='utf-8') as f:
        for author in author_list:
            f.write(author)
            f.write('\n')
    return author_list
