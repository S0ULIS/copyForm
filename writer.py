from browser import browser
import json

OFFSET = 49

if __name__ == "__main__":
    with open("data.json", "r") as f:
        data = json.loads(f.read())
    
    data = data[OFFSET:]
    print("[+] Migrando {} items".format(len(data)))
    br = browser("http://10.1.255.50/centreon/")
    br.create_Services(data)
    print("[+] Migración completada")