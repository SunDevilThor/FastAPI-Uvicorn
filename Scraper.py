# Scraper file for website
# Quotes To Scrape

from requests_html import HTMLSession

class Scraper(): 

    def scrape_data(self, tag):
        url = f'https://quotes.toscrape.com/tag/{tag}'
        s = HTMLSession()
        r = s.get(url)
        print(r.status_code)

        quotes_list = []

        quotes = r.html.find('div.quote')

        for q in quotes: 
            item = {
                'text': q.find('span.text', first=True).text.strip(), 
                'author': q.find('small.author', first=True).text.strip(), 
            }
            print(item)
            quotes_list.append(item)
        
        return quotes_list


quotes = Scraper()
quotes.scrape_data('life')