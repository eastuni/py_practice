class MyDict(dict):

    def    keys(self):
        k=super().keys()
        return sorted(k)

data=MyDict({ 'japan': 26,
              'china': 28,
              'america': 34,
              'korea': 33})

print(data.keys())
