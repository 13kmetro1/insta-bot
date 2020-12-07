import selenium
from selenium import webdriver as Fire
import time
driver = Fire.Firefox()
def login():
    driver.get("https://www.instagram.com")
    time.sleep(3)
    username = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
    username.clear()
    username.send_keys("9086555947")
    time.sleep(2)
    password = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
    password.clear()
    password.send_keys("13kmetro1")
    time.sleep(2)
    login = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div")
    login.click()
    time.sleep(4)
    try:
        posbutton = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button") #for save info button
        posbutton.click()
        time.sleep(3)
    except:
        print("There was no save info button")
    try:
        notifbutton = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]") #for notification button
        notifbutton.click()
        time.sleep(3)
    except:
        print("There was no notification button")
def likeall(accountname):
    searchbutton = driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
    searchbutton.send_keys(accountname)
    time.sleep(2)
    account = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[4]/div/a[1]') #finds first account in dropdown list
    account.click()
    time.sleep(4)
    pics = driver.find_elements_by_tag_name('a') #finds all clickable articles
    print(pics)
    time.sleep(2)
    pics[1].click() #clicks first picture

if __name__ == "__main__":
    login()
    likeall("jeff.metro")