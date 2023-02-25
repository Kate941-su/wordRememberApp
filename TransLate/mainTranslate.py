from googletrans import Translator
#定数定義
languageList = ["ja", "en", "pt"]
translator = Translator()
sentence = "Fazer o que gosta, é liberdade. Gostar do que faz é felicidade."
sentence = sentence.replace(".", "")
words = sentence.split(" ")
sentenceTrans = translator.translate(sentence, dest = "en", src = "auto")

languageEnum = {"ja" : 0, "en" : 1, "pt" : 2}

#言語リストの初期化する
def initList(languageList):
    wordList = []
    for i in range(len(languageList)):
        wordList.append([])
    return wordList

#翻訳を実行する
def translate(Translator, src, dst, wordList):
    for word in wordList:
        wordList.append(translator.translate(word, dest = dst, src = src))           

#ワードリストの初期化
wordList = initList(languageList)


#English翻訳
for word in words:
    wordTrans.append(translator.translate(word, dest = "en", src = "auto"))   

#portgueses翻訳
for i in range(len(wordTrans)):
    print("src : {0}, dest : {1}".format(words[i], wordTrans[i].text))