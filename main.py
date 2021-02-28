#!/usr/bin/env python

from Exceptions import keywords, definitions
import operator

CRESET  = '\33[0m'
CGREEN  = '\33[32m'

bad_words = ["the", "in", "a", "an", "was", "to", "of", "with",
             "such", "made", "as"]

def output_results(final):
    print("Best match: \n\t{}{}{}: {}".format(CGREEN, final[0], CRESET, definitions[final[0]]))
    new_tuple = final[1:]
    print("Other possible matches:")
    for item in new_tuple:
        print("\t{}: {}".format(item, definitions[item]))


def sort_results(matches):
    sorted_matches = dict(sorted(matches.items(), key=operator.itemgetter(1), reverse=True))
    final = ()
    for (key, value) in sorted_matches.items():
        if value > 0:
            final = final + (key,)

    output_results(final)


def populate_matches():
    matches = {}
    for exception in definitions.keys():
        matches[exception] = 0

    return matches


def find_best_match(split_search):
    matches = populate_matches()
    for search_word in split_search:
        for (key, value) in keywords.items():
            if search_word in value:
                matches[key] = matches[key] + 1

    sort_results(matches)


def remove_bad_words(split_search):
    for word in split_search:
        if word in bad_words:
            split_search.remove(word)

    return split_search


def process_search(search):
    split_search = search.split(" ")
    new_search = remove_bad_words(split_search)
    find_best_match(new_search)


def get_input():
    search = input("Exception: ")
    return search


def main():
    search = get_input()
    process_search(search)


if __name__ == '__main__':
    main()
