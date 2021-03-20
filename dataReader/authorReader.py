
def read_authors_list(filename):
    authors_list = []
    authors_dict = {}
    order = 0  # 表示每个作者对应的序号
    with open(filename, 'r', encoding='utf-8') as f:
        line = f.readline()
        while line:
            author_name = line.rstrip('\n')
            authors_list.append(author_name)
            authors_dict[author_name] = order
            order += 1
            line = f.readline()
    return authors_list, authors_dict


def read_author_collaboration_network(filename):
    collaboration_list = []
    with open(filename, 'r', encoding='utf-8') as f:
        line = f.readline()
        while line:
            # 读取两个作者名
            first_a, second_a = line.split('==>')
            line = f.readline()
            # 作者名去掉两边空格，转小写
            first_a = first_a.strip().lower()
            second_a = second_a.strip().lower()
            collaboration_list.append((first_a, second_a))
    return collaboration_list
