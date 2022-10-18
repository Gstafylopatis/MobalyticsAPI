from bs4 import BeautifulSoup
import requests
import sys


class Mobalytics_API:
    def __init__(self):
        self.mobalytics_url = "https://app.mobalytics.gg/lol/champions"
        self.mobalytics_icons_url = (
            "https://cdn.mobalytics.gg/assets/lol/images/dd/champions/icons/"
        )

    def getChampionsList(self):
        r = requests.get(self.mobalytics_url)

        if r.status_code != 200:
            print("Error speaking to mobalytics")
            sys.exit(0)

        soup = BeautifulSoup(r.content, "html.parser").find(
            "div", "m-1u0kasc"
        )  # This gets the div with the links to each champ

        champ_links = soup.find_all("a")  # Gives all links

        # Splits the link by the / delimeter and returns the champ's name thats in pos 3
        champsList = [link.get("href").split("/")[3] for link in champ_links]
        return champsList


api = Mobalytics_API()
print(api.getChampionsList())
