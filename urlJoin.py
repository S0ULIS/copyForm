with open("urls2.txt","r") as f:
    result = set(f.read().replace("{","").replace("}","").split(", "))

with open("urls2Jose.txt","r") as f:
    result.update(set(f.read().replace("{","").replace("}","").split(", ")))

with open("urls2.txt", "w") as f:
            f.write(str(result))
