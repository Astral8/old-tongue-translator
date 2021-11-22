# from bs4 import BeautifulSoup
# from urllib.request import Request, urlopen
#
# url = "https://www.tor.com/2016/12/20/the-wheel-of-time-english-to-old-tongue-dictionary/"
# hdr = {'User-Agent': 'Mozilla/5.0'}
# req = Request(url,headers=hdr)
# page = urlopen(req)
# soup = BeautifulSoup(page, features="lxml")
#
# file1 = open("dictionary.txt","w")
# for word in soup.find_all('em'):
#     file1.write(word.parent.get_text())
#     file1.write("\n")
#
# file1.close()

file1 = open("dictionary.txt", "r")
lines = file1.readlines()
file1.close()
dictionary = {}
for line in lines:
    line = line.strip()
    speech = line[line.find("(") + 1:line.find(")")]
    english_word = line.split('(')[0]
    old_tongue_word = line.split("- ", 1)[1]
    dictionary[english_word] = {}
    dictionary[english_word][speech] = [old_tongue_word]
    # print("english word is", english_word)
    # print("old tongue word is", old_tongue_word)
    # print(speech)

print(dictionary)
