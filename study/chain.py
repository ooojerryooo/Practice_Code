class Chain():

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __call__(self, path=''):
        return Chain('%s/%s' % (self._path, path))


    def __str__(self):
        return self._path

    __repr__ = __str__

if __name__ == '__main__':
    print(Chain().abc.ddd.nnn('123').sdfdfdsf('sdfd'))


