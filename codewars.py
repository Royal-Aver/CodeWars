# 7 kyu - Stone Pickaxe Crafting
# Task: Given an array, return the maximum amount of stone pickaxes you can craft before you run out of sticks
# and cobblestones. Within the array would be a series of strings with the exact names of the materials listed below.
# A single stone pickaxe is made of 3 "Cobblestone" and 2 "Sticks", check if your given array contains
# enough "Sticks" and "Cobblestone" to craft a single stone pickaxe or even more.
# Do not count any materials apart from "Cobblestones", "Sticks" and "Wood". Wood can be converted into 4 sticks!
# Here are the materials you would expect in an array:
#
# Sticks
# Cobblestone
# Stone (These are different from cobblestone and cannot be used to make a stone pickaxe.)
# Wool
# Dirt
# Wood (Can be treated as sticks, typically 4 sticks for 1 wood)
# Diamond

def stone_pick(lst_materials: list) -> int:
    cobblestone = 0
    sticks = 0
    if len(lst_materials) == 0:
        return 0
    for item in lst_materials:
        if item == "Sticks":
            sticks += 1
        elif item == "Cobblestone":
            cobblestone += 1
        elif item == "Wood":
            sticks += 4

    count_pickaxe = int(min(cobblestone / 3, sticks / 2))
    return count_pickaxe

assert stone_pick(["Sticks"] * 4 + ["Cobblestone"] * 6) == 2
assert stone_pick(["Wool"] * 21 + ["Sticks"] * 11 + ["Stone"] * 31 + ["Cobblestone"] * 41 + ["Diamond"] * 8) == 5
assert stone_pick([]) == 0


# 5 kyu First non-repeating character
# Write a function named first_non_repeating_letter that takes a string input,
# and returns the first character that is not repeated anywhere in the string.
# For example, if given the input 'stress', the function should return 't',
# since the letter t only occurs once in the string, and occurs first in the string.
# As an added challenge, upper- and lowercase letters are considered the same character,
# but the function should return the correct case for the initial letter.
# For example, the input 'sTreSS' should return 'T'.
# If a string contains all repeating characters, it should return an empty string ("");
# Note: the function is called firstNonRepeatingLetter for historical reasons,
# but your function should handle any Unicode character.

def first_non_repeating_letter(text: str) -> str:
    text_lower = text.lower()
    non_repeating_character_string = ''
    if len(text) == 1:
        return text
    if len(set(text_lower)) == 1 or text_lower == '':
        return non_repeating_character_string
    else:
        for i, char in enumerate(text_lower):
            if text_lower.count(char) == 1:
                non_repeating_character_string += text[i]
        if len(non_repeating_character_string) == 0:
            return non_repeating_character_string

    return non_repeating_character_string[0]


assert first_non_repeating_letter('stress') == 't'
assert first_non_repeating_letter('moonmen') == 'e'
assert first_non_repeating_letter('A') == 'A'
assert first_non_repeating_letter('') == ''
assert first_non_repeating_letter('abba') == ''
assert first_non_repeating_letter('sTreSS') == 'T'


# 5kyu Scramblies
# Complete the function scramble(str1, str2) that returns true if a portion
# of str1 characters can be rearranged to match str2, otherwise returns false.
# Notes:
# Only lower case letters will be used (a-z). No punctuation or digits will be included.
# Performance needs to be considered.

def scramble(s1, s2):
    if len(s1) < len(s2):
        return False

    char_count = {}

    for char in s1:
        if char in char_count:
            char_count[
                char] += 1
        else:
            char_count[
                char] = 1

    for char in s2:
        if char not in char_count or \
                char_count[
                    char] == 0:
            return False
        char_count[char] -= 1

    return True

assert scramble('rkqodlw', 'world') == True
assert scramble('katas', 'steak') == False
assert scramble('yyfywsumxbkppxuvrva', 'bwuxvkbv') == False


# Trolls are attacking your comment section!
# A common way to deal with this situation is to remove all of the vowels
# from the trolls' comments, neutralizing the threat.
# Your task is to write a function that takes a string and return
# a new string with all vowels removed.
# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
# Note: for this kata y isn't considered a vowel.
vowels_lst = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

def disemvowel(text:str) -> str:
    res = ''.join([char for char in text if char not in vowels_lst])
    return res

assert disemvowel("This website is for losers LOL!") == "Ths wbst s fr lsrs LL!"


