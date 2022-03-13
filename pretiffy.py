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
king = BeautifulSoup(file,"html.parser")
print(king.prettify())
print(king.find_all("link"))
print(king.find_all("meta"))
array = king.find_all("link")
print(array[2])