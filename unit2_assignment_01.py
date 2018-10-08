__author__ = 'Kalyan'

notes = '''
1. Read instructions for each function carefully.
2. Feel free to create new functions if needed. Give good names though :)
3. Use builtins and datatypes that we have seen so far.
4. If something about the function spec is not clear, use the corresponding test
   for clarification.
5. Many python builtin functions allow you to pass functions to customize their behavior. This makes it very productive
   to get things done in python.
'''

# Given a list of age, height of various people [(name, years, cms), .... ]. Sort them in decreasing by age and increasing by height.
# NOTE: define a function and pass it to the builtin sort function (key) to get this done, don't do your own sort.
# Do the sort in-place (ie) don't create new lists.
def a(x):
    return (-x[1],x[2])
def custom_sort(input):
 try:
    input = sorted(input,key=a)
    return input
 except TypeError as te:
    return None
 except IndexError as ie:
    return []



def single_custom_sort_test(input, expected):
    input= custom_sort(input) # sorts in place
    assert input == expected
def test_custom_sort():
    # boundary cases
    single_custom_sort_test(None, None)
    single_custom_sort_test([], [])

    # no collisions
    single_custom_sort_test(
        [("Ram", 25, 160), ("Shyam", 30, 162), ("Sita", 15, 130)],
        [("Shyam", 30, 162), ("Ram", 25, 160), ("Sita", 15, 130)])

    # collisions in age
    single_custom_sort_test(
        [("Ram", 25, 165), ("Shyam", 30, 162), ("Ravi", 25, 160), ("Gita", 30, 140)],
        [("Gita", 30, 140), ("Shyam", 30, 162), ("Ravi", 25, 160), ("Ram", 25, 165)])

    # collisions in age and height, then initial order is maintained in stable sorts.
    single_custom_sort_test(
        [("Ram", 25, 165), ("Shyam", 30, 140), ("Ravi", 25, 165), ("Gita", 30, 140)],
        [("Shyam", 30, 140), ("Gita", 30, 140), ("Ram", 25, 165), ("Ravi", 25, 165)])


VOWELS = set("aeiou")

# returns the word with the maximum number of vowels, in case of tie return
# the word which occurs first. Use the builtin max function and pass a key func to get this done.
def vowel(word):
    return len(set("aeiou") & set(word))

def count_vowels(words):
        result = []
        count = 0
        for j in range(0, len(words)):
            if vowel(words[j].lower()):
                count += 1
        return count

def sort_by_vowel_count(words):
       if words == None:
            return None
       try:
            words.sort(key=count_vowels, reverse=True)
            return words[0]
       except IndexError:
           return None
def max_vowels(input):
        input = sort_by_vowel_count(input)
        return input


def test_max_vowels():
    assert None == max_vowels(None)
    assert None == max_vowels([])

    assert "hello" == max_vowels(["hello", "pot", "gut", "sit"])
    assert "engine" == max_vowels(["hello","engine", "pot", "gut", "sit"])

    assert "automobile" == max_vowels(["engine", "hello", "pot", "gut", "sit", "automobile"])

    assert "fly" == max_vowels(["fly", "pry", "ply"])


