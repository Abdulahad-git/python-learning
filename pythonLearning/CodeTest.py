import unittest
def getFormatedName(fname,lname):
    Format_name=fname+" "+lname
    return Format_name.title()

h=getFormatedName("abdul","ahad")

class Testing(unittest.TestCase):
    def testThis(self):
        TesTFunc=getFormatedName("abdul","ahad")
        self.assertEqual(TesTFunc,"Abdul Ahad")

unittest.main()