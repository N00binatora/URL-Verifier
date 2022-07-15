import requests

try:
    users = input('enter URL: ')
    r = requests.get(users)
    if r.status_code == 200:
        print("Website is up!")
    else:
        print("Website is down :(")
except:
    print("URL not valid, try again! (try with http or https://wwww.websiteofchoice.com)")
