from browser import browser

if __name__=="__main__":
    br1 = browser("http://boreal.dipusevilla.es/boreal/main.php?p=601")
    data = br1.get_Hosts_Information()
    print(data)
    br2 = browser("http://10.1.255.50/centreon/")
