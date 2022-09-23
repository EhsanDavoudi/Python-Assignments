def words_cn(sen):
    sen_lis = sen.split()
    num_words = len(sen_lis)
    return num_words
    
sentence = input('Enter sentence:')
print(f'number of words in your sentence: {words_cn(sentence)}')