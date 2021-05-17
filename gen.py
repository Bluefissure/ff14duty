import requests
import re
import csv
import json

def load_web_duties():
    r = requests.get("https://ff14.org/duty/")
    duties = re.findall(r"\/duty\/(\d+)\.htm", r.text)
    questIdSet = list(map(lambda x: int(x), duties))
    print(questIdSet)


def load_from_territory():
    r = requests.get("https://raw.githubusercontent.com/thewakingsands/ffxiv-datamining-cn/master/TerritoryType.csv")
    cr = csv.reader(r.text.splitlines(), delimiter=',')
    my_list = list(cr)
    zoneIdMap = {}
    print("{")
    for row in my_list:
        if row[0].isdigit() and int(row[11]) > 0:
            print("  {}: {},".format(int(row[0]), int(row[11])))
    print("}")


if __name__ == "__main__":
    load_web_duties()
    load_from_territory()