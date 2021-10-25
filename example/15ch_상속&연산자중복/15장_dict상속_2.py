class MyDict(dict):

    def   items(self):
        k=super().items()
        return sorted(k, key=lambda a:a[1])
data=MyDict({ 'japan': 26, 'china': 28, 'america': 34, 'korea': 33})

print(data.items())
for k, v in data.items():
    print(k, v)
