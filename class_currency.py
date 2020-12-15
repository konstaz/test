class Money:
    def __init__(self, money):
        self._money = money

    currency = {'USD': 'USD', 'EUR': 'EUR', 'UAH': 'UAH'}

    rate = {
        'UAH': {'EUR': 0.029, 'USD': 0.034},
        'EUR': {'UAH': 34, 'USD': 1.21},
        'USD': {'UAH': 28, 'EUR': 0.82}
    }


    def amount_in(self, eur):
        d = ''.join([i for i in self._money if i.isdigit()])
        s = ''.join([i for i in self._money if not i.isdigit()])

        return f'{float(d) * self.rate[s][eur]}{eur}'

    def get_currency(self, currency):
        return self.currency.get(currency)

    def get_money(self, value, from_: str, to: str):  # UAH USD EUR
        return f'{value * self.rate[from_][to]}{to}'

    def change_money(self, value: str):
        q = value.split('_')
        return f'{float(q[0]) * self.rate[q[1]][q[2]]}{q[2]}'

    def add_currency(self, value, from_: str, to: str):
        # try:
        #     self.rate[from_][to] = value
        # except KeyError:
        #     self.rate[from_] = {}
        #     return self.add_currency(value, from_, to)
        self.rate[from_] = self.rate.get(from_, False) or {}
        self.rate[from_][to] = value


if __name__ == "__main__":
    x = Money('85USD')
    print(x.change_money('100_USD_UAH'))
    print(x.get_money(50000, 'UAH', 'EUR'))
    print(x.amount_in('EUR'))
    x.add_currency(38, 'GBR', 'UAH')
    print(x.rate)
