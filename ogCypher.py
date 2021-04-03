import re


# Colors
class Color:
    RED = '\033[31m'
    GREEN = '\033[92m'
    BOLD = '\033[1m'
    RESET = '\033[0m'
    YELLOW = '\033[93m'


def banner():
    # Banner

    print('')
    print(Color.GREEN + '░█████╗░░██████╗░  ░█████╗░██╗░░░██╗██████╗░██╗░░██╗███████╗██████╗░')
    print(Color.GREEN + '██╔══██╗██╔════╝░  ██╔══██╗╚██╗░██╔╝██╔══██╗██║░░██║██╔════╝██╔══██╗')
    print(Color.GREEN + '██║░░██║██║░░██╗░  ██║░░╚═╝░╚████╔╝░██████╔╝███████║█████╗░░██████╔╝')
    print(Color.GREEN + '██║░░██║██║░░╚██╗  ██║░░██╗░░╚██╔╝░░██╔═══╝░██╔══██║██╔══╝░░██╔══██╗')
    print(Color.GREEN + '╚█████╔╝╚██████╔╝  ╚█████╔╝░░░██║░░░██║░░░░░██║░░██║███████╗██║░░██║')
    print(Color.GREEN + '░╚════╝░░╚═════╝░  ░╚════╝░░░░╚═╝░░░╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝')
    print('')


def main():
    # Input

    method = str.lower(input(Color.GREEN + Color.BOLD + '[#]' + Color.RESET + ' Do you want to decrypt or encrypt (D/E): '))

    if method == 'e':
        string_to_encrypt = input(Color.GREEN + Color.BOLD + '[#]' + Color.RESET + ' Enter a string to encrypt: ')
        binary = ''.join(format(x, 'b').zfill(8) for x in bytearray(string_to_encrypt, 'utf-8'))
        rev = binary[::-1]
        rep0 = rev.replace('0', '420')
        rep1 = rep0.replace('1', '69')
        print(Color.YELLOW + Color.BOLD + '[#]' + Color.RESET + ' Output: ')
        print('')
        print(Color.YELLOW + rep1)
        print('')
    elif method == 'd':
        string_to_decrypt = input(Color.GREEN + Color.BOLD + '[#]' + Color.RESET + ' Enter a string to decrypt: ')
        rep1 = string_to_decrypt.replace('69', '1')
        rep0 = rep1.replace('420', '0')
        rev = rep0[::-1]

        validation = bool(re.match("^[01 ]+$", rev))

        if validation is True:
            def bitstring_to_bytes(s):
                v = int(s, 2)
                b = bytearray()
                while v:
                    b.append(v & 0xff)
                    v >>= 8
                return bytes(b[::-1])

            bytes_array = bitstring_to_bytes(rev)
            output = bytes_array.decode("utf-8")
            print(Color.RED + Color.YELLOW + '[#]' + Color.RESET + ' Output: ')
            print('')
            print(Color.YELLOW + output)
            print('')
        else:
            print(Color.RED + Color.BOLD + '[#]' + Color.RESET + ' Invalid input')
    else:
        print(Color.RED + Color.BOLD + '[#]' + Color.RESET + ' Invalid method')


try:
    banner()
    while True:
        main()
except KeyboardInterrupt:
    print('')
    print(Color.GREEN + Color.BOLD + '[#]' + Color.RESET + ' Bye')
    print('')
    pass
