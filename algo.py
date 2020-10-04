class ListSearchReplace():
    """
    Outlining the limitations:
    The only data type that works for this, will be for numbers such as double, float, or integer.
    As well as strings. If it contains a data structure, such as a dictionary inside of it, it will
    not work. Unsure if it will work with tuples, however, going on the fact to access elements inside
    of a tuple requires the used of indexs, the same as lists it should be able to work. Since this is
    used mainly for lists, I have not tested if it will work for tuples or not.
    """
    def __init__(self, board, nested=False):
        self.nested = nested
        self.board = board

    def search(self, element_to_search):
        """
        This will search for the requested element, this will go only as deep as
        a list inside a list. Not further, mostly because in normal circumstances,
        there won't be a list nested inside a list nested inside another list.

        Returns the index of the element, if it is self.nested is true. Then it will
        first return the the first index (index1) which would be the list, then the
        second (index2) the element it self. 
        """

        if self.nested == True:
            for index1, element in enumerate(self.board):
                for index2, value in enumerate(element):
                    if element[index2] == element_to_search:
                        return index1, index2

                    elif (element[index2] == element_to_search) == False:
                        pass
                        # return self.compress(False, False)

        elif self.nested == False:
            for index, value in enumerate(board):
                if self.board[index] == element_to_search:
                    return index, value

                elif (element[index] == element_to_search) == False:
                    pass
                    # return self.compress(False, False)

    def replace(self, element_to_replace, replacement):
        """
        Replaces an element within a list, with what ever you want it to be.
        However this only goes, as deep as one nested listed. It can't go further than
        a list inside, a list, inside another list. In normal cases, there would be the case
        which I've mentioned above, so this will more than likely solve what you need it for.

        If the element you want to replace does not exist, then nothing will change. A simple way
        to see the results is to obviously print it out, but if you want to automate it. I suggest
        comparing the element inside of the list, which will equate to a true or false value using
        if/else statements. However, this only works for one layer meaning this does not work on nested lists.
        The feature of testing if the element exists within a nested list, is currently being worked
        on.
        """
        self.to_replace = element_to_replace
        if self.nested == True:
            for element in self.board:
                for index, value in enumerate(element):
                    if value == self.to_replace:
                        element[index] = replacement

                    elif (self.to_replace == element[index]) == False:
                        pass

                return self.board

        elif self.nested == False:
            for index, value in enumerate(self.board):
                if value == self.to_replace:
                    self.board[index] = replacement

                elif (self.to_replace == self.board[index]) == False:
                    pass

            return self.board

class DictSearch:
    """
    Outlining the limitations:
    Unable to do the same to the reverse, meaning it can't change the value behind the key, when the dictionary is inside the list. Under normal circumstances.

    This type of functionality will not be needed, if it is. Please by all means, go the the add-on branch and make a new file with the changes detailing them as well. 
    """
    def __init__(self, board):
        self.board = board # In this case board is the dictionary


    def search(self, element_to_search, search_type):
        """
        Has the same features of the search function as the in the ListSearchReplace class.
        Takes in the same parameters, although it does take a slightly different method to 
        achieve the same results.
        """
        search_type = search_type.lower()
        if search_type == 'dictlist':
            """
            This allows you to change the value of a list inside a dictionary. Just pair this up with the replace function from the ListSearchReplace class. 

            However, you will need to reference the to search that is inside the list, and not the key.

            And you will be able to change the value of that index into whatever you want, and do anything with it. It will return the key so you know which list it's pointing to.

            As well as the index of the list of the element within the list. Print out the dictionary and you will see the changes take effect. 
            """
            try:
                for key, value in self.board.items():
                    for index, item in enumerate(self.board[key]):
                        if element_to_search == item:
                            return key, index 

            except IndexError:
                pass

        elif search_type == 'dict':
            """
            Allows you to search for a key within a dictionary. If they key does indeed exist. 

            It will return True, if it does not then it will return False
            """
            for key, value in self.board.items():
                if element_to_search == key:
                    return True

                elif element_to_search != key:
                    return False