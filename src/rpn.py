from collections import deque

class RPN:
    """This is a Reverse Polish Notation calculator. The stack of numbers represents a stack"""
    def __init__(self, file_name, operation_dict):
        self.file_name = file_name
        self.operation_dict = operation_dict
        self.file_data = None
        self.stack = deque([])

    def get_file_data(self):
        """Create, open for reading, and store file contents into file_data member"""
        file = open(self.file_name, 'r+')
        #Strip newline character and store file data
        self.file_data = file.read().splitlines()
        return self.file_data

    def is_integer(self, val):
        """Check that value read from file can be typecasted into numerical value"""
        try:
            int(val)
            return True
        except ValueError:
            pass

    def get_result(self):
        """This function loops through the file_data file and determines whether the
        data read is an mumerical value or an operation from the operation_dict. It then
        operates on the stack to simulate the "first on first off operations of a stack"""
        answer = 0
        print('-' * 62)
        print("\tTokens", format("Operations", '>16'), format("Stack", '>13'))
        print('-' * 62)

        for i in self.file_data:
            if self.is_integer(i):
                self.stack.appendleft(round(int(i), 3))
                action = "pushed: " + i
                print('\t', i.ljust(11), action.ljust(18), ' '.join(str(val) for val in self.stack))
            else:
                i = i.upper()
                answer = self.operation_dict[i](self.stack)
                action = "popped: " + str(self.stack.popleft())
                print('\t', i.ljust(11), action.ljust(18), ' '.join(str(val) for val in self.stack))
                self.stack.popleft()
                self.stack.appendleft(answer)

        print('-' * 62)
        print("\tAnswer: ", answer)

