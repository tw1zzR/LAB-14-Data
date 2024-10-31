import requests; from bs4 import BeautifulSoup

r = requests.get("https://en.wikipedia.org/wiki/CNN")
r1 = requests.get("https://en.wikipedia.org/wiki/BBC")
r2 = requests.get("https://en.wikipedia.org/wiki/Forbes")

if r.status_code == 200:
    word = "News"
    wbs = BeautifulSoup(r.text, "html.parser")
    wordlist1 = wbs.find_all(string=word)
    word_count = sum(len(item.split()) for item in wordlist1)
    print(f"At site '{r.url[30:]}' Word '{word}' was find {word_count} times: {wordlist1}")

if r1.status_code == 200:
    word = "News"
    wbs = BeautifulSoup(r1.text, "html.parser")
    wordlist = wbs.find_all(string=word)
    word_count1 = sum(len(item.split()) for item in wordlist)
    print(f"At site '{r1.url[30:]}' Word '{word}' was find {word_count1} times: {wordlist}")

if r2.status_code == 200:
    word = "News"
    wbs = BeautifulSoup(r2.text, "html.parser")
    wordlist = wbs.find_all(string=word)
    word_count2 = sum(len(item.split()) for item in wordlist)
    print(f"At site '{r2.url[30:]}' Word '{word}' was find {word_count2} times: {wordlist}")

sum = word_count + word_count1 + word_count2
print(f"The total sum of words: {sum}")
