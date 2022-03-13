love = """<head>
<span class="wr-value--temperature--c">36°</span>

<div class="wr-day__weather block" aria-hidden="true">Sunny and a gentle breeze</div></head>
<body>
    <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=1">
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta http-equiv="cleartype" content="on">
    <link rel="dns-prefetch" href="https://ssl.bbc.co.uk/">
    <link rel="dns-prefetch" href="http://sa.bbc.co.uk/">
    <link rel="dns-prefetch" href="http://ichef-1.bbci.co.uk/">
    <link rel="dns-prefetch" href="http://ichef.bbci.co.uk/">
</body>"""

from bs4 import BeautifulSoup
police = BeautifulSoup(love, "html.parser")
#print(police)
police.prettify()
print(police.div)
print(police.find_all("link"))
array = police.find_all("link")
print(array[2])
print(police.body.href)