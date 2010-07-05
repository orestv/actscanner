import urllib, os, sys;

VERDICT, ORDER, AWARD = range(3)

def get_list_url(type, page):
    if type==VERDICT:
        return    '''http://www8.city-adm.lviv.ua/pool/info/doclmr_1.nsf/(RishenniaWeb)?OpenView&Start=%s'''    % str(page*30+1)
