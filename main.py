import bencode
import requests
import hashlib

def getPeerList(metadata):
    url = 'announce-url?'
    info_hash = hashlib.sha1(bencode.bencode(metadata['info'])))
    info_hash_param = 'param={0}&'.format(info_hash.digest())
    peer_id
    port
    uploaded
    downloaded
    left
    compact
    no_peer_id
    event

def main():
    torrent = open(filename, 'r')
    metadata = bencode.bdecode(torrent)
    peer_list = getPeerList(metadata)
    lexer = TorrentLexer(torrent_input)
    info_hash
