__author__ = 'Kalyan'

notes = '''
Implement a left binary search and write exhaustive tests for the same. Left binary search returns the index of left most
element when a search key repeats. For e.g if input is [1,2,3,3,4,4,5] and I search 3, it should return 2 as index 2 is
the left most occurance of 3.

In [1,1,1,1,1,1,1,1], I search for 1, you should return 0.

Note that we are looking for a binary search => we want not more than log(N) lookups, so a solution that involves finding
a random 1 and then doing a linear scan to the left is not a solution :).

- input is an indexable, value is any object.
- return -1 if not found or index of 1st occurance if found.
'''


def left_binary_search(input, value):
    try:
        low, high = 0, len(input)-1
        while low <= high:
            mid = (low + high) / 2
            if input[mid] == value:
               if low==mid:
                   return low
               while input[low]<value:
                   low+=1
               return low
            if input[mid] > value:
                high = mid - 1
            else:
                low = mid + 1
        return -1
    except TypeError as te:
        return -1
    except IndexError as ie:
        return -1


# write your own exhaustive tests :)
def test_left_binary_search_student():
   input = range(10)
   for index, value in enumerate(input):
     assert index == left_binary_search(input, value)
   assert 0 == left_binary_search([1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3], 1)
   assert 0 == left_binary_search([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], 0)
   assert 0==left_binary_search([12],12)
   assert -1==left_binary_search([12],[11])
   assert -1==left_binary_search([12],13)
   assert 6 == left_binary_search([10, 19, 35, 43, 45, 45, 69], 69)
   assert 789965 == left_binary_search(range(789966), 789965)
   assert -1 == left_binary_search(range(5), None)
   assert -1 == left_binary_search(range(5), {1})
   assert -1==left_binary_search([],2)
# these tests run only on our runs and will be skipped on your computers.
# DO NOT EDIT.
import pytest
def test_left_binary_search_server():
    servertests = pytest.importorskip("unit5_server_tests")
    servertests.test_left_binary_search(left_binary_search)
