# Task 2: Program to analyze text and perform various operations
# Lab Assignment: #4
# Version: 1.0
# Developer: Yury Dudko
# Date: 20.04.2024

import zipfile
import re
from TextAnalyzer import *
from decorator import *

@repeat_execution
def task_2():
    """
    Test function for Task 2.
    """
    # Example text for analysis
    filename = 'TextExample.txt'
    analyzer = TextAnalyzer(filename)

    # Print results to the screen
    print("Number of sentences:", analyzer.count_sentences())
    print("Number of sentences by type:", analyzer.count_sentence_types())
    print("Average sentence length:", analyzer.average_sentence_length())
    print("Average word length:", analyzer.average_word_length())
    print("Number of smileys:", analyzer.count_smileys())
    print("Words including characters from 'g' to 'o':", analyzer.find_words_in_range())
    print("Is valid email:", analyzer.check_email_format())
    print("Number of words:", analyzer.count_words())
    print("Longest word:", analyzer.longest_word())
    print("Odd words:", analyzer.odd_words())

    # Save results to a file
    analyzer.save_results_to_file("text_analysis_results.txt")

    # Archive the results file
    with zipfile.ZipFile('text_analysis_results.zip', 'w') as zipf:
        zipf.write('text_analysis_results.txt')
