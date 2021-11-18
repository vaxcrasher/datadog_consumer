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

def get_value(endpoint):
    logger.info("Calling " + endpoint)
    response = requests.get(endpoint) 
    if (response.status_code == 200):
       logger.info("Name: " + str(response.status_code) + " " + response.text)
    elif (response.status_code == 404):
        logger.error(endpoint + " returns 404")
    else:
       logger.warn("Name: " + str(response.status_code) + " " + response.text)

# Set up loop to keep making calls
runLoop = True
counter = 1
while runLoop: 
    # determine which call to make
    thingToTry = random.randrange(0,200)
    if thingToTry <50:
        get_value("http://localhost:8080/name")
    elif thingToTry >50 and thingToTry <= 100:
        get_value("http://localhost:8080/word")
    elif thingToTry > 100 and thingToTry <= 150:
        get_value("http://localhost:8080/sentence")
    else:
        get_value("http://localhost:8080/paragraph")

    # sleep for a small amount of time
    # sleepSeconds = random.randrange(0,5)
    # time.sleep(sleepSeconds)
    counter += 1

    # testing only - stop after 50
    if counter > 100:
        runLoop = False
