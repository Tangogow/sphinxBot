#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

import mechanize
import random
import time

import config, utils
from input import *

def sendForm(br):
    res = br.submit()
    if config.debugHTML:
        print(res.read()) #  you'll see the thanks you page after submitting the survey

def setValues(form):
    ############# ANSWERS GOES THERE ###############
    name = ["Jim", "Mike", "Ellen", "Donald", "Jeffrey", "Mia", "James", "John", "Mary", "Jennifer", "Michael", "David", "Richard", "Ashley", "Karen", "Sarah", "Thomas", "Sandra", "Mark", "Paul", "Amanda"]
    console = ["GameBoy", "GameBoy Color", "GameBoy Advance", "Nintendo DS", "Nintendo 3DS", "Nintendo Switch"]
    pokemon = ["Charmander", "Bulbasaur", "Squirtle", "Pikachu", "Eevee"]

    form['952323510'] = checkbox(2) # Sex ? (Male or Female)
    form['1974977126'] = number(15, 40) # What's your age ? (Choose between 15 and 40)
    form['1400739879'] = text(1, 1, name) # What's your name ? (Choose one name in the list above)
    form['8553127596'] = checkbox(3, True, True) # How did you know about pokemon ? (Friends, TV, internet) (multiple choice allowed)
    form['1553507596'] = checkbox(2) # Do you play pokemon ? (Yes or No)
    if form['1553507596'] == ['1']: # If yes, then the following questions are enabled:
        form['1008124807'] = checkbox(5) # How much do you like Pokemon ? (Scale on "love it", "like it", "okay i guess", "not much", "hate it")
        form['8123712391'] = number(0, 5) # How much do you like Pokemon ? (Number between 0 and 5)
        form['123Z823939'] = graduated(0, 10) # How much do you like Pokemon ? (Graduation between 0 and 10)
        form['148964210'] = checkbox(2) # Do you remember each generation ? (Yes or No)
        if form['148964210'] == ['1']: # If yes:
            form['1440599398'] = number(1, 8) # What is your favorite generation of pokemons ? (Choose between 1 and 8)
            form['1491175067'] = ranking(8, True, True, 2, 7) # In which order do you rank the 8 different generations ? Between 2 and 7 answers awaited.
        form['581849239'] = text(1, 6, console) # On what console where you playing ? (Choose between 1 and 6 console in the list above, can be multiple)
        form['402629921'] = text(3, 3, pokemon) # Your 3 favorite pokemon ? (Choose exactly 3 from live above)
        form['452628921'] = text(0, 5, pokemon) # What pokemon do you hate ? (Choose between 0 (none) and 5 (all of them) from list above)
        form['131266989'] = number(0, 3000) # How much have you spend on pokemon games in € ? (Between 0€ and 3000€)
    # Done
    ####################
    return form

def openForm(br):
    ''' Need to submit a form on the link URL to get some token before being redirected on the survey pages.
        Otherwise you'll get an "Invalid request" error
    '''
    res = br.open(config.url)
    if config.debugHTML:
        '''shows the invisible page with tokens in hidden input tags that your broswer is dealing with'''
        print(res.read())
    br.select_form("form")
    res = br.submit()
    if config.debugHTML:
        print(res.read()) # show the survey page
    return br

def randUserAgent():
    ''' To fake the origin device, otherwise will look like it's all done with a PC
    '''
    user_agent = random.randrange(0, 2)
    if user_agent == 1: # Smartphone
        user_agent = 'Linux; Android 7.1.2; AFTMM Build/NS6265; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36'
    else: # PC
        user_agent = 'Mozilla/5.0'
    #elif:
    #    user_agent = 'Android 7.1.2' # Linux tablet
    return user_agent


def init():
    br = mechanize.Browser()
    br.set_handle_robots(False) # will return 403 if True
    br.set_handle_refresh(False)

    br.addheaders = [
        ('Accept', '*/*'),
        ('Accept-Encoding', 'gzip, deflate, br'),
        ('Cache-Control', 'max-age=0'),
        ('Connection', 'keep-alive'),
        ('Content-Type', 'application/x-www-form-urlencoded'),
        ('Host', 'sphinx-campus.com'),
        ('Origin', 'https://sphinx-campus.com'),
        ('Referer', config.url),
        ('Sec-Fetch-Dest', 'none'),
        ('Sec-Fetch-Mode', 'navigate'),
        ('Sec-Fetch-Site', 'same-origin'),
        ('Upgrade-Insecure-Requests', '1'),
        ('User-agent', randUserAgent()),
        ]
    return br

def answerSurvey():
    br = init()
    br = openForm(br)
    br.form = list(br.forms())[0] # main form got no name
    if config.debug:
        print(br.form)
    br.form = setValues(br.form)
    if not config.debug:
        utils.delay(config.answerMin, config.answerMax) # delay for filling up the survey
    sendForm(br)

def main():
    startTime = time.time()
    print('*** SPHINX BOT ACTIVE ***')
    print('Survey URL: ' + config.url)
    if config.debug:
        config.loopMax = 1
    utils.delay(2, 3)
    for i, key in enumerate(range(0, config.loopMax)): # delay between each surveyor
        print("Filling survey #" + str(i + 1))
        answerSurvey()
        if not config.debug:
            utils.delay(config.surveyMin, config.surveyMax, minutes=True)
    print('Done in ' + str(round(time.time() - startTime)) + ' secs')

if __name__ == "__main__":
    main()
