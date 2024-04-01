html_doc = """
<html>
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
		<title>Yazılım Kodlama</title>
	</head>
	<body>
        <h1 id="header">
        Python
            </h1>
        <h1 id="header">
        Css
            </h1>
            <h1 id="header">
        js
            </h1>
            <a href="https://www.btkakademi.gov.tr/portal1/course/player"</a>
            <a href="https://www.btkakademi.gov.tr/portal2/course/player"</a>
            <a href="https://www.btkakademi.gov.tr/portal3/course/player"</a>

	</body>
</html>
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, "html.parser")

result = soup.prettify()  # düzenleme yapar html de

result = soup.title
result = soup.body
result = soup.title.name
result = soup.title.string
result = soup.h2
result = soup.h1

result = soup.find_all("h1")
result = soup.find_all("h1")[1]
result = soup.h1.findChildren()
result = soup.h1.findNextSibling().findNextSibling()
result = soup.h1.findPrevious()
result = soup.find_all("a")
for link in result:
    print(link.get("href"))

print(result)
