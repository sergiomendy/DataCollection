import random
import pandas as pd


class Utils(object):
    @classmethod
    def divider(cls, n=54):
        return '-' * n

    @classmethod
    def randomize(cls,
                  start,
                  final):
        return random \
            .randint(start, final)

    @classmethod
    def x(cls, x):
        x = x.split(' ')
        last_name = x[-1].upper()
        first_name = x[0].capitalize()
        x = ' '.join([first_name, last_name])
        return x

    @classmethod
    def concatenate(cls,*args):
        data = []
        for arg in args:
            if isinstance(arg,list):
                data = data + arg
            else:
                pass
        return data

    @classmethod
    def convertToXOF(cls,amount,devise,currencies):
        currencies = pd.DataFrame(currencies)
        currency = currencies[currencies['devise'] == devise]
        achat = currency.achat.values[0]
        return amount*achat
    