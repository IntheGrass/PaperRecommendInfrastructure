# �����Ƽ������ܹ�

## ���

�����Ƽ��Ļ����ܹ�����Ҫ���������ݼ���Ԥ�������������ĵ������Ƽ�����

## �ļ��ṹ

```python
��  .gitignore
��  main.py
��  organization.txt
��  README.md
��  ��־.md
��          
����data
��  ����basicData  # ��AAN���ļ����ƹ�����ԭʼ���ݼ�
��  ��      acl-metadata-utf8.txt
��  ��      acl.txt
��  ��      author-collaboration-network.txt
��  ��      paper_ids.txt
��  ��      
��  ����formatData # ��AAN��ԭʼ���ݼ��������������֣��õ����׶�ȡ�����ݼ���
��          collaboration_authors_list.txt
��          test_paper_citation.txt
��          test_paper_ids.txt
��          train_paper_citation.txt
��          train_paper_ids.txt
��          
����dataFormatter	# ��AANԭʼ���ݽ��и�ʽ���İ�,�������²�����ѵ��/���Լ����֡���������
��  ��  authorFormatter.py	
��  ��  formatter.py	# ִ���ļ�
��  ��  paperFormatter.py
��  ��  __init__.py
��          
����dataReader	# ��ȡ���ݰ�����Ҫ�Ǵ�data/formatData/�ж�ȡ������ֱ�Ӵ�basicData��ȡ
��  ��  authorReader.py
��  ��  localReader.py # ���ú�ֱ�ӻ�ö�ȡ������ݣ�������id�б������б��������ù�ϵ��
��  ��  metaReader.py
��  ��  paperReader.py
��  ��  reader.py
��  ��  __init__.py
��          
����paperRecommend # �����Ƽ���ʵ�֣���Ҫ��ӵĵط�
��  ��  main.py	# �����Ƽ���ʵ�ֲ��֣�(δ���)
��  ��  preprocess.py	#	���ݼ���Ԥ���������Ҫ�����Ǹ���dataReader����������ö�Ӧ�ľ���
��  ��  util.py
��  ��  __init__.py
��          
����topicModel	# ���⽨ģ������ʹ��gensimʵ�ֵ�һ���򵥵����⽨ģ
��  ��  cache.py	
��  ��  textReader.py	#	������ȡ�ı����ݵķ���
��  ��  main.py  # ѵ����һ���򵥵�LDAģ��
��  ��  trainer.py  # ����һ��
��  ��  __init__.py    
```

## ��ǰ����

- [ ] ʹ��`gensim`��ѵ��LDA����ģ��
- [ ] ������ģ��Ӧ�õ������Ƽ���ȥ

