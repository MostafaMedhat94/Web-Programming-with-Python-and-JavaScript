import requests

def main():
    res = requests.get('https://www.otmost.com')
    print(res.text)

if __name__ == '__main__':
    main()

