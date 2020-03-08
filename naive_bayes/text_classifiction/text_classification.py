# coding: utf-8
# 中文文本分类
import os
import jieba
import warnings
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

warnings.filterwarnings('ignore')


def cut_words(file_path):
    """
    对文本进行切词
    :param file_path: txt文本路径
    :return: 用空格分词的字符串
    """
    text_with_spaces = ''
    with open(file_path, 'r', encoding='gb18030', errors='ignore') as f:
        text = f.read()
        textcut = jieba.cut(text)
        for word in textcut:
            text_with_spaces += word + ' '
    return text_with_spaces


text_category = ['女性', '体育', '文学', '校园']



def loadfile(data_path):
    """
    将路径下的所有文件加载
    :param file_dir: 保存txt文件目录
    :param label: 文档标签
    :return: 分词后的文档列表和标签
    """
    words_list = []
    labels = []
    for category in text_category:
        file_path = data_path  + category + '/'
        file_list = os.listdir(file_path)
        for file in file_list:
            words_list.append(cut_words(file_path+file))
        labels.append(category)
    return words_list, labels


def get_stop_words(stop_words_path):
    stop_words = open(stop_words_path, 'r', encoding='utf-8').read()
    stop_words = stop_words.encode('utf-8').decode('utf-8-sig')  # 列表头部\ufeff处理
    stop_words = stop_words.split('\n')  # 根据分隔符分隔

    return stop_words


if __name__ == '__main__':
    train_data_path = 'train' + '/'
    test_data_path = 'test' + '/'
    stop_words_path = 'stop/stopword.txt'
    train_words_list, train_labels = loadfile(train_data_path)

    test_words_list, test_labels = loadfile(test_data_path)

    stop_words = get_stop_words(stop_words_path)

    tf = TfidfVectorizer(stop_words=stop_words, max_df=0.5)

    train_features = tf.fit_transform(train_words_list)

    # 上面fit过了，这里transform
    test_features = tf.transform(test_words_list)

    # 多项式贝叶斯分类器
    from sklearn.naive_bayes import MultinomialNB

    clf = MultinomialNB(alpha=0.001).fit(train_features, train_labels)
    predicted_labels = clf.predict(test_features)

    # 计算准确率
    print('准确率为：', metrics.accuracy_score(test_labels, predicted_labels))
