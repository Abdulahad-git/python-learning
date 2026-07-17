import unittest


class AnonymouseSurvey():
    def __init__(self,question):
        self.question=question
        self.responses=[]

    def showQuest(self):
        print(self.question)

    def new_response(self,nr):
        self.responses.append(nr)

    def show_resp(self):
        print("All the responses")
        for ne in self.responses:
            print(self.responses)
            print(ne)


quest = "What is your Favourite college?"
mysur=AnonymouseSurvey(quest)

while True:
    mysur.showQuest()
    print("Press q to Quit")
    dat=input("Respond :\t")
    if quest == 'q':
        break;
    else:
        mysur.new_response(dat)

mysur.show_resp()



'''class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()'''
