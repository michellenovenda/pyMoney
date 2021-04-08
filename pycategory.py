def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk)) 
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk)) 
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))

acc = []
ds = []

_dsc = "DESCRIPTION"
_amt = "AMOUNT"
_blc = "BALANCE"
_init = "INITIAL"
_cat = "CATEGORY"
_blk = " "
block = "||"


class Categories:
    """
    This is a class of Categories. The commands are:
    __init__                    initialize a nested list of categories and its sub-categories
    view                        shows user the list of categories and its sub-categories
    is_category_valid           check a sub-category's existence in a specific category
    find_subcategories          show all the sub-categories under a specific category
    """
    def __init__(self):
        """
        This is a category initializer.
        Its main purpose is to initialize categories and its sub-categories.
        Takes self as the parameter.
        """
        self._categories = ['Expense',\
                        ['Food',
                            ['meal', 'drink', 'snack', 'cafe', 'groceries']], \
                        ['Transportation',\
                            ['taxi', 'bus', 'railway']],\
                        ['Shopping',\
                            ['stationery', 'health', 'beauty', 'electronics', 'accessories', 'clothing']], \
                        ['Communication',\
                            ['internet', 'phone']], \
                        ['Finance',\
                            ['taxes', 'fines', 'insurance']], \
                    'Income',\
                        ['salary', 'bonus', 'lottery']]

    def get_categories(self):
        return self._categories

    def view(self, prefix=()):
        """
        This is a category viewer.
        Its purpose is to show the user what categories can be chosen for the record inputs.
        Prints the list of categories and its sub-categories.
        """
        def view_categories(categories, prefix=()):
          if type(categories) in {list, tuple}:
              i = 0
              for elm in categories:
                  view_categories(elm, prefix+(i,))
          else:
              s = ' '*3*(len(prefix)-1)
              s += '•' + categories
              print(s)

        view_categories(self._categories)


    def is_category_valid(self, category):
        """
        This is a sub-category checker.
        Its purpose is to check a subcategory's existence in a list of categories.
        Takes self and the category to be checked as a parameter.
        Returns True if the subcategory is in the category list.
        Returns False if it is not.
        """
        def is_valid(category, categories):
          for thing in categories:
              if type(thing) == list:
                  if is_valid(category, thing):
                      return True
              if thing == category:
                  return True
          return False

        return is_valid(category, self._categories)


    def find_subcategories(self, category):
        """
        This is a find subcategory function.
        Its purpose is to show all the sub-categories under a specific category.
        Takes self and a category name to find as a parameter.
        Returns a non-nested list containing the specified category and all the sub-categories under it (if any).
        """
        def find_subcategories_gen(category, categories, found = False):
            if type(categories) == list:
                for index, child in enumerate(categories):
                    yield from find_subcategories_gen(category, child, found)

                    if child == category and index + 1 < len(categories) and type(categories[index+1]) == list and found == False:
                        yield from find_subcategories_gen(category, categories[index:index+2], found = True)
            else:
                if categories == category or found == True:
                    yield categories

        return [x for x in find_subcategories_gen(category, self._categories)]


