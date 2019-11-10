def encoder(pscript)
    text = open(pscript).read()
    out = open(pscript[:pscript.index(".")]+".bin", "w")
    for i in text:
        out.write(bin(ord(i)[2:])
    out.close()
