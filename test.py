str1 = 'welocme to super&Test'

# def reverse_srt1(str1):
#     srt2 = str1.split()
#     # print(srt2)
#     new_srt = []
#     for word in srt2:
#         for i in range(len(word)):
#             x = ''.join([word[i] for i in range(len(word) - 1, -1, -1)])
#             print(x)
#             new_srt.append(x)
#     return ' '.join(new_srt)
#
#
#
# print(reverse_srt1(str1))


def fun1(str1):
    m = ''
    for n in str1:
        m = n + m
    return m



def fun2(srt1):
    words = []  # 用于存储单词的列表
    current_word = ''  # 当前正在构建的单词
    for char in srt1:
        if char.isalnum():  # 如果字符是字母或数字，它是单词的一部分
            current_word += char  # 追加到当前单词
        else:
            if current_word:  # 如果当前单词已经结束（遇到了非字母数字字符）
                words.append(fun1(current_word))  # 反转并存储当前单词
                current_word = ''  # 重置当前单词为空
            words.append(char)  # 将非字母数字字符直接加入单词列表
    if current_word:  # 处理最后一个单词
        words.append(fun1(current_word))  # 反转并添加到单词列表

    return ''.join(words)  # 将所有元素连接成一个字符串
#

# 输出结果
new_str = fun2(str1)
print(new_str)
