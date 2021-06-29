import requests
URL='https://en.wikipedia.org/wiki/History_of_Mexico'

page=requests.get(URL)
# print(page.content)

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')


result1 = soup.find('div', class_="mw-parser-output")
# print(result1.prettify())



# print(result2)


def get_citations_needed_count():
    result2 = result1.find_all('sup', class_='noprint Inline-Template Template-Fact')       
    array=[]
    for res in result2:
        result3= res.find('span')

        array.append(result3.text) 

        print('here is a result',result3)
        length=len(array)
        print(array)
        return f'Number of citation {length}'

print(get_citations_needed_count())

    

def get_citations_needed_report():
    txt=[]

    parghraphs = result1.find_all('p')
    for p in parghraphs:
        p2 = p.find('span',string=lambda text: 'citation needed' in text)
        if p2 :
            txt.append(p.text.strip())

    # for a in txt:
    #     print(a)
    #     print('-'*20)

get_citations_needed_report()



