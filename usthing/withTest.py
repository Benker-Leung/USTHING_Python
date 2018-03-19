
class example:
    def __enter__(self):
        print('__enter__ called')
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        print('__exit__ called')
        print('type', exc_type)
        print('value', exc_value)
        print('tb', exc_tb)

    def do_something(self):
        print('do something called')

with example() as p:
    p.do_something()



















#
