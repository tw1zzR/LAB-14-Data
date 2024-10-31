import requests, json; from bs4 import BeautifulSoup

def count_word(url,word):
    r = requests.get(url)
    if r.status_code == 200:
        wbs = BeautifulSoup(r.text, "html.parser")
        wordlist = wbs.find_all(string=word)
        word_count = len(wordlist)
        print(f"At site '{r.url[30:]}' Word '{word}' was found {word_count} times: {wordlist}")
        return {
            "site": r.url,
            "word": word,
            "count": word_count,
            "wordlist": wordlist
        }

urls = [
    "https://en.wikipedia.org/wiki/CNN",
    "https://en.wikipedia.org/wiki/BBC",
    "https://en.wikipedia.org/wiki/Forbes"
]

results = [count_word(url, "News") for url in urls]

with open("result.json", "w", encoding="utf-8") as file:
    json.dump(results, file, ensure_ascii=False, indent=4)

print("\nResults have been written to 'result.json'")
