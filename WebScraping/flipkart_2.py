import bs4
import urllib.request as url

for n in range(1,6):
    print(f"Scraping Page No : {n}")
    path = f"https://www.flipkart.com/search?q=APPle%20IPHonE%2015&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={n}"

    response = url.urlopen(path)  # making HTTPRequest
    page = bs4.BeautifulSoup(response)

    title = page.find("div", {"class" : "_4rR01T"})
    print(title.text)

    price = page.find("div", {"class" : "_30jeq3 _1_WHN1"})
    print(price.text)

    titleList = page.find_all("div", {"class" : "_4rR01T"})
    priceList = page.find_all("div", {"class" : "_30jeq3 _1_WHN1"})

    for i in range(len(titleList)):
        print(titleList[i].text)
        print(priceList[i].text)
        print("*" * 50)
    print("=" * 50)
