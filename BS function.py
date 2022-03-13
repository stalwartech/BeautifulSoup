file = """<span class="wr-value--temperature--c">36°</span>

<div class="wr-day__weather-type-description wr-js-day-content-weather-type-description wr-day__content__weather-type-description--opaque" style="display:block" aria-hidden="true">Sunny and a gentle breeze</div>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=1">
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta http-equiv="cleartype" content="on">
    <link rel="dns-prefetch" href="https://ssl.bbc.co.uk/">
    <link rel="dns-prefetch" href="http://sa.bbc.co.uk/">
    <link rel="dns-prefetch" href="http://ichef-1.bbci.co.uk/">
    <link rel="dns-prefetch" href="http://ichef.bbci.co.uk/">
</head>"""

from bs4 import BeautifulSoup
baby = BeautifulSoup(file, "html.parser")
head_tag= baby.head
#print(head_tag)
print(head_tag.contents) # It prints eveyrthing inside the headtag
for i in head_tag.children:
    print(i) #This print all the direct tag behind the head_tag
for p in head_tag.descendants:
    print(p) #This print all the content in the file and also all what is inside the file separately