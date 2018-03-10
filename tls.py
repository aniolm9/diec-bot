import urllib.request
import ssl

# There is a bug for TLSv1 and DIEC currently only supports it.
def fix_tls():
    https_TLSv1_handler = urllib.request.HTTPSHandler(context=ssl.SSLContext(ssl.PROTOCOL_TLSv1))
    opener = urllib.request.build_opener(https_TLSv1_handler)
    urllib.request.install_opener(opener)