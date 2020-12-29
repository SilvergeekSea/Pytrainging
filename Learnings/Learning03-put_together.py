"""
    Put what we learned
    so far together.
"""
import urllib.request as req
import os
#get your proxy server url details using below command
req.getproxies()

#user your credentials and url to authenticate

os.environ['http_proxy'] = "http://schen33:@proxy.cmltd.net.au:8080"
os.environ['https_proxy'] = "https://schen33:@proxy.cmltd.net.au:8080"
from urllib.request import urlopen
story = urlopen('http://sixty-north.com/c/t.txt')
story_words = []
for line in story:
    line_words = line.decode('utf8').split()
    for word in line_words:
        story_words.append(word)

story.close()
print (f'storty_words is {story_words}')
print (story)
print story_words






