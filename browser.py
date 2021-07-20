from socket import MsgFlag
from typing import NamedTuple
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import re
import time
from collections import namedtuple
from selenium.webdriver.support.select import Select

Input = namedtuple("Input","name,type") # type in ["checkBox","text","radio","select","autocomplete","click"]
Option = namedtuple("Option","value,text")

DELAY = 4 # Seconds (s)

differents = {
    "service_hPars-t[]" : "service_hPars[]",
    "service_cs-t[]" : "service_cs[]",
    "service_cgs-t[]" : "service_cgs[]"
    
}
SERVICE_INPUTS = [
    Input("service_description", "text"),
    Input("service_template_model_stm_id","select"),
    Input("service_is_volatile[service_is_volatile]","radio"),
    Input("timeperiod_tp_id","select"),
    Input("command_command_id","select"),
    Input("ARG1","text"),
    Input("ARG2","text"),
    Input("ARG3","text"),
    Input("ARG4","text"),
    Input("ARG5","text"),
    Input("ARG6","text"),
    Input("ARG7","text"),
    Input("ARG8","text"),
    Input("ARG9","text"),
    Input("ARG10","text"),
    Input("service_max_check_attempts", "text"),
    Input("service_normal_check_interval", "text"),
    Input("service_retry_check_interval", "text"),
    Input("service_active_checks_enabled[service_active_checks_enabled]","radio"),
    Input("service_passive_checks_enabled[service_passive_checks_enabled]", "radio"),
    Input("service_notifications_enabled[service_notifications_enabled]", "radio"),
    Input("service_cs-t[]","autocomplete"),
    Input("service_cgs-t[]", "autocomplete"),
    Input("service_notification_interval", "text"),
    Input("timeperiod_tp_id2", "select"),
    Input("service_notifOpts[w]","checkBox"),
    Input("service_notifOpts[u]","checkBox"),
    Input("service_notifOpts[c]","checkBox"),
    Input("service_notifOpts[r]","checkBox"),
    Input("service_notifOpts[f]","checkBox"),
    Input("service_notifOpts[s]","checkBox"),
    Input("service_first_notification_delay","text"),

    Input("li#c2 a","click"),
    Input("service_hPars-t[]","autocomplete"),
    Input("mnftr","select"),
    Input("service_traps-t[]","autocomplete"),
    Input("service_obsess_over_service[service_obsess_over_service]","radio"),

    Input("li#c3 a","click"),
    Input("service_check_freshness[service_check_freshness]", "radio"),
    Input("service_freshness_threshold","text"),
    Input("service_flap_detection_enabled[service_flap_detection_enabled]","radio"),
    Input("service_low_flap_threshold","text"),
    Input("service_high_flap_threshold","text"),
    Input("service_retain_status_information[service_retain_status_information]","radio"),
    Input("service_retain_nonstatus_information[service_retain_nonstatus_information]","radio"),
    Input("service_stalOpts[o]","checkBox"),
    Input("service_stalOpts[w]","checkBox"),
    Input("service_stalOpts[u]","checkBox"),
    Input("service_stalOpts[c]","checkBox"),
    Input("service_event_handler_enabled[service_event_handler_enabled]","radio"),
    Input("command_command_id2","select"),
    Input("command_command_id_arg2","text"),
    Input("li#c4 a","click"),
    Input("graph_id","select"),
    Input("service_categories-t[]","autocomplete"),
    Input("esi_notes_url","text"),
    Input("esi_notes","text"),
    Input("esi_action_url","text"),
    Input("esi_icon_image","select"),
    Input("esi_icon_image_alt","text"),
    Input("criticality_id","select"),
    Input("service_activate[service_activate]","radio"),
    Input("service_comment","textArea")

]

SERVICE_OUTPUTS = [
    Input("service_description", "text"),
    Input("service_template_model_stm_id","select"),
    Input("service_is_volatile[service_is_volatile]","radio"),
    Input("timeperiod_tp_id","select"),
    Input("command_command_id","select"),
    Input("ARG1","text"),
    Input("ARG2","text"),
    Input("ARG3","text"),
    Input("ARG4","text"),
    Input("ARG5","text"),
    Input("ARG6","text"),
    Input("ARG7","text"),
    Input("ARG8","text"),
    Input("ARG9","text"),
    Input("ARG10","text"),
    Input("service_hPars-t[]","autocomplete"),
    Input("service_max_check_attempts", "text"),
    Input("service_normal_check_interval", "text"),
    Input("service_retry_check_interval", "text"),
    Input("service_active_checks_enabled[service_active_checks_enabled]","radio"),
    Input("service_passive_checks_enabled[service_passive_checks_enabled]", "radio"),
    Input("li#c2 a","click"),

    Input("service_notifications_enabled[service_notifications_enabled]", "radio"),
    Input("service_cs-t[]","autocomplete"),
    Input("service_cgs-t[]", "autocomplete"),
    Input("service_notification_interval", "text"),
    Input("timeperiod_tp_id2", "select"),
    Input("service_notifOpts[w]","checkBox"),
    Input("service_notifOpts[u]","checkBox"),
    Input("service_notifOpts[c]","checkBox"),
    Input("service_notifOpts[r]","checkBox"),
    Input("service_notifOpts[f]","checkBox"),
    Input("service_notifOpts[s]","checkBox"),
    Input("service_first_notification_delay","text"),

    Input("li#c3 a","click"),
    Input("service_traps-t[]","autocomplete"),
    Input("service_obsess_over_service[service_obsess_over_service]","radio"),

    Input("li#c4 a","click"),
    Input("service_check_freshness[service_check_freshness]", "radio"),
    Input("service_freshness_threshold","text"),
    Input("service_flap_detection_enabled[service_flap_detection_enabled]","radio"),
    Input("service_low_flap_threshold","text"),
    Input("service_high_flap_threshold","text"),
    Input("service_retain_status_information[service_retain_status_information]","radio"),
    Input("service_retain_nonstatus_information[service_retain_nonstatus_information]","radio"),
    Input("service_stalOpts[o]","checkBox"),
    Input("service_stalOpts[w]","checkBox"),
    Input("service_stalOpts[u]","checkBox"),
    Input("service_stalOpts[c]","checkBox"),
    Input("service_event_handler_enabled[service_event_handler_enabled]","radio"),
    Input("command_command_id2","select"),
    Input("command_command_id_arg2","text"),
    
    Input("li#c5 a","click"),
    Input("graph_id","select"),
    Input("service_categories-t[]","autocomplete"),
    Input("esi_notes_url","text"),
    Input("esi_notes","text"),
    Input("esi_action_url","text"),
    Input("esi_icon_image_alt","text"),
    Input("service_activate[service_activate]","radio"),
    Input("service_comment","textArea"),
    Input("submitA","click")
]

HOST_INPUTS = [
    Input("host_name","text"),
    Input("dupSvTplAssoc[dupSvTplAssoc]","radio"),
    Input("host_notifOpts[u]","checkBox"),
    Input("nagios_server_id","select"),
    Input("host_cgs-t[]","autocomplete")
]

HOST_OUTPUTS = [
    Input("host_name","text"),
    Input("dupSvTplAssoc","radio"),
    Input("host_notifOpts[u]","checkBox"),
    Input("nagios_server_id","select")
]


def pause():
    print("[+] Pausa ...")
    input("[-] Pulse Enter para continuar: ")

wait = lambda t: time.sleep(t)
check_host_pattern = lambda x: "&o=c&host_id=" in x
check_service_pattern = lambda x: "p=60201&o=c&service_id=" in x


class browser:
    def __init__(self,url,item_offset = 0,page_number = 0) -> None:
        self.item_offset = item_offset
        self.page_number = page_number
        self.base = url
        self.driver = webdriver.Chrome('./chromedriver.exe')
        self.driver.get(url)
        self.urls = []
        pause()
    
    def get_Hosts_Urls(self):
        elements = self.driver.find_elements_by_css_selector("td.ListColLeft a")
        for element in elements:
            if check_host_pattern(element.get_attribute('href')):
                #print(element.get_attribute('href'))
                if not element.get_attribute('href') in self.urls:
                    self.urls.append(element.get_attribute('href'))
        
        return self.urls[self.item_offset:]

    def get_Services_Urls(self):
        last_host = ""
        self.driver.get("http://boreal.dipusevilla.es/boreal/main.php?p=60201&num={}&limit=30&poller=&template=0&search=&type=&o=&search_type_service=1&search_type_host=1&status=&hostgroups=0".format(self.page_number))
        wait(DELAY)
        table = self.driver.find_elements_by_css_selector(".ListTable tr")
        for tr in table:
            children = tr.find_elements_by_css_selector("td.ListColLeft a")
            for a in children:
                if check_host_pattern(a.get_attribute('href')):
                    if not a.text in [""," "]:
                        last_host = a.text
                elif check_service_pattern(a.get_attribute('href')):
                    self.urls.append((last_host,a.get_attribute('href')))
                    print((last_host,a.get_attribute('href')))
        self.urls = self.urls[self.item_offset:]
        return self.urls

    def get_Input_Value(self,name,type):
        try:
            if type == "text":
                result = None
                if(len(self.driver.find_elements_by_xpath("//input[@name='{}']".format(name)))>0):
                    result = self.driver.find_element_by_xpath("//input[@name='{}']".format(name)).get_attribute("value")
            elif type == "textArea":
                result = self.driver.find_element_by_xpath("//textarea[@name='{}']".format(name)).get_attribute("value")
            elif type == "radio":
                radiosBtns = self.driver.find_elements_by_name(name)
                result = [radio for radio in radiosBtns if radio.get_attribute("checked")=="true"][0].get_attribute("value")
            elif type == "checkBox":
                result = self.driver.find_element_by_name(name).is_selected()
            elif type == "autocomplete":
                select = Select(self.driver.find_element_by_name(name))
                result = [[element.text for element in select.options]]
            elif type == "select":
                select = Select(self.driver.find_element_by_xpath("//select[@name='{}']".format(name)))
                result = select.first_selected_option.text
            elif type == "click":
                self.driver.find_element_by_css_selector(name).click()
                wait(0.5)
                result = True

            if name=="service_description":
                print("[+] Leyendo {}".format(result))
            #pause()
            return result
        except:
            print("[-] Error lectura")
            pause()

    def set_Input_Value(self,name,type,value):
        try:
            nname = differents[name] if name in differents else name # nname = new name
            if type=="text" and value!="": # value constains text
                element = WebDriverWait(self.driver,10).until(lambda d: d.find_element_by_css_selector("input[name='{}']".format(nname)))
                #element = self.driver.find_element_by_css_selector("input[name='{}']".format(nname))
                element.send_keys(value)
            elif type=="radio": # value contains the value of the one that was previously checked
                radioBtns = self.driver.find_elements_by_name(nname)
                element = [r for r in radioBtns if r.get_attribute("value")==value][0]
                self.driver.execute_script("document.getElementById('{}').click()".format(element.get_attribute("id")))
            elif type=="checkBox": # value True if checked
                if value:
                    element = self.driver.find_element_by_name(nname)
                    self.driver.execute_script("document.getElementById('{}').click()".format(element.get_attribute("id")))
            elif type == "select":
                
                select = WebDriverWait(self.driver,10).until(lambda d: d.find_element_by_name(nname))
                parent = self.driver.execute_script("return arguments[0].parentNode;",select)
                parent.find_element_by_class_name("select2-container").click()

                search_bar = WebDriverWait(self.driver,10).until(lambda d: d.find_elements_by_class_name("select2-container--open"))
                search_bar_input = [sb for sb in search_bar if len(sb.find_elements_by_tag_name("input"))>0][0].find_element_by_tag_name("input")
                search_bar_input.send_keys(value)
                wait(1)
                search_bar_input.send_keys(Keys.ENTER)

            elif type=="autocomplete":
                value = value[0]
                if nname == "service_traps-t[]":
                    select = self.driver.find_element_by_id("service_traps")
                elif nname == "service_categories-t[]":
                    select = self.driver.find_element_by_id("service_categories")
                else:
                    select = WebDriverWait(self.driver,10).until(lambda d: d.find_element_by_name(nname))
                parent = self.driver.execute_script("return arguments[0].parentNode;",select)
                parent.find_element_by_class_name("select2-container").click()

                search_bar = WebDriverWait(self.driver,10).until(lambda d: d.find_elements_by_class_name("select2-container--open"))
                search_bar_input = [sb for sb in search_bar if len(sb.find_elements_by_tag_name("input"))>0][0].find_element_by_tag_name("input")
                for i in range(0,len(value)):
                    search_bar_input.send_keys(value[i])
                    wait(1)
                    search_bar_input.send_keys(Keys.ENTER)
                    if i <len(value)-1:
                        wait(1)
                        search_bar_input.send_keys("a")
                        wait(1)
                        search_bar_input.send_keys(Keys.BACKSPACE*(len(value[i])))

            elif type == "click":
                if "li#c" in nname:
                    index = nname[4]
                    self.driver.execute_script("javascript:montre('{}');".format(index))
                elif "submitA" == nname:
                    self.driver.execute_script("document.getElementsByName('submitA')[0].click();")
                    wait(DELAY)
                else:
                    self.driver.find_element_by_name(nname)
                wait(0.5)
                

            if name=="service_description":
                print("[+] P {} I {} Añadiendo {}".format(self.page_number,self.item_offset,value))

            return True

        except Exception as e:
            if not "ARG" in name:
                print(e)
                return False
            else:
                return True

    def create_Host(self,data):
        self.driver.get(self.base+"main.php?p=60101&o=a")
        wait(DELAY)
        for oinp in outInputs:
            self.set_Input_Value(oinp.name,oinp.type,data[oinp.name])
        self.item_offset+=1
            
    
    def create_Hosts(self,data):
        for host in data:
            self.create_Host(host)

    def get_Host_Information(self,url):
        values = {}
        self.driver.get(url)
        wait(DELAY)
        for inp in inInputs:
            values[inp.name] = self.get_Input_Value(inp.name,inp.type)
        return values

    def get_Hosts_Information(self):
        self.get_Urls()
        result = []
        for url in self.urls:
            result.append(self.get_Host_Information(url))
        return result

    def create_Service(self,data):
        self.driver.get(self.base+"main.php?p=60201&o=a")
        wait(DELAY)
        self.driver.switch_to.frame(self.driver.find_element_by_id("main-content"))
        for oinp in SERVICE_OUTPUTS:
            if not oinp.name in data and oinp.type == "click":
                result = self.set_Input_Value(oinp.name,oinp.type,None)
            else:
                result = self.set_Input_Value(oinp.name,oinp.type,data[oinp.name])
            if not result:
                print("[-] Fallo en name={}. Página {} item {} Servicio {}".format(oinp.name, self.page_number,self.item_offset,data["service_description"]))
                pause()
        self.item_offset+=1
    
    def create_Services(self,data):
        for service in data:
            self.create_Service(service)

    def get_Service_Information(self,url):
        values = {}
        self.driver.get(url)
        wait(DELAY)
        for inp in SERVICE_INPUTS:
            values[inp.name] = self.get_Input_Value(inp.name,inp.type)
        return values

    def get_Services_Information(self):
        self.get_Services_Urls()
        result = []
        for (host,url) in self.urls:
            service = self.get_Service_Information(url)
            service["host_name"] = host
            result.append(service)
        return result
    
    
    def next_host_page(self):
        self.page_number += 1
        self.item_offset = 0
        self.driver.get(self.base+"01&num={}&limit=30&poller=0&template=0&search=&type=&o=&search_type_service=1&search_type_host=1&hostgroup=0".format(self.page_number))
        wait(DELAY)
    
    def next_service_page(self):
        self.page_number += 1
        self.item_offset = 0
        self.driver.get("http://boreal.dipusevilla.es/boreal/main.php?p=60201&num={}&limit=30&poller=&template=0&search=&type=&o=&search_type_service=1&search_type_host=1&status=&hostgroups=0".format(self.page_number))
        wait(DELAY)

