import hmac
import hashlib

def calc_mac(used_key, message):
    used_key = bytes(used_key, "utf-8")
    message = bytes(message, "utf-8")

    messageHmac = hmac.new(used_key, message, hashlib.sha256)
    return messageHmac.hexdigest()