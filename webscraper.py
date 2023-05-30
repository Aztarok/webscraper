import requests
from bs4 import BeautifulSoup
import pandas as pd

# site_map = "https://danbooru.donmai.us/sitemap.xml?sitemap=posts"
site_map = "https://danbooru.donmai.us/posts.sitemap?limit=10000&tags=id%3A0..10000"
response = requests.get(site_map)

xml = response.text

soup = BeautifulSoup(xml, "xml")
site_maps = []
for loc in soup.find_all("loc"):
    url = loc.text
    site_maps.append(url)

print(site_maps)

# def get_clinic_name(clinic_id):
#     url = f"https://{clinic_id}.portal.athenahealth.com/"
#     response = requests.get(url)
#     html = response.text
#     soup = BeautifulSoup(html, "html.parser")
#     clinic_name = soup.find_all("h1")[-1].text.strip()
#     return clinic_name


# start = 12690
# end = 12700

# master_list = []

# for clinic_id in range(start, end):
#     data_dict = {}
#     data_dict["clinic_id"] = clinic_id
#     data_dict["clinic_name"] = get_clinic_name(clinic_id)
#     if data_dict["clinic_name"] != "Payment Confirmation" and data_dict["clinic_name"] != "Sorry, we can't find that practice. Make sure you typed the right address.":
#         master_list.append(data_dict)
#     print(clinic_id)

# df = pd.DataFrame(master_list)
# df.to_csv("clinic_data.csv", index=False)
