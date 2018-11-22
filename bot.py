#!/usr/bin/env python

from pyvirtualdisplay import Display
from selenium import webdriver
import bottle
from bottle import route, run

app = bottle.default_app()

@route('/', 'GET')
def pendentes():
    display = Display(visible=0, size=(800, 600))
    display.start()

    # now Firefox will run in a virtual display. 
    # you will not see the browser.
    browser = webdriver.Firefox()
    browser.get('http://www.google.com')
    print(browser.title)
    browser.quit()

    display.stop()

    return 'Oi!'

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
