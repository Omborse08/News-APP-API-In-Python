import requests
import json
import platform
import os
import time
import shutil

if not os.path.exists("FakeArticle2025.txt"):
    open("FakeArticle2025.txt",'w').close()
    print("> File Created ")
else:
    print("> Already Exited")

class news:
    def __init__(self):
        pass

    def openfile(self,path):
        if platform.system() == 'Windows':
            os.startfile(path)
        elif platform.system() == 'Darwin':
            os.system(f"open \"{path}\"")
        else:
            print("\nCheck Your System Broo! ")

    @staticmethod
    def show_news(search):
        alt_news = (f"https://newsapi.org/v2/everything?q={search}&from=2025-07-26&sortBy=publishedAt&apiKey=9077577b088141559a0000acdab5217e")
        resource = requests.get(alt_news)
        json_news = json.loads(resource.text)
        with open("FakeArticle2025.txt",'w') as file:        
            for new_news in json_news['articles']:
                print(new_news.get('title','No title available'))
                print(new_news.get('description','No description available'))
                print(50*'-')
                file.write(new_news.get('title','No title available') + "\n")
                file.write(new_news.get('description','No description available') + "\n")
                file.write("-" * 50 + "\n")

                break_choice = input("    > q [ Quit ] <   > Enter [ Continue ] < ") 
                if break_choice == "q":
                    break

    @staticmethod
    def news_menu():
        print("""[1] 🏏 Cricket News
[2] ⚽ Football News
[3] 📰 AI World News
[4] 🔎 Search News
[5] 💾 Saved Articles
[6] Quit""")

default_search = {
    1:"Cricket",
    2:"Football",
    3:"AI News"
}

new = news()

new.news_menu()
while True:
    choice = int(input("\n> Choose Option: "))
    try:
      match choice:
        case 1 | 2 | 3:
            if choice in default_search:
                new.show_news(default_search[choice])

        case 4:
            search_choose = input("\n> Enter What You Search: ")
            new.show_news(search_choose)
        
        case 5:
            print("\n> File Open In 3 Seconds")
            time.sleep(3)
            new.openfile("FakeArticle2025.txt")
        
        case 6:
            print("\n> Thank You For Using My Code! ")
            print("APP Deleting In 3 Seconds")
            time.sleep(3)
            os.remove("FakeArticle2025.txt")
            pyfile = __file__
            if os.path.exists(pyfile):
                os.remove(pyfile)
            break

        case _:
            print("\n> Broo Look At the Keyboard Man!")
    
    except Exception:
        print("\nInvalid Option..")