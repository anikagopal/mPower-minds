from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

def crawl_page(main_url,page):
    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
    req = Request(main_url , headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read()
    soup = BeautifulSoup(html, "html.parser")
    if page=="sat_page":
       new_url = soup.find("div",{"class":"cb-band-panel-content"})
    elif page=="psat_page":
        new_url = soup.find("section",{"class":"d8-wysiwyg cb-margin-top-72"})
    else:
        new_url = soup.find("table",{"class":"table"})
    htmlFile = open("C:\\Users\\dhira\\Documents\\AWS\\Science_Project\\Website_Project\\"+page+".html", "w")
    htmlFile.write(str(new_url))
    htmlFile.close()

sat_page_url="https://satsuite.collegeboard.org/sat"

crawl_page(sat_page_url,"sat_page")

psat_page_url ="https://satsuite.collegeboard.org/psat-nmsqt/test-dates"

crawl_page(psat_page_url,"psat_page")

act_page_url="https://www.act.org/content/act/en/products-and-services/the-act/registration.html"

crawl_page(act_page_url,"act_page")



   


    
    

