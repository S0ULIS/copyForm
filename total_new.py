from browser import browser
import json

if __name__ == "__main__":
    br = browser("http://10.1.255.50/centreon/main.php?p=60201")
    try:
        with open("urls2.txt","r") as f:
            result = f.read().replace("{","").replace("}","").split(", ")
    except:
        result = br.get_all_new_Services_Urls(0,52)
        with open("urls2.txt", "w") as f:
            f.write(str(result))
    print(len(result))
    
    result = result[:988]
    dics = br.get_new_Services_Information(result)
    with open("data.json", "w") as f:
        f.write(json.dumps(dics))
    print("[+] Finalizado con éxito")
