# Author: Christopher Boyd
# GitHub username: CtheBoyd
# Date: 5/18/2022
# Description: Takes an alphanumeric and special character string returning only letters and the count of each.
#

def count_letters(string):
    """Takes an alphanumeric and special character string returning only letters and the count of each. """

    alpha = {}

    for lp in string:

        lp = lp.upper()

        if 'A' <= lp <= 'Z':

            if lp not in alpha:

                alpha[lp] = 0

            alpha[lp] += 1

    return alpha

print(count_letters("AaBb*&%?C12345AFDAFDFASDFASDFdfsdfasdfdsfYJKYJLKHJKL%^#%^%$&#^$*&(*)*(*&^%$<>?6cDcEe"))