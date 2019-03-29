from dicto import dicto


ports = dicto()
ports.p01 = '01010101'.decode('hex')
ports.p02 = '01010102'.decode('hex')
ports.p03 = '01010103'.decode('hex')
ports.p04 = '01010104'.decode('hex')
ports.p05 = '01010105'.decode('hex')
ports.p06 = '01010106'.decode('hex')
ports.p07 = '01010107'.decode('hex')
ports.p08 = '01010108'.decode('hex')
ports.p09 = '01010109'.decode('hex')

class Ports(dicto):
    """docstring for Ports"""
    def __init__(self):
        super(Ports, self).__init__()
        self.p01 = '01010101'.decode('hex')
        self.p02 = '01010102'.decode('hex')
        self.p03 = '01010103'.decode('hex')
        self.p04 = '01010104'.decode('hex')
        self.p05 = '01010105'.decode('hex')
        self.p06 = '01010106'.decode('hex')
        self.p07 = '01010107'.decode('hex')
        self.p08 = '01010108'.decode('hex')
        self.p09 = '01010109'.decode('hex')
