import hmac
import hashlib

def calc_mac(key, message):
    key = bytes(key, "utf-8")
    message = bytes(message, "utf-8")

    messageHmac = hmac.new(key, message, hashlib.sha256)
    return messageHmac.hexdigest()
