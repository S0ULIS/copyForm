from typing import NamedTuple
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import time
from collections import namedtuple
from selenium.webdriver.support.select import Select

Input = namedtuple("Input","name,type") # type in ["checkBox","text","radio"]
Option = namedtuple("Option","value,text")


inInputs = [
    Input("host_name","text"),
    Input("dupSvTplAssoc","radio"),
    Input("host_notifOpts[u]","checkBox"),
    Input("nagios_server_id","select"),
    Input("pasar_pagina","click")
]

outInputs = [
    Input("host_name","text"),
    Input("dupSvTplAssoc[dupSvTplAssoc]","radio"),
    Input("host_notifOpts[u]","checkBox")
]


def pause():
    print("[+] Pausa ...")
    input("[-] Pulse Enter para continuar: ")

wait = lambda t: time.sleep(t)
check_pattern = lambda x: "&o=c&host_id=" in x


class browser:
    def __init__(self,url,page_offset = 0) -> None:
        self.page_offset = page_offset
        self.base = url
        self.driver = webdriver.Chrome('./chromedriver.exe')
        self.driver.get(url)
        self.urls = []
        pause()
    
    def get_Urls(self):
        elements = self.driver.find_elements_by_css_selector("td.ListColLeft a")
        for element in elements:
            if check_pattern(element.get_attribute('href')):
                #print(element.get_attribute('href'))
                if not element.get_attribute('href') in self.urls:
                    self.urls.append(element.get_attribute('href'))
        
        return self.urls[self.page_offset:]

    def get_Input_Value(self,name,type):
        if type == "text":
            result = self.driver.find_element_by_xpath("//input[@name='{}']".format(name)).get_attribute("value")
        elif type == "radio":
            radiosBtns = self.driver.find_elements_by_xpath("//input[contains(@name,'{}')]".format(name.replace("[","\[").replace("]","\]")))
            result = [radio for radio in radiosBtns if radio.get_attribute("checked")=="true"][0].get_attribute("value")
        elif type == "checkBox":
            result = self.driver.find_element_by_name(name).is_selected()
        elif type == "autocomplete":
            select = Select(self.driver.find_element_by_name(name))
            result = select.all_selected_options
        elif type == "select":
            select = Select(self.driver.find_element_by_name(name))
            result = select.first_selected_option
        elif type == "click":
            self.driver.find_element_by_id(name).click
            result = True

        if name=="host_name":
            print("[+] Leyendo {}".format(result))
        print(result)
        #pause()
        return result

    def set_Input_Value(self,name,type,value):
        try:
            if type=="text": # value constains text
                self.driver.find_element_by_name(name).sendKeys(value)
            elif type=="radio": # value contains the value of the one that was previously checked
                radiosBtns = self.driver.find_elements_by_name(name)
                [radio for radio in radiosBtns if radio.get_attribute("value")==value][0].click()
            elif type=="checkBox": # value True if checked
                if value:
                    self.driver.find_element_by_name(name).click()
            elif type=="autocomplete":
                self.driver.find_element_by_id(name).click()
                self.driver.find_element_by_xpath("//input[@class='select2-search__field']").sendKeys(value + Keys.ENTER)
            return True

        except:
            return False
    def create_Host(self,data):
        self.driver.get(self.base+"main.php?p=60101&o=a")
        for oinp in outInputs:
            self.set_Input_Value(oinp.name,oinp.type,data[oinp.name])
    
    def create_Hosts(self,data):
        for host in data:
            self.create_Host(host)

    def get_Host_Information(self,url):
        values = {}
        self.driver.get(url)
        wait(7)
        for inp in inInputs:
            values[inp.name] = self.get_Input_Value(inp.name,inp.type)
        return values

    def get_Hosts_Information(self):
        self.get_Urls()
        result = []
        for url in self.urls:
            result.append(self.get_Host_Information(url))
            wait(5)
        return result
