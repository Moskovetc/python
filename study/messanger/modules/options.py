def check_ipv4_address(ipv4_address):
    ipv4_address = ipv4_address.split('.')
    check = True
    if len(ipv4_address) == 4:
        for octet in ipv4_address:
            if 1 > int(octet) > 254:
                check = False
    else:
        check = False
    return check


def get_options(args):
    try:
        if args[1] == '-a':
            try:
                if check_ipv4_address(args[2]):
                    ipv4_address = args[2]
                else:
                    print('IP address is incorrect')
            except IndexError:
                ipv4_address = '127.0.0.1'
                print('IP address not input, default IP 127.0.0.1')
    except IndexError:
        ipv4_address = '127.0.0.1'
        print('IP address not input, default IP 127.0.0.1')

    try:
        if args[3] == '-p':
            try:
                if 0 < int(args[4]) < 2**16:
                    port = int(args[4])
                else:
                    port = 7777
                    print('Port is incorrect, default порт 7777')
            except IndexError:
                port = 7777
                print('Port not input, default порт 7777')
    except IndexError:
        port = 7777
        print('Port not input, default порт 7777')

    return ipv4_address, port