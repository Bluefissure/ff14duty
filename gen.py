import requests
import re
import csv
import json
from bs4 import BeautifulSoup

questIdSet = {}

def load_web_duties():
    r = requests.get("https://ff14.org/duty/")
    bs = BeautifulSoup(r.text, "html.parser")
    duty_list = bs.find('ul', {'class': 'duty-list'})
    for duty in duty_list.children:
        if not duty or not duty.a:
            continue
        href = duty.a.attrs.get('href')
        m = re.match(r"\/duty\/(\d+)\.htm", href)
        if not m:
            continue
        duty_id = int(m.group(1))
        questIdSet[duty_id] = duty.text.strip()
    print(questIdSet.keys())

def load_from_territory():
    r = requests.get("https://raw.githubusercontent.com/thewakingsands/ffxiv-datamining-cn/master/TerritoryType.csv")
    cr = csv.reader(r.text.splitlines(), delimiter=',')
    my_list = list(cr)
    zoneIdMap = {}
    print("{")
    for row in my_list:
        if row[0].isdigit() and int(row[11]) > 0:
            print("  {}: {},\t//{}".format(
                int(row[0]), int(row[11]), questIdSet.get(int(row[11]), "")))
    print("}")


if __name__ == "__main__":
    load_web_duties()
    load_from_territory()