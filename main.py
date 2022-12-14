from requests import Session
from bs4 import BeautifulSoup as bs
from rich import print

dict_data = {"success":True,
    "message":None,
    "data":{"datetime":"",
        "latitude":"",
        "longitude":"",
        "magnitude":"",
        "depth":"",
        "region":"",
        "maps":""}}
# base url
url = "https://www.bmkg.go.id/gempabumi-terkini.html"
#headers
headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; TECNO W4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Mobile Safari/537.36"}
r = Session()
def main_function():
    response = r.get(url, headers=headers)
    soup = bs(response.text, "html.parser")
    find = soup.find_all("tr")
    data = find[1].text.splitlines()
    dict_data["data"]["datetime"] = data[2]
    dict_data["data"]["latitude"] = data[3]
    dict_data["data"]["longitude"] = data[4]
    dict_data["data"]["magnitude"] = data[5]
    dict_data["data"]["depth"] = data[6]
    dict_data["data"]["region"] = data[7]
    dict_data["data"]["maps"] = f"https://www.google.com/maps/place/{data[3]},{data[4]}"
    print(dict_data)
main_function()
