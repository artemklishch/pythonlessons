from bs4 import BeautifulSoup
import urllib.request


class Parser:
    row_html = ''
    html = ''
    results = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = urllib.request.urlopen(self.url)
        self.row_html = req.read()
        self.html = BeautifulSoup(self.row_html, "html.parser")

    def parsing(self):
        news = self.html.find_all("li", class_="liga-news-item")
        for item in news:
            title = item.find('span', class_="d-block").get_text(strip=True)
            desc = item.find('span', class_="name-dop").get_text(strip=True)
            href = item.a.get('href')
            self.results.append({
                'title': title,
                'desc': desc,
                'href': href
            })

    def save(self):
        # f = open('news.txt', 'w', encoding='utf-8')
        # i = 1
        # for item in self.results:
        #     f.write(
        #         f'New № {i}\n\nName: {item["title"]}\nDescription: {item["desc"]}\nLink: {item["href"]}\n\n***********\n\n')
        #     i += 1
        # f.close()
        with open(self.path, 'w', encoding='utf-8') as f:
            i = 1
            for item in self.results:
                f.write(
                    f'New № {i}\n\nName: {item["title"]}\nDescription: {item["desc"]}\nLink: {item["href"]}\n\n***********\n\n')
                i += 1

    def run(self):
        self.get_html()
        self.parsing()
        self.save()
