__author__ = 'Kalyan'

notes = '''
Again while this code passes the tests, this code is wrong as it has been modified for the sake of the tests.

Write a test case that will fail this test. Ignore infinite sequences for now.
'''

def generator_zip(seq1, seq2, *more_seqs):
    flag=True
    if ((seq1 == None) | (seq2 == None)):
        flag = False
        yield []
    if flag:
        seq1=list(seq1)
        seq2=list(seq2)
        if more_seqs==():
            t=min(len(seq1),len(seq2))
            for x in range(t):
              yield (seq1[x],seq2[x])
        else:
           if any(i==None for i in more_seqs):
               flag=False
               yield []
           elif any(i == [] for i in more_seqs):
               flag = False
               yield []
           elif flag:
               more_seqs = [list(i) for i in more_seqs]
               k = min([len(i) for i in more_seqs])
               t=min(len(seq1),len(seq2),k)
               try :
                   for x in range(t+1):
                       z=(seq1[x],seq2[x])+tuple([more_seqs[i][x] for i in range(len(more_seqs))])
                       yield z
               except:
                   pass

# add some test inputs that fail with the above code, then fix the above code.
def test_generator_zip_student():

  gen = generator_zip("satya", "rajesh", "viswanadh", "govind")
  assert list(gen)==[('s', 'r', 'v', 'g'), ('a', 'a', 'i', 'o'), ('t', 'j', 's', 'v'), ('y', 'e', 'w', 'i'), ('a', 's', 'a', 'n')]
  gen = generator_zip("satyaaaa", "rajeshhhh", {1, 2, 3, 'a', 's'}, {1: 2, '2': 3, '3': 3, 4: 4, 5: 6, 6: 'a'})
  assert list(gen)==[('s', 'r', 'a', 1), ('a', 'a', 1, 4), ('t', 'j', 's', 5), ('y', 'e', 3, 6), ('a', 's', 2, '3')]

  gen= generator_zip("abcd", "abcd", "abcd")
  assert list(gen)== [('a', 'a', 'a'), ('b', 'b', 'b'),('c','c','c'),('d','d','d')]

  gen=generator_zip([],[])
  assert list(gen)==[]

  gen=generator_zip([],[],[])
  assert list(gen)==[[]]

  gen=generator_zip([],None)
  assert list(gen)==[[]]

  gen  =  generator_zip(range(4), range(5), None)
  assert list(gen) == [[]]

  gen  =   generator_zip({1: 1, 2: 'a', 3: 3}, {1, 2, 3, 'a'}, [1, 2, 3, 4], "satya", "aditya")
  assert [(1, 'a', 1, 's', 'a'), (2, 1, 2, 'a', 'd'), (3, 2, 3, 't', 'i')] == list(gen)

def test_generator_zip():
    gen = generator_zip(range(5), range(3), range(4), range(5))
    assert type(gen).__name__ == 'generator'
    check_generator(gen, 3, 4)

    gen = generator_zip(range(5), range(3), range(2))
    assert type(gen).__name__ == 'generator'
    check_generator(gen, 2, 3)

    gen = generator_zip(range(1, 5), "abc", [1, 2])
    assert [(1, 'a', 1), (2, 'b', 2)] == list(gen)

    gen = generator_zip((1, 2), "abcd")
    assert [(1, 'a'), (2, 'b')] == list(gen)

def check_generator(gen, max_count, tuple_length):
    for x in range(max_count):
        result = next(gen)
        assert len(result) == tuple_length, "invalid length"
        for element in result:
            assert x == element, "unexpected value"
    try:
        next(gen)
        assert False, "generator did not finish as expected"
    except StopIteration as se:
        pass


# this will run only on our runs and will be skipped on your computers.
# DO NOT EDIT
import pytest
def test_generator_zip_server():
    servertests = pytest.importorskip("unit5_server_tests")
    servertests.test_generator_zip(generator_zip)
