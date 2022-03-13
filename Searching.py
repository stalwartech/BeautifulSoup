from bs4 import BeautifulSoup
import requests
try:
    # https://www.timeanddate.com/weather/nigeria/kaduna
    location = input("Kindly Enter your location: ")
    url = "https://www.weather-atlas.com/en/nigeria/" + location
    print(url)
    link = requests.get(url)
    data = BeautifulSoup(link.text, "html.parser")
    span_tag= data.span
    data2 = data.find("span", {"class":"text-primary fs-3"})
    #print(data2)
    final1 = data2.contents
    #print(final1)
    temp = final1[0]
    print("The temperature in ", location, " is currently ", temp)
except:
    print("Kindly check your internet connection or an invalid search")


