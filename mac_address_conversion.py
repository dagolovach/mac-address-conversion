import re
import sys


def mac_conversion(normalized_mac_address, symbol):
    if symbol == '.':
        return symbol.join([normalized_mac_address[i:i + 4] for i in range(0, len(normalized_mac_address), 4)])
    return symbol.join(a + b for a, b in zip(normalized_mac_address[::2], normalized_mac_address[1::2]))


def main(current_mac_address, mac_address_format):
    normalized_mac_address = re.sub(r'\W+', '', current_mac_address)

    dict_mac_formats = {
        'none': '',
        'dot': '.',
        'colon': ':',
        'dash': '-'
    }
    symbol = dict_mac_formats.get(mac_address_format, 'Invalid format')
    if symbol == 'Invalid format':
        return 'Invalid format. Should be none | dot |  colon | dash '

    if len(normalized_mac_address) == 12:
        symbol = dict_mac_formats.get(mac_address_format, 'Invalid format')
        return mac_conversion(normalized_mac_address, symbol)
    else:
        return "Invalid format. Should be 01-23-45-67-89-AB | 01:23:45:67:89:AB | 0123456789AB | 0123.4567.89AB or " \
               "any combination "

if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SyntaxError("Insufficient arguments.")
    print(main(sys.argv[1], sys.argv[2]))
