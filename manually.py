from browser import browser
import json

OFFSET = 955

if __name__ == "__main__":
    with open("data.json", "r") as f:
        data = json.loads(f.read())
    br = browser("https...")
    br.create_Host(data[OFFSET])


