import requests
import json

def get_and_print_info(url):
    response=requests.get(url)
    if response.status_code == 200:
        articles=response.json().get('results',[])
        c=1
        for i in articles:
            title = str(c)+': '+i.get('title')
            desc=i.get("description")
            link=i.get("link")
            print(title,desc,link,sep='\n')
            c=c+1
        print('\n')
    else:
        print(f"Error :{response.status_code}")

#API_KEY="pub_91a3b69f2de24220bdf575e1c3d63967"

print("hello,welcome to real_time_news")
cond=True
while cond==True:
    print("press one of 1,2,3,4 or exit for following options")
    ch=input("enter 1 for sports,2 for entertainment,3 for crime,4 for politics,exit to close the app\n")
    match ch:
        case '1':
            url = "https://newsdata.io/api/1/latest?apikey=pub_91a3b69f2de24220bdf575e1c3d63967&country=in&language=en,hi&category=sports&timezone=Asia/Kolkata"
            print('\n')
            get_and_print_info(url)
        case '2':
            url="https://newsdata.io/api/1/latest?apikey=pub_91a3b69f2de24220bdf575e1c3d63967&country=in&language=en,hi&category=entertainment&timezone=Asia/Kolkata"
            print('\n')
            get_and_print_info(url)
        case '3':
            url = "https://newsdata.io/api/1/latest?apikey=pub_91a3b69f2de24220bdf575e1c3d63967&country=in&language=en,hi&category=crime&timezone=Asia/Kolkata"
            print('\n')
            get_and_print_info(url)
        case '4':
            url = "https://newsdata.io/api/1/latest?apikey=pub_91a3b69f2de24220bdf575e1c3d63967&country=in&language=en,hi&category=politics&timezone=Asia/Kolkata"
            print('\n')
            get_and_print_info(url)
        case 'exit':
            print("thank you for using real_time_news")
            cond=False
        case _:
            print("please enter the correct choice")