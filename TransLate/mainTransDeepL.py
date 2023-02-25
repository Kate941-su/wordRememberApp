import deepl

# 定数定義
API_KEY = 'c861e777-4ab8-89ac-920e-2094c944f93a:fx'
LANGUAGE_LIST = ["JA", "EN-US", "PT"]
LANGUAGE_ENUM = {"JA" : 0, "EN-US" : 1, "PT" : 2}

# テスト用文章
#sentence = "Fazer o que gosta, é liberdade. Gostar do que faz é felicidade."
sentence = "Fazer o que gosta, é liberdade."


class MainTransDeepL():
    def __init__(self, sentence):
        # 元言語のセンテンス
        self.srcSentence = sentence
        # 翻訳機の初期化
        self.translator = deepl.Translator(API_KEY)
        # 元言語の定義
        self.srcLang = LANGUAGE_LIST[LANGUAGE_ENUM["PT"]]
        # 翻訳言語の定義
        self.destLang_1 = None
        self.destLang_2 = None
        # 元言語から翻訳言語を決定(クラスで言語情報を保持しておく)
        if (self.srcLang == LANGUAGE_LIST[LANGUAGE_ENUM["PT"]]):
            self.destLang_1 = LANGUAGE_LIST[LANGUAGE_ENUM["JA"]]
            self.destLang_2 = LANGUAGE_LIST[LANGUAGE_ENUM["EN-US"]]
        elif (self.srcLang == LANGUAGE_LIST[LANGUAGE_ENUM["EN-US"]]):
            self.destLang_1 = LANGUAGE_LIST[LANGUAGE_ENUM["JA"]]
            self.destLang_2 = LANGUAGE_LIST[LANGUAGE_ENUM["PT"]]    
        else:
            self.destLang_1 = LANGUAGE_LIST[LANGUAGE_ENUM["EN-US"]]
            self.destLang_2 = LANGUAGE_LIST[LANGUAGE_ENUM["PT"]]        
        # 翻訳後のセンテンス
        self.destSentence_1 = self.translateSentences(self.translator,
                                             self.srcSentence, self.srcLang, self.destLang_1)
        self.destSentence_2 = self.translateSentences(self.translator,
                                             self.srcSentence, self.srcLang, self.destLang_2)

    # 単語に分解する
    def splitSentence(self, sentence):
        sentence = sentence.replace(".", "")
        words = sentence.split(" ")
        return words

    # 文章を翻訳する
    def translateSentences(self, translator, sentence, srcLang, destLang):
        return translator.translate_text(sentence, source_lang = srcLang, target_lang = destLang)

    # 単語を翻訳する
    def translateWord(self, translator, words, srcLang, destLang):
        translateWordList = []
        for word in words:
            translateWordList.append(translator.translate_text(word, 
                                            source_lang = srcLang, 
                                            target_lang = destLang))   
        return translateWordList
    # 元言語の文章を取得する
    def getTransSentence(self, lang = None):
        return self.srcSentence
    # 翻訳後の文章を取得する
    def getTransSentence(self, lang = None):
        return self.destSentence_1, self.destSentence_2

# インスタンス化
mtd = MainTransDeepL(sentence)
ret1, ret2 = mtd.getTransSentence()
print(ret1)
print(ret2)



#単語の分解
#wordsSrc = splitSentence(sentence)
#重複の削除
#wordsSrc = list(set(wordsSrc))
#wordsDest_1 = translateWord(translator, wordsSrc, srcLang, destLang_1)
#wordsDest_2 = translateWord(translator, wordsSrc, srcLang, destLang_2)
# 翻訳を実行
#result = translator.translate_text(sentence, source_lang = LANGUAGE_LIST[LANGUAGE_ENUM["PT"]],
#                                             target_lang = LANGUAGE_LIST[LANGUAGE_ENUM["EN-US"]])