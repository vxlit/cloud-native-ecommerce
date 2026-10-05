# def count_words(words):
#     count = {}

#     for word in words:
#         if word in count:
#             count[word] += 1
#         else:
#             count[word] = 1

#     return count

# print(count_words(["apple", "banana", "apple", "cherry", "banana", "apple"]))


import heapq

def top_3_words(words):
    count = {}

    for word in words:
        count[word] = count.get(word, 0) + 1

    return heapq.nlargest(3, count.items(), key=lambda item: item[1])
print(top_3_words(["apple", "banana", "apple", "cherry", "banana", "apple"]))