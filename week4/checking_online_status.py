import winsound
from urllib import request
from time import sleep
import winsound
# a url for a website that we expect to be available
url = 'http://www.google.com'

seconds_between_sleep_check = 3

while True:
    print('Checking if you are online...')
    try:
        # opens the url. This will error/fail if you are not online/connected to wifi or ethernet
        request.urlopen(url).read()
        print('You seem to be online')
        #  adds a beeping sound. Only works on windows
        winsound.MessageBeep()
    except:
        print('You are not online')

    print(f'Sleeping for {seconds_between_sleep_check} seconds.....')
    print()
    sleep(seconds_between_sleep_check)

    break
