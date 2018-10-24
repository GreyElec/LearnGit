A = ['amazon', 'apple', 'facebook', 'google', 'leetcode']
B = ['e', 'o']


class WordSubSet:
    @staticmethod
    def solution(subset_a, subset_b):
        universal = []
        for char in subset_a:
            for sub_char in subset_b:
                char_temp = char
                for word in sub_char:
                    if word not in char_temp:
                        break
                    else:
                        ind = char_temp.index(word)
                        char_temp = char_temp[:ind] + char_temp[ind + 1:]
                else:
                    continue
                break
            else:
                universal.append(char)
        return universal

    @staticmethod
    def solution_update(subset_a, subset_b):
        universal = []
        from collections import Counter
        count_char_in_subset_b = Counter()
        for word in subset_b:
            for (key, value) in Counter(word).items():
                if count_char_in_subset_b[key] < value:
                    count_char_in_subset_b[key] = value
        for word in subset_a:
            string_letter_counts = Counter(word)
            for (key, value) in count_char_in_subset_b.items():
                if string_letter_counts[key] < value:
                    break
            else:
                universal.append(word)
        return universal


S = WordSubSet()
print(S.solution_update(A, B))
