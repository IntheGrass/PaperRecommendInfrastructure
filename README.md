# 论文推荐基础架构

## 简介

论文推荐的基础架构，主要包含对数据集的预处理，用于填充核心的论文推荐代码

## 文件结构

```python
│  .gitignore
│  main.py
│  organization.txt
│  README.md
│  日志.md
│          
├─data
│  ├─basicData  # 从AAN论文集复制过来的原始数据集
│  │      acl-metadata-utf8.txt
│  │      acl.txt
│  │      author-collaboration-network.txt
│  │      paper_ids.txt
│  │      
│  └─formatData # 将AAN的原始数据集进行提炼、划分，得到更易读取的数据集，
│          collaboration_authors_list.txt
│          test_paper_citation.txt
│          test_paper_ids.txt
│          train_paper_citation.txt
│          train_paper_ids.txt
│          
├─dataFormatter	# 将AAN原始数据进行格式化的包,包含如下操作：训练/测试集划分、精炼数据
│  │  authorFormatter.py	
│  │  formatter.py	# 执行文件
│  │  paperFormatter.py
│  │  __init__.py
│          
├─dataReader	# 读取数据包，主要是从data/formatData/中读取，部分直接从basicData读取
│  │  authorReader.py
│  │  localReader.py # 调用后直接获得读取后的数据，如论文id列表、作者列表、论文引用关系等
│  │  metaReader.py
│  │  paperReader.py
│  │  reader.py
│  │  __init__.py
│          
├─paperRecommend # 论文推荐的实现，需要添加的地方
│  │  main.py	# 论文推荐的实现部分，(未完成)
│  │  preprocess.py	#	数据集的预处理包，主要功能是根据dataReader的数据来获得对应的矩阵
│  │  util.py
│  │  __init__.py
│          
└─topicModel	# 主题建模，包含使用gensim实现的一个简单的主题建模
│  │  cache.py	
│  │  textReader.py	#	包含读取文本数据的方法
│  │  main.py  # 训练了一个简单的LDA模型
│  │  trainer.py  # 包含一个
│  │  __init__.py    
```

## 当前任务

- [ ] 使用`gensim`库训练LDA主题模型
- [ ] 将主题模型应用到论文推荐中去

