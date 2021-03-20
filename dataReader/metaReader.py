"""
    读取论文的元数据信息
"""

"""
    >功能：
        读取论文元信息，返回一个ID->元信息的映射字典
    >参数：
        @path: 文件路径
    >返回值：
        @paper_meta_dict: 
"""


def read_paper_metadata(path):
    f = open(path, 'r', encoding='utf-8')
    paper_meta_dict = {}
    line = f.readline()
    count = 1
    while line:
        paper_meta = {}
        key, paper_id = key_value_extraction(line)
        for i in range(0, 4):
            line = f.readline()
            count += 1
            key, value = key_value_extraction(line)
            if key is None:
                print(count)
                continue
            if key != 'author':
                paper_meta[key] = value
            else:
                # 储存文本数据
                paper_meta['author_text'] = value
                # 作者元数据需要转化为数组
                # (分隔符的空格不能删，有些作者名是自带分号的)
                authors = value.split('; ')
                authors = [val.strip() for val in authors if len(val.strip()) > 0]
                paper_meta[key] = authors
        paper_meta_dict[paper_id] = paper_meta
        # 读空行
        f.readline()
        # 读ID行
        line = f.readline()
        count += 2
    f.close()
    return paper_meta_dict

"""
    >功能:
        对如下格式：key = { value }的字符串进行键值对提取
    >参数:
        @line: 包含键值对数据的字符串，符合如下格式：key = { value }
    >返回值:
        @key: 键
        @value: 值
"""


def key_value_extraction(line):
    key, value = line.split('=', 1)
    key = key.strip()
    # 读取{}内的内容
    try:
        left_index = value.index('{') + 1
        right_index = value.rindex('}')
    except ValueError:
        print('格式错误：无完整花括号')
        return None, None
    else:
        value = value[left_index:right_index].strip()
        return key, value
