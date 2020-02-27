import re

def mac_normalization(current_mac_address, symbol):
    if symbol == '.':
        return symbol.join([current_mac_address[i:i+4] for i in range(0, len(current_mac_address), 4)])
    return symbol.join(a + b for a, b in zip(current_mac_address[::2], current_mac_address[1::2]))

def main(current_mac_address, mac_address_format):

    current_mac_address = re.sub(r'\W+', '', current_mac_address)

    dict_mac_formats = {
        'mac_address_pure': '',
        'mac_address_dot': '.',
        'mac_address_colon': ':',
        'mac_address_dash': '-'
    }

    if len(current_mac_address) == 12:
        symbol = dict_mac_formats[mac_address_format]
        print(mac_normalization(current_mac_address, symbol))
        result = True
    else:
        print('not enough or too many characters or invalid format')
        result = False

    return result


if __name__ == '__main__':
    """
    ccef.4870.c081
    cc-ef-48-70-c0-81
    cc:ef:48:70:c0:81
    ccef4870c081   
    """
    current_mac_address = 'cc:ef:48:70:c0:84'
    mac_address_format = 'mac_address_pure'
    #mac_address_format = 'mac_address_colon'
    #mac_address_format = 'mac_address_dash'
    #mac_address_format = 'mac_address_pure'
    print(main(current_mac_address, mac_address_format))
