import urllib.request
import re

def connect(host):

    try:
        urllib.request.urlopen(host)
        return 1
    except:
        return 0

def test(url):

    count, trys = 0, 10
    for _ in range(trys):
        count += connect(url)
        #if i % trys == 0:
        print("#", end='', flush=True)
    print()
    if count == 10:
        print("Connection to "+url+" is stable")
    elif count > 0:
        print("Connection to "+url+" is unstable")
        
    else:
        print("Connection to "+url+" not established")
    print("Passed "+str(count)+"/"+str(10)+" connections")

def validate(url):

    regex = re.compile(
            r'^(?:http|ftp)s?://' # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
            r'localhost|' #localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
            r'(?::\d+)?' # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    
    return re.match(regex, url)

def enter_url(url=""):

    while True:
        if url == "":
            url = input("Enter a URL: ").strip()
        if url.lower() == 'exit':
            exit()
        if validate(url):
            break
        print("Inavlid URL format\n")
        url = ""

    test(url)


def run():
    
    while True:
        print("Enter a URL to test")
        mode = input()
        if mode.lower() == 'exit':
            break
        elif mode.lower() in ('1', 'enter', 'enter a url') or mode.strip == "":
            enter_url()
        else:
            enter_url(mode)
    exit()

run()

