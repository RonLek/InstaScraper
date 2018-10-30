#Script that scrapes images off Instagram and saves it on your machine
import requests, time, shutil
from selenium import webdriver
def instaScrapper(url):
    #Opens Instagram URL
    browser.get(url)
    
    #Scroll down until all images are loaded on the screen
    SCROLL_PAUSE_TIME = 5

    # Get scroll height
    last_height = browser.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    #Get all img elements    
    imgelems = browser.find_elements_by_class_name('FFVAD')

    i=0
    for imgelem in imgelems:
        imglink = imgelem.get_attribute('src')
        response = requests.get(imglink, stream = True)
        with open('C:\\InstaScraper\\img'+str(i)+'.png','wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        i+=1

#Opens the browser (Make sure you have the Chrome webdriver executable listed in your Environment Variable Path
        
browser = webdriver.Chrome(executable_path=r'C:\\Users\\hp\\Chrome WebDriver\\chromedriver.exe') #Specify your own Chrome Driver Path here
time.sleep(5)
browser.get('https:www.instagram.com')
time.sleep(30)
#Enter username password after Instagram opens.
instaScrapper('Enter_Custom_Instagram_URL')
    
