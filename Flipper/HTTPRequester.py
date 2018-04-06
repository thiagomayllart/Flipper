import re
import urllib2
import base64
from base64 import b64encode, b64decode

requests_file = None
arr = None
file_string = None


def set_file(file_location):
    global requests_file, file_string
    requests_file = open(file_location, "r")
    file_string = requests_file.read()
    requests_file.close()


def get_key():
    global requests_file, arr, file_string
    file_string_aux = file_string
    data = file_string_aux.replace('\n', '!!!')
    arr = data.split('@@@@')
    print "Original Key: " + arr[1]
    decoded = arr[1].decode('base64')
    return decoded


def HTTP_request(key, block, position):
    arr_aux = arr
    arr_aux[1] = key.encode('base64').replace('\n', '')
    new_req = ''.join(arr_aux)
    s = new_req
    start = 'request base64='
    end = '/request'
    method = ''
    ax = s
    result = ax.split(start)[-1]
    result = result.split(end)[0]

    start = 'CDATA['
    end = ']]><'
    method = ''
    result = result.split(start)[-1]
    result = result.split(end)[0]

    start = '<url><![CDATA['
    end = ']]></url>'
    path = s.split(start)[-1].split(end)[0]

    raw_header, data = result.split('!!!!!!')
    lines = raw_header.split('!!!')
    if 'POST' in lines[0]:
        method = 'POST'
    else:
        if 'GET' in lines[0]:
            method = 'GET'

    headers = {}

    i = 1
    while i < len(lines):
        info = lines[i].split(': ', 1)
        if 'Content-Length' not in info[0]:
            headers.update({info[0]: info[1]})
        i = i + 1

    the_page = ''
    code = ''

    try:
        if method == 'POST':
            req = urllib2.Request(path, data=data, headers=headers)
            response = urllib2.urlopen(req)
            the_page = response.read()
            code = response.getcode()

        if method == 'GET':
            req = urllib2.Request(path, headers=headers)
            response = urllib2.urlopen(req)
            the_page = response.read()
            code = response.getcode()

        print ("%s, %s, %s, %s, %s", arr_aux[1], block, position, code, len(the_page))

    except urllib2.HTTPError as err:
        print err

