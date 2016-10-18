

#the emails associated with all of your microsoft accounts and their respective passwords
emails = [('email1@example1.com', 'password1'), ('email2@example2.com', 'password2')]

from time import sleep

#will need to install the package splinter for python 3 for this to work
from splinter import Browser

for email in emails:
    with Browser('chrome') as b:
        # stuff using the b
        # b = Browser('chrome')
        b.visit('https://login.live.com')
        # b.find_by_text('Email or phone')
        b.fill("loginfmt", email[0])
        b.fill("passwd", email[1])
        b.find_by_id('idSIButton9').click()
        #bunch of random things that the script will search to collect your rewards, these are arbitrary and can be anything really
        arr = ["matlab", "things", "nike shoes", "kickstarter", "android development", "apple iphone", "mountain range", "appalachian plateau", "how to implement a map in python", "cython documentation", "champion.gg league", "columbia computer science", "how to make a paper airplane", "edx courses", "computer science college rankings", "longest increasing subsequence algorithm", "yardwork", "skyrim", "no man's sky", "undertale", "ocaml", "jane street",  'reddit', 'query', 'string', 'imgur', 'array', ' python list',
     'words', 'excluded definition','Teach me how to twerk', 'vine videos', 'deep ocean', 'giraffes', 'atlantis']
        print(len(arr))
        for i in range(len(arr)):
    	    sleep(5)
    	    b.visit('https://www.bing.com')
    	    b.fill("q", arr[i])
    	    b.find_by_id('sb_form_go').click()










