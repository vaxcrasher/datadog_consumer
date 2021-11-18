import requests
import time
import random
import logging
import os

# Logging setup
scriptPath = os.path.realpath(__file__)
logFile = os.path.dirname(scriptPath) + "/logs/consumer.log"

# create logger with 'consumer_application'
logger = logging.getLogger('consumer.py')
logger.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
fh = logging.FileHandler(logFile)
fh.setLevel(logging.DEBUG)

# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

logger.info("Consumer application started!")

# Set up loop to keep making calls
runLoop = True
counter = 1
while runLoop: 
    # determine which call to make
    thingToTry = random.randrange(0,100)
    if thingToTry <50:
        response = requests.get("http://localhost:8080/name")
        print("Name: " + str(response.status_code) + " " + response.text)
    elif thingToTry >50 and thingToTry <= 100:
        response = requests.get("http://localhost:8080/word")
        print("Word: " + str(response.status_code) + " " + response.text)

    # sleep for a small amount of time
    # sleepSeconds = random.randrange(0,5)
    # time.sleep(sleepSeconds)
    counter += 1

    # testing only - stop after 50
    if counter > 100:
        runLoop = False
