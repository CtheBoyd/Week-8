# Author: Christopher Boyd
# GitHub username: CtheBoyd
# Date: 5/18/2022
# Description: Takes two strings and returns words that are in both strings.
#

def words_in_both(sent_1, sent_2):
    """Takes two strings and returns words that are in both strings."""
    sent_1 = set(sent_1.lower().split())

    sent_2 = set(sent_2.lower().split())

    return sent_1.intersection(sent_2)

common_words = words_in_both("She is a jack of all trades", 'Jack was tallest of all')
print(common_words)
