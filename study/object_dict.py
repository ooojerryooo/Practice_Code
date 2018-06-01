'''重新定义有序字典的取值方式'''


class ObjectDict(dict):
    def __init__(self, *args, **kwargs):
        super(ObjectDict, self).__init__(*args, **kwargs)

    def __getattr__(self, name):
        value = self[name]
        if isinstance(value, dict):
            value = ObjectDict(value)
        return value


if __name__ == '__main__':
    od = ObjectDict(asf={'a': {'d': 1,'f':2}}, d=True)
    print(od.asf, od.asf.a.d, od.asf.a.f)  # {'a': 1} 1
    print(od.d)  # True
