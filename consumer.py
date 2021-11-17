import requests
import time
import random

# Set up loop to keep making calls
runLoop = True
counter = 1
while runLoop: 
    # determine which call to make
    thingToTry = random.randrange(0,100)
    if thingToTry <50:
        response = requests.get("http://localhost:8081/name")
        print("Name: " + str(response.status_code) + " " + response.text)
    elif thingToTry >50 and thingToTry <= 100:
        response = requests.get("http://localhost:8081/word")
        print("Word: " + str(response.status_code) + " " + response.text)

    # sleep for a small amount of time
    sleepSeconds = random.randrange(0,5)
    time.sleep(sleepSeconds)
    counter += 1

    # testing only - stop after 50
    if counter > 50:
        runLoop = False
