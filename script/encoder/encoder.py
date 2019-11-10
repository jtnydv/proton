import argparse

def encoder(pscript):
    text = open(pscript).read()
    out = open(pscript[:pscript.index(".")]+".bin", "w")
    for i in text:
        out.write(bin(ord(i)[2:])
    out.close()
    
parser = argparse.ArgumentParser()
parser.add_argument("-e","--encode", metavar='FILE', help="Encode a ProtonScript program file.")
parser.add_argument("-d","--decode", metavar='FILE', help="Decode a ProtonScript program file.")
args = parser.parse_args()
    
if args.encode:
     filename = open(args.encode).read().split("\n") if args.encode else []
     encoder(filename)
