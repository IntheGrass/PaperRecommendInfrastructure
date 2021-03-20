"""
    用于读取论文的全文数据，构建语料库
"""
import os
import re

'''
@功能: 获取单篇论文文本中的摘要文本（多行转单行）,去除换行符以及单词的多行连接符（即-）
@参数：
    >filePath: 文件路径
@返回值：
    >abstract_text：摘要文本
'''


def get_abstract_text(filePath):
    with open(filePath, 'r', encoding='utf-8') as f:
        line = f.readline().rstrip('\n')  # 读取时删除尾部的换行符
        abstract_text = ''  # 摘要文本
        # 该正则主要是为了删除非字母的字符
        while line and re.sub(r'[^a-zA-Z]', '', line).lower() != 'introduction':
            # 当没有abstract标题时，将introduction之前的所有文本作为摘要
            abstract_text += line.rstrip("- ")  # 去除单词的多行连接符
            # 遇到摘要标题时，将下文文本加入到abstract_text中
            if re.sub(r'[^a-zA-Z]', '', line).lower() == 'abstract':
                abstract_text = ''
                line = f.readline().rstrip('\n')
                # 将本行文本转为用于验证是否到下一标题（introduction）的形式
                validation_text = re.sub(r'[^a-zA-Z]', '', line).lower()
                while line and validation_text != 'introduction':
                    abstract_text += line.rstrip("- ")  # 去除单词的多行连接符
                    line = f.readline().rstrip('\n')
                    validation_text = re.sub(r'[^a-zA-Z]', '', line).lower()
                break
            line = f.readline().rstrip('\n')
    return abstract_text


'''
@功能: 获取论文从摘要到引用之间的所有文本（多行转单行）,去除换行符以及单词的多行连接符（即-）
@参数：
    >filePath: 文件路径
@返回值：
    >paper_text：全文文本
'''


def get_paper_text(filePath):
    with open(filePath, 'r', encoding='utf-8') as f:
        line = f.readline().rstrip('\n')  # 读取时删除尾部的换行符
        paper_text = ''  # 摘要文本
        while line:
            if re.sub(r'[^a-zA-Z]', '', line).lower() == 'abstract':
                # 遇到摘要标题时，将下文文本加入到paper_text中
                line = f.readline().rstrip('\n')
                # 将本行文本用于验证是否到达尾部（references）（删除空格，转小写）
                while line and re.sub(r'[^a-zA-Z]', '', line).lower() != 'references':
                    paper_text += line.rstrip("- ")  # 去除单词的多行连接符
                    line = f.readline().rstrip('\n')
                break
            line = f.readline().rstrip('\n')
    return paper_text


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
                       re.match(r'^[A-Z]\d{2}-\d{4}(\.txt)$', file) is not None]
        paper_ids = [file.rstrip('.txt') for file in files if re.match(r'^[A-Z]\d{2}-\d{4}(\.txt)$', file) is not None]
    return paper_paths, paper_ids
