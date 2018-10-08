__author__ = 'Kalyan'

notes = '''
Though it might appear as if the given tests should be able to catch all logical bugs in de_dup_and_sort, that is not the
case as the code below shows.

So be clear that some blackbox tests alone are no substitute for reasoning/taking care of the correctness yourself.

Now add a test that fails with the given code. You can assume that inputs are of right type.
'''
def de_dup_and_sort(input):
    """
    Given an input list of strings, return a list in which the duplicates are removed and the items are sorted.
    """
    if input== None:
        return None
    input = list(input)
    input = remove_duplicates(input)
    input.sort()
    return input
def remove_duplicates(input):
    i=0;j=1
    while i<len(input):
        j=i+1
        while j<len(input):
            if(input[i]==input[j]):
                input.remove(input[j])
                j=0;i=0
                break
            else:
                j+=1
        else:
         i+=1
    return input


# add an test input that fails with above code and then fix the above code.
def test_de_dup_and_sort_student():
    assert None == de_dup_and_sort(None)
    assert [None, 1, 'a', 'none']==de_dup_and_sort(['a', 1, None, 'none'])
    assert [None, 'a', 'satya', ('1', '3'), ('6', '5'), ('9', '1')]== de_dup_and_sort([('6','5'),('9','1'),('1','3'),'a','satya',None])
    assert [['a','b'], ['b', 'a', 'c', 'd'], ['c', 'd','e'], ['f','a', 'b']]==de_dup_and_sort([['c','d','e'],['a','b'],['b','a','c','d'],['f','a','b']])
def test_de_dup_and_sort():
    assert ["a", "b"] == de_dup_and_sort(["b", "a", "b", "a"])
    assert ["a"] == de_dup_and_sort(["a", "a", "a"])
    assert [] == de_dup_and_sort([])
    assert ["a", "b"] == de_dup_and_sort(["a", "b"])
    assert ["a", "b"] == de_dup_and_sort(["a", "b"]*10)


# this will run only on our runs and will be skipped on your computers.
# DO NOT EDIT
import pytest
def test_de_dup_and_sort_server():
    servertests  = pytest.importorskip("unit5_server_tests")
    servertests.test_de_dup_and_sort(de_dup_and_sort)
