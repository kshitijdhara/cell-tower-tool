import ijson


with open("cell.json") as f:
        obj = ijson.items(f, "item")
        for o in obj:
            print(o['lon'])