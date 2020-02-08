import pyperclip
from selenium import webdriver

class SearchBot():

    def __init__(self):
        
        self.driver = webdriver.Chrome('E:\PythonFiles\chromedriver_win32 79\chromedriver.exe')
    
    def google_search(self):

        self.driver.get("https://google.com")
        
        search_button = self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
        
        search_button.click()
        
        search_query = pyperclip.paste()
        
        search_button.send_keys(search_query)
        
        search_submit = self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
        
        search_submit.click()
 


def search():
    while True:
        old_search = pyperclip.paste()

        Qbot = SearchBot()
        Qbot.google_search()
        while True:
            newmaybe = pyperclip.paste()
            if newmaybe == old_search:
                continue
            elif newmaybe!=old_search:
                break
search()





