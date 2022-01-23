class SampleClass:
    def __init__(self, cfg):
        self.params = cfg

    def sender(self):
        print('sender')
        self.receaver()

        return_value = 1
        output = self.return_value_test(return_value)
        print(output)

    def receaver(self):
        print('receaver')

    def return_value_test(self, return_value):
        return_value += 1
        return return_value
        
