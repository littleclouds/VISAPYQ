'''Anish is given a string S and has been asked to determine if the given string S contains two non-overlapping substrings "AB" and "BA" (the substrings can go in any order).

As a friend of Anish, your task is to return “True” if the string S contains two non-overlapping substrings "AB" and "BA" (the substrings can go in any order) otherwise return “False” (without quotes).

Example:-
The string “ABBA” has two non-overlapping substrings “AB” and “BA” respectively. So “True” will be printed(without quotes).'''

def has_non_overlapping_substrings(s):
    n = len(s)
    found_ab = False
    found_ba = False

    i = 0
    while i < n - 1:
        if s[i:i+2] == "AB":
            if found_ba:
                return True
            found_ab = True
            i += 1
        elif s[i:i+2] == "BA":
            if found_ab:
                return True
            found_ba = True
            i += 1
        i += 1

    return False

# Example usage
if __name__ == "__main__":
    s = "ABBA"
    print(has_non_overlapping_substrings(s)) # Output: True
