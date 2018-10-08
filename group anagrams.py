import collections
class Solution(object):
    def calculate_hash(self,string):
        prime_dict = {'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13, 'g': 17, 'h': 19, 'i': 23, 'j': 29, 'k': 31,
             'l': 37, 'm': 41, 'n': 43, 'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 79, 'w': 83,
             'x': 89, 'y': 97, 'z': 101}

        hash_val = 1
        for i in string:
            hash_val *= prime_dict[i]
        return hash_val


    def groupAnagrams(self, strs):
        # anagram_dict = {}
        # for i in strs:
        #     hash_val = self.calculate_hash(i)
        #     if hash_val in anagram_dict:
        #         anagram_dict[hash_val].append(i)
        #     else:
        #         anagram_dict[hash_val] = [i]
        # result = []
        # print anagram_dict
        # for key in anagram_dict:
        #     result.append(anagram_dict[key])
        # result = map(sorted, result)
        # result.sort(key = len)
        #
        # return result
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()

if __name__ == "__main__":
    a = Solution()
    print a.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])