meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "РОФЛ":  "шутка",
            "ЩИЩ": "одобрение или восторг",
            "КРИПОВЫЙ":  "страшный, пугающий",
            "АГРИТЬСЯ":  "злиться",
            }
word = input("Введите непонятное слово (большими буквами!): ")

if word in meme_dict.keys():
    print (meme_dict [word])
else:
     print ("Слово неизвестно")
