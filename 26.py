def bintodec (bin):
    return int(bin,2)
def llbintodec(llbin):
    lldec = []
    for e in llbin:
        lldec.append(bintodec(e))
