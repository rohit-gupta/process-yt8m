import requests
import sys
from tqdm import tqdm
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

base_url = "https://data.yt8m.org/2/j/i/<chunk>/<id>.js"
data_file = "yt8m_1percent_validate.txt"

data_with_ytids = open("yt8m_1percent_validate_ids.txt", "w")

with open(data_file, "r") as f:
        data = [x.strip() for x in f.readlines()]

for vid in tqdm(data):
        yt8m_id = vid.split(",")[0]
        req_url = base_url.replace("<chunk>", yt8m_id[:2]).replace("<id>", yt8m_id)
        r = requests.get(req_url, verify=False)

        try:
                ytid = r.text[:-3].split(",")[1][1:]
                print(ytid + "," + vid, file=data_with_ytids)
        except Exception:
                pass
