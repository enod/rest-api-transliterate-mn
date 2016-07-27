# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
from transliterate import translit, get_available_language_codes
import os
import codecs
import re
app = Flask(__name__)
directory = os.getcwd()
# with codecs.open(directory + "/mnwiktionary-latest-all-titles-in-ns0", "r", encoding='utf-8') as f:
#     data = f.readlines()
#     writing = [line.lower() for line in data]
#     f.close()
#
# with codecs.open(directory + "/output.txt", "wb", encoding='utf-8') as f:
#     for item in writing:
#         f.write("%s" % item)
with codecs.open(directory + "/output.txt", "r", encoding='utf-8') as f:
    data = f.readlines()


def replacer(word):
    search_word = translit(word, 'mn')
    if u"ө" in search_word:
        search_word_regex = search_word.replace(u"ө", u"[өүу]")
        search_word_regex_reform = "^" + search_word_regex + '$'
        found_or_not = [item for i, item in enumerate(data) if re.search(search_word_regex_reform, item)]

        if found_or_not:
            return found_or_not[0]
        else:
            return search_word
    elif u"у" in search_word:
        search_word_regex = search_word.replace(u"у", u"[өүу]")
        search_word_regex_reform = "^" + search_word_regex + '$'
        found_or_not = [item for i, item in enumerate(data) if re.search(search_word_regex_reform, item)]

        if found_or_not:
            return found_or_not[0]
        else:
            return search_word
    elif u'үү' == search_word:
        return u'уу'
    elif u"ү" in search_word:
        search_word_regex = search_word.replace(u"ү", u"[өүу]")
        search_word_regex_reform = "^"+search_word_regex+'$'
        found_or_not = [item for i, item in enumerate(data) if re.search(search_word_regex_reform, item)]

        if found_or_not:
            return found_or_not[0]
        else:
            return search_word
    else:
        return search_word


@app.route('/', methods=['POST'])
def converter():
    content = request.json
    result = map(lambda x: replacer(x.lower()) if u'u' in x else translit(x, 'mn'), content['text'].split())
    result = [i.strip("\n") for i in result]
    return " ".join(result) + "\n"


@app.route('/', methods=['GET'])
def returner():
    return jsonify({"message": 'It works!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0')

