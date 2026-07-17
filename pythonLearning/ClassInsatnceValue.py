from random import randint
from collections import OrderedDict
class A():
    def info(self):
        print("Info From A")

class B():
    b=A()

c=B()
c.b.info()




favorite_languages = OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'
for name, language in favorite_languages.items():

    print(name.title() + "'s favorite language is " +
    language.title() + ".")



x = randint(1, 6)
print(x)