class ListSearchReplace:
    def __init__(self, board, dtype, nested=False):
        self.board = board
        self.nested = nested
        self.dtype = dtype

    def search(self, element_to_search):
        if self.nested == True:
            for index1, element in enumerate(self.board):
                for index2, value in enumerate(element):
                    if element[index2] == element_to_search:
                        return index1, index2

                    elif (element[index2] == element_to_search) == False:
                        pass

        elif self.nested == False:
            for index, value in enumerate(self.board):
                if self.board[index] == element_to_search:
                    return index

                elif (self.board[index] == element_to_search) == False:
                    pass

    def replace(self, element_to_replace, replacement):
        self.to_replace = element_to_replace
        if self.dtype.lower() == 'str':
            if self.nested == True:
                for element in self.board:
                    for index, value in enumerate(element):
                        if value == self.to_replace:
                            element[index] = replacement

                        elif (self.to_replace == element[index]) == False:
                            pass

            elif self.nested == False:
                for index, value in enumerate(self.board):
                    if value == self.to_replace:
                        self.board[index] = replacement

                    elif (self.to_replace == self.board[index]) == False:
                        pass

        elif self.dtype.lower() == 'int':
            if self.nested == True:
                for element in self.board:
                    for index, value in enumerate(element):
                        if value == self.to_replace:
                            element[index] = replacement

                        elif (self.to_replace == element[index]) == False:
                            pass

            elif self.nested == False:
                for index, value in enumerate(self.board):
                    if value == self.to_replace:
                        self.board[index] = replacement

                    elif (self.to_replace == self.board[index]) == False:
                        pass

class DictSearch:
    def __init__(self, board):
        self.board = board # In this case board is the dictionary

    def search(self, element_to_search, search_type):
        if search_type == 'dictlist':
            try:
                for key, value in self.board.items():
                    for index, item in enumerate(self.board[key]):
                        if element_to_search == item:
                            return key, index 

            except IndexError:
                pass

        elif search_type == 'dict':
            for key, value in self.board.items():
                if element_to_search == key:
                    return True

                elif element_to_search != key:
                    return False
