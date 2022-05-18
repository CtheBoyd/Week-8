def words_in_both(a, b):
    a1 = set(a.lower().split())
    b1 = set(b.lower().split())
    return a1.intersection(b1)

common_words = words_in_both("She is a jack of all trades", 'Jack was tallest of all')
print(common_words)
