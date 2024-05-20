# Task 4: Program to analyze a given text string
# Lab Assignment: #3
# Version: 1.0
# Developer: Dudko Yury
# Date: 28.03.2024

from decorator import repeat_execution

# Function to count the frequency of each letter in the text
def count_letter_frequency(text):
    """
    Count the frequency of each letter in the given text.
    
    Args:
    text (str): The text string.
    
    Returns:
    dict: A dictionary containing the frequency of each letter.
    """
    letter_freq = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            letter_freq[char] = letter_freq.get(char, 0) + 1
    return letter_freq

def count_words(text):
    """
    Count the number of words in the given text.
    
    Args:
    text (str): The text string.
    
    Returns:
    int: The number of words in the text.
    """
    word = text.split()
    return len(word)

# Function to sort and join word phrases separated by commas
def sort_and_join_phrases(text):
    """
    Sort and join word phrases separated by commas in the given text.
    
    Args:
    text (str): The text string.
    
    Returns:
    str: Sorted word phrases separated by commas.
    """
    words = text.split(',')
    sorted_phrases = '\n '.join(sorted(words))
    return sorted_phrases

@repeat_execution
def task_4():
    """
    Function to perform Task 4 .
    """
    text = "So she was considering in her own mind, as well as she could, for the hot day made her feel very sleepy and stupid, whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her."
    # Count letter frequency
    letter_freq = count_letter_frequency(text)
    print("\nLetter Frequency:")
    for letter, freq in letter_freq.items():
        print(f"{letter}: {freq}")

    # Count number of words
    word_count = count_words(text)
    print("\nNumber of Words:", word_count)

    # Sort and join phrases
    sorted_phrases = sort_and_join_phrases(text)
    print("\nSorted and Joined Phrases:")
    print(sorted_phrases)

#task_4()

# Frequency of each letter
#letter_freq = {char: text.count(char) for char in text if char.isalpha()}