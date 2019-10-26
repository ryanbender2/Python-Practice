""" English to Pig Latin Translator
    Write two functions to make an English to pig latin translator.
    The first function translate_word(word) takes a single word and
    returns that word translated into pig latin. The second function
    translate_sentence(sentence) takes an English sentince and returns
    that sentence translated into pig latin.
"""
import re

def translate_word(word):
    if len(word) == 0:
        return ''
    vowels = ['a', 'e', 'i', 'o', 'u']
    if word[0].lower() in vowels:
        return word + 'yay'
    vwl_idx = None
    for let in word:
        if let in vowels:
            vwl_idx = word.index(let)
            break
    new_word = word[vwl_idx:] + word[:vwl_idx] + 'ay'
    if word[0].isupper():
        new_word = list(new_word.lower())
        new_word[0] = new_word[0].upper()
        new_word = ''.join(new_word)
    return new_word


def translate_sentence(sentence):
    sen_lst = sentence.split(' ')
    for word in range(len(sen_lst)):
        for char in ['"', ',', '?', '.']:
            sen_lst[word] = sen_lst[word].strip(char)

    trans_words = sentence.split(' ')
    for word in range(len(sen_lst)):
        for char in ['"', ',', '?', '.']:
            trans_words[word] = trans_words[word].strip(char)
    
    for word in range(len(trans_words)):
        new_w = translate_word(trans_words[word])
        trans_words[word] = new_w
    for word in range(len(sen_lst)):
        sentence = sentence.replace(sen_lst[word], trans_words[word], 1)

    return sentence





print(translate_sentence('Hello how is it going?'))