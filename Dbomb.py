#Encoded By Decoder_X

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode('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'))))
