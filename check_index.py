import json

OFFSET = 374

if __name__ == "__main__":
    with open("data.json", "r") as f:
        data = json.loads(f.read())
    print(data[OFFSET])


    
    
