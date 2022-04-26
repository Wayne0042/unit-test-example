class Caculator2:
    _sum = 0

    def add(self, value):
        try:
            self._sum += value
        except:
            print('can not add')

    def sum(self):
        return self._sum

if __name__ == '__main__':
    caculator = Caculator2()
    caculator.add('123')