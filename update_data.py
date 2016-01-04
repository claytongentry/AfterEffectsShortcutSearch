# https://helpx.adobe.com/after-effects/using/keyboard-shortcuts-reference.html#time_navigation_keyboard_shortcuts

from bs4 import BeautifulSoup
import urllib2
import csv
from shortcuts import COMMANDS_FILE

# Encoding = UTF-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

if __name__=="__main__":

    try:
        AFX_page = "https://helpx.adobe.com/after-effects/using/keyboard-shortcuts-reference.html#time_navigation_keyboard_shortcuts"
        print "Grabbing command data from AFX website..."
        html = urllib2.urlopen(AFX_page)
        soup = BeautifulSoup(html, "html.parser")
        print "Formatting and writing to csv..."
        with open(COMMANDS_FILE, "w") as f:
            command_writer = csv.writer(f)
            boxes = soup.findAll('div', {'class': 'parbase table section'})
            for box in boxes:
                table = box.find('tbody')
                rows = table.findAll('tr')
                for row in rows:
                    data = row.findAll('td')
                    arr = []
                    for element in data:
                        el = None
                        try:
                            el = element.find('p').text
                        except:
                            el = element.text
                        arr.append(el)
                    command_writer.writerow(arr)
        print 'Done!'
    except:
        print "Something's not quite right. Call Clayton.\n"
