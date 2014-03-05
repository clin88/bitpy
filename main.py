from itertools import chain
import bencode
import requests
from requests import RequestException
import hashlib

def get_tracker_peers(url, metainfo):
    params = {
        "info_hash": hashlib.sha1(bencode.bencode(metainfo['info'])).digest(),
        "peer_id": "JEFF-123456789012356",
        "left": get_left(metainfo),
    }

    response = bencode.bdecode(requests.get(url, params=params).content)
    return get_peerlist(response)

def get_peerlist(response):
    decoded_dec_peer = map(ord, response['peers'])
    peer_list = []
    for indx in range(0, len(decoded_dec_peer), 6):
        port = (decoded_dec_peer[indx+4] * 256) + (decoded_dec_peer[indx+5])
        ip_str = '{ip[0]}.{ip[1]}.{ip[2]}.{ip[3]}:{port}'.format(ip=decoded_dec_peer[indx:indx+4], port=port)
        peer_list.append(ip_str)
    return peer_list

def get_left(metainfo):
    sum = 0
    for file in metainfo['info']['files']:
        sum += file['length']

    return sum

def trackerlist(metainfo):
    yield metainfo['announce']
    for tracker in chain(*metainfo['announce-list']):
        yield tracker


def get_peers(metainfo):
    peers = []
    for tracker in trackerlist(metainfo):
        try:
            peers.extend(get_tracker_peers(tracker, metainfo))
        except RequestException, e:
            continue

    return peers

def main():
    with open("test2.torrent", 'rb') as inpf:
        metainfo = bencode.bdecode(inpf.read())

    peers = get_peers(metainfo)

# parse peer list for ip address and port in function getPeerAddr

if __name__ == "__main__":
    main()
