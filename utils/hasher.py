import base64


def encode_url(url):
    return base64.urlsafe_b64encode(url.encode('utf-8')).decode('utf-8').rstrip('=')



def decode_url(encoded_url):
    padding_needed = 4 - (len(encoded_url) % 4)
    encoded_url += "=" * padding_needed
    return base64.urlsafe_b64decode(encoded_url.encode('utf-8')).decode('utf-8')
