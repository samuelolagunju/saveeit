import os
import requests
import datetime

def main():
    print("Please enter the URL of the Reddit video you want to download.")

    redditURL = input(">> ")[:-1]+".json"

    request = requests.get(redditURL, headers = { "User-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0" })
    
    jsonData = request.json()[0]

    main.vidURL = jsonData["data"]["children"][0]["data"]["secure_media"]["reddit_video"]["fallback_url"] # Gets the video URL

    main.nameOfVid = jsonData["data"]["children"][0]["data"]["name"] + datetime.datetime.now().strftime("%Y-%m-%dT%H-%M-%S") + "vid"
    main.nameOfAudio = jsonData["data"]["children"][0]["data"]["name"] + datetime.datetime.now().strftime("%Y-%m-%dT%H-%M-%S") + "audio"

    print("")

    print("Got video URL!")

    print("")

    main.soundURL = "https://v.redd.it/" + main.vidURL.split("/")[3] + "/DASH_audio.mp4"

    print("Got sound URL!")

    print("")

def downloadMP4():
    with open(main.nameOfVid + ".mp4", "wb") as w:
        vidDL = requests.get(main.vidURL, stream = True)
        w.write(vidDL.content)

    print("Downloaded mp4!")

    print("")

def downloadMP3():
    with open(main.nameOfAudio + ".mp3", "wb") as w:
        audioDL = requests.get(main.soundURL, stream = True)
        w.write(audioDL.content)

    print("Downloaded mp3!")
