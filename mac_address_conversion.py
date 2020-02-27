import re
import sys


def mac_normalization(current_mac_address, symbol):
    if symbol == '.':
        return symbol.join([current_mac_address[i:i + 4] for i in range(0, len(current_mac_address), 4)])
    return symbol.join(a + b for a, b in zip(current_mac_address[::2], current_mac_address[1::2]))


def main(current_mac_address, mac_address_format):
    current_mac_address = re.sub(r'\W+', '', current_mac_address)

    dict_mac_formats = {
        'none': '',
        'dot': '.',
        'colon': ':',
        'dash': '-'
    }
    symbol = dict_mac_formats.get(mac_address_format, 'Invalid format')
    if symbol == 'Invalid format':
        print('Invalid format. Should be none | dot |  colon | dash ')
        return

    if len(current_mac_address) == 12:
        symbol = dict_mac_formats.get(mac_address_format, 'Invalid format')
        print(mac_normalization(current_mac_address, symbol))
    else:
        print('Invalid format. Should be 01-23-45-67-89-AB | 01:23:45:67:89:AB | 0123456789AB | 0123.4567.89AB\n or '
              'any combination')

    return


if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SyntaxError("Insufficient arguments.")
    main(sys.argv[1], sys.argv[2])
