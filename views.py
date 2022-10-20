from flask import Blueprint, render_template
from mobalytics import Mobalytics_API

views = Blueprint(__name__, "views")
api = Mobalytics_API()


@views.route("/")
def home():
    championsList = api.getChampionsList()
    print(len(championsList))
    numOfRows = int(len(championsList) / 6)

    return render_template(
        "index.html", championsList=championsList, champsPerRow=6, numOfRows=numOfRows
    )


@views.route("/<championName>")
def getChampionProfile(championName):
    return render_template("index.html", champion=championName)
