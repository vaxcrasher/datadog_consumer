import requests
import time
import random
import logging
import os

# Set up which server to call
# url = "http://localhost:8080/"
url = "http://100.21.163.215/"

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
       logger.warning("Name: " + str(response.status_code) + " " + response.text)

# Set up loop to keep making calls
runLoop = True
counter = 1
while runLoop: 
    # determine which call to make
    thingToTry = random.randrange(0,210)
    if thingToTry <50:
        get_value(url + "name")
    elif thingToTry >50 and thingToTry <= 100:
        get_value(url + "word")
    elif thingToTry > 100 and thingToTry <= 150:
        get_value(url + "sentence")
    elif thingToTry > 150 and thingToTry <= 200:
        get_value(url + "paragraph")
    else: 
        get_value(url + "badendpoint")

    # sleep for a small amount of time 5% of the time
    sleepTrigger = random.randrange(1,100)
    if (sleepTrigger < 5):
        logger.warning("Sleeping for " + str(sleepTrigger) + " seconds")
        time.sleep(sleepTrigger)
    counter += 1
