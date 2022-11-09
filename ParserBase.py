
class ParserBase:

    import requests
    from lxml import etree as et

    parserName = ""

    def __init__(self, parserName):
        self.parserName = parserName

    def parse(self, data):
        url = data['url']
        selector = data['selector']
        name = data['name']

        print("Parsing " + name + "(" + url + ") with " + self.parserName + " parser")

        HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
        response = self.requests.get(url, headers = HEADERS)
        dom = self.et.HTML(response.content)

        try:
            price = dom.xpath(selector)[0]
            return str(price)
        except Exception as e:
            price = 'Not Available'
            return None
