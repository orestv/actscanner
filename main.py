import gtk, pygtk;
import window;
import os, sys;
import threading;
import urllib;
import func;

class Thread(threading.Thread):
    def __init__(self, url):
        self._url = url
        threading.Thread.__init__(self)

    def run(self):
        handle = urllib.urlopen(self._url)
        for line in handle.readlines():
            print unicode(line, 'cp1251')


if __name__ == '__main__':
    print func.get_list_url(func.VERDICT, 0)
    #Thread('http://www8.city-adm.lviv.ua/pool/info/doclmr_1.nsf/(RishenniaWeb)?OpenView').start()
