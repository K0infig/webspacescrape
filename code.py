from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

START_URL = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"

browser = webdriver.Chrome("/Users/sreelakshmi/Downloads/chromedriver")
browser.get(START_URL)
time.sleep(10)

def scrape():

    header = ["name", "light_years_from_earth", "planet_mass", "stellar magnitude", "Discovery_date"]
    planet_data =[]

    soup = BeautifulSoup(browser.page_source,"html.parser")

    for ul_tag in soup.find_all("ul", attrs = {"class","exoplanet"}):
        li_tags = ul_tag.find_all("li")
        templist = []
        

        for index, li_tag in enumerate(li_tags):
            if index ==0:
                templist.append(li_tag.find_all("a")[0].contents[0])

            else:
                try:
                    templist.append(li_tag.contents[0])

                except:
                    templist.append("")

            planet_data.append(templist)

        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()


    with open("space.csv", "w") as f:
        csvwrite =csv.writer(f)
        csvwrite.writerow(header)
        csvwrite.writerows(planet_data)


scrape()



    

    


