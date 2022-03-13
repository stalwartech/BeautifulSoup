#https://www.dictionary.com/browse/brilliant
#<span class="one-click-content css-nnyc96 e1q3nk1v1">shining brightly; sparkling; glittering; lustrous: <span class="luna-example italic">the brilliant lights of the city.</span></span>
from bs4 import BeautifulSoup
import requests
try:
    word= input("Enter a keyword to search: ")
    king = requests.get("https://www.dictionary.com/browse/"+word)
    data1 = BeautifulSoup(king.text, "html.parser")
    span_tag = data1.find("span",{"class": 'one-click-content css-nnyc96 e1q3nk1v1'})
    #print(span_tag)
    data2 = span_tag
    data3 = data2.contents
    print(data3[0])
except:
    print("Invalid search or failed internet connection")