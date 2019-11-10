import argparse

def encoder(pscode):
    text = open(pscode).read()
    out = open(pscode[:pscode.index(".")] + ".bin", "w")
    txt = ""
    for i in text:
        txt += (bin(ord(i))[2:]+ ' ')
    out.write(txt[:-1])
    out.close()
    
def decoder(pscode):
    binary = open(pscode).read().split(" ")
    out = open(pscode[:pscode.index(".")] + ".p", "w")
    text = ""
    for i in binary:
        text += chr(int(i, base=2))
    out.write(text)
    out.close()
    
parser = argparse.ArgumentParser()
parser.add_argument("-e","--encode", metavar='FILE', help="Encode a ProtonScript program file.")
parser.add_argument("-d","--decode", metavar='FILE', help="Decode a ProtonScript program file.")
args = parser.parse_args()
    
if args.encode:
    filename = open(args.encode).read().split("\n") if args.encode else []
    encoder(args.encode)
    
if args.decode:
    filename = open(args.decode).read().split("\n") if args.decode else []
    decoder(args.decode)
