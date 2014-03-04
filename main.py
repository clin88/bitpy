from itertools import chain
import bencode
import requests
from requests import RequestException
import hashlib

def get_tracker_response(url, metainfo):
    params = {
        "info_hash": hashlib.sha1(bencode.bencode(metainfo['info'])).digest(),
        "peer_id": "JEFF-123456789012356",
        "left": get_left(metainfo),
    }
    print url
    return bencode.bdecode(requests.get(url, params=params).content)

def get_left(metainfo):
    sum = 0
    for file in metainfo['info']['files']:
        sum += file['length']

    return sum

def trackerlist(metainfo):
    yield metainfo['announce']
    for tracker in chain(*metainfo['announce-list']):
        yield tracker

def getPeerAddr(response):
    decoded_dec_peer = map(ord, response['peers'])


def main():
    with open("test2.torrent", 'rb') as inpf:
        metainfo = bencode.bdecode(inpf.read())

    for tracker in trackerlist(metainfo):
        try:
            response = get_tracker_response(tracker, metainfo)
            print response
        except RequestException, e:
            continue

    #addr_list = getPeerAddr(response)

if __name__ == "__main__":
    main()
