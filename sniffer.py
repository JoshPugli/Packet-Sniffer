import socket
import struct
import textwrap


# loop that runs as long as program runs, sit and wait for packet to come in, then extract information
def main():
    connection = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

    while True:
        raw_data, address = connection.recvfrom(65536)
        dest_mac, src_mac, eth_proto = ethernet_f(raw_data)  # take data pass to function, store in variables
        print('\nEthernet Frame:')
        print('Destination: {}, Source: {}, Protocol: {}'.format(dest_mac, src_mac, eth_proto))


# unpack data, give information
# gives destination, source, ethernet type, actual payload
def ethernet_f(data):
    dest_mac, src_mac, proto = struct.unpack('! 6s 6s H', data[:14])  # read first 14 bytes of data
    return get_mac_addr(dest_mac), get_mac_addr(src_mac), socket.htons(proto), data[14:]


# mac address has format AB:CD:EF:GH:IJ:KL
def get_mac_addr(bytes_address):
    bytes_str = map('{:02x}'.format, bytes_address)     # format each chunk to two decimal places
    mac_address = ':'.join(bytes_str).upper()   # take each of the two chunks, make sure that they're uppercase,
    # join with colon
    return mac_address

main()