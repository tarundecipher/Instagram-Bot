from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import tkinter
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import random
window = tkinter.Tk()

window.geometry('500x200')
chromedriver = 'C:\\Users\\Hp\Desktop\\chromedriver.exe'
 
# options = webdriver.ChromeOptions()
# options.add_argument('headless')
# options.add_argument('window-size=1200x600') # optional
 
# driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)
driver = webdriver.Chrome(executable_path=chromedriver)

driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
driver.implicitly_wait(20)
def login():
   
    driver.find_element_by_xpath("//input[@name='username']").send_keys(username.get())
    driver.find_element_by_xpath("//input[@name='password']").send_keys(password.get())
    driver.find_element_by_xpath("//body//div[4]").click()
    b1.config(state='disabled')
    
def hash():
    driver.get('http://www.instagram.com/explore/tags/'+hashtag.get()+'/')
  
    driver.find_element_by_xpath("//body/div[@id='react-root']/section[contains(@class,'_9eogI E3X2T')]/main[contains(@class,'o64aR')]/article[contains(@class,'KC1QD')]/div[contains(@class,'EZdmt')]/div/div/div[1]/div[1]/a[1]/div[1]").click()
    r = int(num.get())
    for i in range(r):
        driver.find_element_by_xpath("//span[contains(@class,'glyphsSpriteHeart__outline__24__grey_9 u-__7')]").click()
        time.sleep(random.randint(30,60))
        driver.find_elements_by_xpath("//a[contains(@class,'HBoOv coreSpriteRightPaginationArrow')]")[0].click()
        
def follow_user():
    driver.get('http://www.instagram.com/'+follow_username.get()+'/')
    driver.find_elements_by_xpath("//main[contains(@class,'o64aR')]//li[2]//a[1]")[0].click()
    r = int(num.get())
    for i in range(r):
        time.sleep(random.randint(30,60))
        driver.find_elements_by_class_name("sqdOP")[i].click()


def follow_commentors():
   
    #url to the photograph
    r = int(num.get())
    url = follow_commentors.get()
    driver.get(url)
    for i in range(50):
        driver.find_elements_by_xpath("//span[contains(@class,'glyphsSpriteCircle_add__outline__24__grey_9 u-__7')]")[0].click()
    names = driver.find_elements_by_class_name("TlrDj")
    name = []
    for i in range(len(driver.find_elements_by_class_name("TlrDj"))):
        name.append(names[i].text)
    
    for i in range(r):
        time.sleep(random.randint(30,60))
        driver.get('https://www.instagram.com/'+str(name[i])+'/')
        driver.find_elements_by_xpath("//div[contains(@class,'nZSzR')]//button[contains(@class,'')][contains(text(),'Follow')]")[0].click()
            
def unfollow_users():
    driver.get('https://www.instagram.com/'+username.get()+'/')
    driver.find_element_by_xpath("//main[contains(@class,'o64aR')]//li[3]//a[1]").click()
    
    names = driver.find_elements_by_class_name('FPmhX')
    name = []
    for i in range(len(names)):
        name.append(names[i].text)
    for i in range(len(name)):
        time.sleep(random.randint(30,60))
        driver.get('https://www.instagram.com/'+str(name[i])+'/')
        driver.find_element_by_xpath("//button[contains(text(),'Following')]").click()
        driver.find_element_by_xpath("//button[contains(text(),'Unfollow')]").click()
    unfollow_users()



window.title('InstaBot(Decipher)')
b1 = tkinter.Button(window, text ="Log in", command = login)
b2 = tkinter.Button(window, text ="Start Liking", command = hash)
b3 = tkinter.Button(window,text = "Start Following",command = follow_user)
b4 = tkinter.Button(window,text = 'follow commentors',command = follow_commentors)
b5 = tkinter.Button(window,text = 'unfollow users',command = unfollow_users)
password = tkinter.Entry(show='*')
username = tkinter.Entry()
hashtag = tkinter.Entry()
follow_username = tkinter.Entry()
follow_commentors = tkinter.Entry()
num = tkinter.Spinbox(window, from_=0, to=500)

follow_commentors.grid(row=6,column=5,pady=2)
follow_username.grid(row=5,column=5,pady=2)
num.grid(row =4,column=5,pady=2)
l1 = tkinter.Label(window,text ='Username')
l1.grid(row=1,column=0)
l3 = tkinter.Label(window,text ='Hashtag')
l3.grid(row=4,column=0)
l4 = tkinter.Label(window,text='Follow Username')
l4.grid(row = 5,column = 4,pady=2)
l2 = tkinter.Label(window,text ='Password')
l2.grid(row=2,column=0)
l5 = tkinter.Label(window,text='Post Url')
l5.grid(row = 6,column = 4,pady=2)
username.grid(row=1,column=4,pady=2)
password.grid(row=2,column=4,pady=2)
hashtag.grid(row=4,column=4,pady=2)
b1.grid(row=3,column=4,pady=2)
b2.grid(row=4,column=6,pady=2)
b3.grid(row=5,column=6,pady=2)
b4.grid(row=6,column=6,pady=2)
b5.grid(row=7,column=6,pady=2)


window.mainloop()