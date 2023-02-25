import deepl

# 定数定義
API_KEY = 'c861e777-4ab8-89ac-920e-2094c944f93a:fx'
LANGUAGE_LIST = ["JA", "EN-US", "PT"]
LANGUAGE_ENUM = {"JA" : 0, "EN-US" : 1, "PT" : 2}

# テスト用文章
sentence = "Fazer o que gosta, é liberdade. Gostar do que faz é felicidade."

# 単語に分解する
def splitSentence(sentence):
    sentence = sentence.replace(".", "")
    words = sentence.split(" ")
    return words

# 単語を翻訳する
def translateWord(translator, words, srcLang, destLang):
    translateWordList = []
    for word in words:
        translateWordList.append(translator.translate_text(word, 
                                        source_lang = srcLang, 
                                        target_lang = destLang))   
    return translateWordList



# 翻訳機の初期化
translator = deepl.Translator(API_KEY)

#単語の分解
wordsPT = splitSentence(sentence)
wordsEN = translateWord(translator, wordsPT,
     LANGUAGE_LIST[LANGUAGE_ENUM["PT"]], LANGUAGE_LIST[LANGUAGE_ENUM["EN-US"]])

# 翻訳を実行
#result = translator.translate_text(sentence, source_lang = LANGUAGE_LIST[LANGUAGE_ENUM["PT"]],
#                                             target_lang = LANGUAGE_LIST[LANGUAGE_ENUM["EN-US"]])