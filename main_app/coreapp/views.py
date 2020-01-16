from django.shortcuts import render
from bs4 import BeautifulSoup as soup
import requests
import re
from .models import Information


def basicScrap(request):
    def main():
        url_list = ["https://www.flipkart.com/signoraware-best-steel-lunch-box"\
                "-blue-500ml-350ml-200ml-tumbler-370ml-3-containers-box/p/itm"\
                "fedq3gcpfutwv?pid=LBXFED4W8HSF9SPD&otracker=wishlist&lid=LST"\
                "LBXFED4W8HSF9SPD8EFHDU&fm=organic&iid=24db7969-8ff2-4574-8550"\
                "-dfed03f05549.LBXFED4W8HSF9SPD.PRODUCTSUMMARY&ppt=hp&ppn=hp&s"\
                "sid=hm69tsuogg0000001569056937359"]
        url_list.append("https://www.flipkart.com/himalaya-anti-hair-fall-sham"\
                "poo/p/itmf3xfxdmywkwhs?pid=SMPEUHHFZYBXXHGB&lid=LSTSMPEUHHFZY"\
                "BXXHGBNMGARX&marketplace=FLIPKART&sattr[]=quantity&st=quantity")
        url_list.append("https://www.flipkart.com/sparx-sfg-529/p/itmfafydk6kw"\
            "wurs?pid=SFFE5VWZMMGKQDGE&lid=LSTSFFE5VWZMMGKQDGEGDB3LS&marketpl"\
            "ace=FLIPKART&sattr[]=color&sattr[]=size&st=size")

        for my_url in url_list:
            """Iterating through each url"""
            uClient = requests.get(my_url)
            if uClient.status_code == 200:
                page_html = uClient.text

                page_soup = soup(page_html, "html.parser")

                containers = page_soup.find("div", {"class": "_1HmYoV _35HD7C col-8-12"})
                name = containers.find("span", {"class": "_35KyD6"})
                pName = name.text
                print(pName)

                price = containers.find("div", {"class": "_1vC4OE _3qQ9m1"})
                boxPrice = price.text.strip()
                pPrice = int(''.join(filter(str.isdigit, boxPrice)))
                print(pPrice)
                minPrice = pPrice

                get_name = Information.objects.filter(productName=pName)

                """If data not in the record then it'll create new object otherwise it'll update the
                   existing object with new price"""
                if get_name.count()==0:
                    information_instance = Information.objects.create(
                                            productName=pName, productPrice=pPrice,
                                            minPrice=minPrice, maxP=pPrice)
                else:
                    minPrice = get_name[0].minPrice
                    maxP = get_name[0].maxP
                    if minPrice > pPrice:
                        minPrice=pPrice
                    if maxP < pPrice:
                        maxP=pPrice
                    information_instance = Information.objects.filter(productName=pName).update(
                                            productPrice=pPrice,
                                            minPrice=minPrice, maxP=maxP)
                    print(minPrice)


            else:
                print('Not Found.')

    main()
    details = Information.objects.all()
    detailsDict = {'detailsDict' : details}
    return render(request, 'coreapp/index.html', context=detailsDict)
