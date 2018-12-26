
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(object):
    def hello(self):
        print(__name__)


if __name__ == '__main__':
    print(11)
    print(type("111"))
