from munch import Munch


class Ports(Munch):
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
        self.p11 = '01010111'.decode('hex')

    def get_port_from_int(self, n):
        return self['p{0}'.format(str(n).zfill(2))]

    def str_to_hex(self, s):
        return s.zfill(8).decode('hex')
