"""
    包含将原始的论文数据转为格式化数据的方法
"""
import re
from os.path import join

BOUNDARY = 12  # 表示训练集和测试集的年份边界，12表示2012年及之后发表的论文为测试集、其他为训练集

'''
    >功能: 将对应文件内的论文id分为训练集和测试集id
    >参数:
        @path:  原始数据的文件路径
        @output_dir: 文件输出目录
    >返回值:
        @train_list: 训练集id列表
        @test_list: 测试集id列表
'''


def train_test_paper_data_split(path, output_dir):
    train_list = []
    test_list = []
    with open(path, 'r', encoding='utf-8') as f:
        line = f.readline()
        while line:
            paper_id = line.split('\t')[0]
            line = f.readline()
            judge = is_train(paper_id)  # 表示该paper是否为训练集的判断
            if judge is None:
                continue
            if judge:
                # 当该paper为训练集时
                train_list.append(paper_id)
            else:
                # 当该paper为训练集时
                test_list.append(paper_id)
        train_path = join(output_dir, 'train_paper_ids.txt')
        test_path = join(output_dir, 'test_paper_ids.txt')
        output_paper_ids(train_path, train_list)
        output_paper_ids(test_path, test_list)
    return train_list, test_list


"""
    >功能: 将论文的引用关系按照训练集和测试集进行拆分
"""


def train_test_paper_citation_split(path, output_dir):
    train_citation_list = []  # 训练集的引用关系的引用文和被引用文都必须属于训练集
    test_citation_list = []  # 测试集的引用关系只需含有测试集即可
    with open(path, 'r', encoding='utf-8') as f:
        line = f.readline()
        while line:
            (origin, cited) = line.split('==>')
            line = f.readline()
            origin = origin.strip()  # 删除两边空格后得到原论文ID
            cited = cited.strip()
            #  舍去被引用论文为测试集的引用关系
            if is_train(cited):
                if is_train(origin):
                    train_citation_list.append((origin, cited))
                else:
                    test_citation_list.append((origin, cited))
    train_path = join(output_dir, 'train_paper_citation.txt')
    test_path = join(output_dir, 'test_paper_citation.txt')
    output_paper_citation(train_path, train_citation_list)
    output_paper_citation(test_path, test_citation_list)
    return train_citation_list, test_citation_list


'''
    >功能: 输出论文id列表
    >参数:
        @filename: 文件路径
        @paper_ids: 论文id列表
    >返回值：
        None
'''


def output_paper_ids(filename, paper_ids):
    with open(filename, 'w') as f:
        for paper_id in paper_ids:
            f.write(str(paper_id))
            f.write('\n')


'''
    >功能： 输出论文引用元组    
'''


def output_paper_citation(filename, citation_list):
    with open(filename, 'w') as f:
        for citation in citation_list:
            f.write(citation[0])
            f.write(',')
            f.write(citation[1])
            f.write('\n')


'''
    >功能：
        根据论文ID判断论文属于训练集，2012年以前的均为训练集。
        论文ID格式应为:Cyy-xxxx, 其中C为任意字母，yy为论文发表年份的后二位数字，如1999对应99
    >参数：
        @paper_id: 论文ID
    >返回值：
        None, False或True, 低于设定年份返回True，否则为False。如果格式不匹配返回None
'''


def is_train(paper_id):
    match_obj = re.match(r'^\w(\d{2})-\d{4}\w?$', paper_id)
    # 测试集的年份上下界
    lower = BOUNDARY  # 下界
    upper = lower + 20  # 上界
    # 不匹配
    if match_obj is None:
        # raise Exception("paper_id 格式有误")
        print('paper ID:\t', paper_id, "\t warning: 格式有误，跳过")
        return None
    year = int(match_obj.group(1))  # 获得论文ID中表示年份的2位标识
    if lower <= year <= upper:
        return False
    else:
        return True
