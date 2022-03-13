file = """<head>
<title> "I am so much in love with programming" </title>
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
alabi = BeautifulSoup(file, "html.parser")
body_tag = alabi.body
head_tag = alabi.head
div_tag = alabi.div
link_tag = alabi.link
title_tag= alabi.title
#print(title_tag.string) # it print the string inside the title tags
final = title_tag.string.replace('"'," ")
#print(final)
blow = title_tag.parent
print(blow)
adenike = title_tag.string
print(adenike)