class MyNumberB(object):

    def __init__(self, number):

        self._number = number


    def number():

        def _get_number(self):

            return self._number

        def _set_number(self, value):

            if isinstance(value, basestring):

                number = eval(value)

            else:

                number = value

            self._number = number

        return dict(fget=_get_number, fset=_set_number)


    number = property(**number())
