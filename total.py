from browser import browser
import json

if __name__ == "__main__":
    br = browser("http://10.1.255.50/centreon/main.php?p=60201")
    try:
        with open("urls.txt","r") as f:
            result = f.read().replace("{","").replace("}","").split(", ")
    except:
        result = br.get_all_Services_Urls(115)
    print(len(result))
    with open("urls2.txt", "w") as f:
        f.write(str(result))
    dics = br.get_Services_Information([("aaa", l) for l in result])
    with open("data.json", "w") as f:
        f.write(json.dumps(dics))

    print(result)
    print(len(result))
