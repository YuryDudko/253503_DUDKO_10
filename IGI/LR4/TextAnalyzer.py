import re

class TextAnalyzer:
    def __init__(self, filename):
        """
        Initialize a TextAnalyzer object with text from a file.

        Args:
            filename (str): Name of the file containing the text.
        """
        self.text = self.read_text_from_file(filename)

    def read_text_from_file(self, filename):
        """
        Read text from a file.

        Args:
            filename (str): Name of the file containing the text.

        Returns:
            str: Text read from the file.
        """
        with open(filename, 'r') as file:
            return file.read()

    def count_sentences(self):
        """
        Count the number of sentences in the text.

        Returns:
            int: Number of sentences in the text.
        """
        sentences = re.split(r'[.!?]', self.text)
        return len(sentences)

    def count_sentence_types(self):
        """
        Count the number of sentences by type (narrative, interrogative, imperative).

        Returns:
            dict: Dictionary containing counts of each sentence type.
        """
        narrative_sentences = re.findall(r'[^\n.!?]*[.!?]', self.text)
        interrogative_sentences = re.findall(r'[^\n.!?]*\?', self.text)
        imperative_sentences = re.findall(r'[^\n.!?]*!', self.text)
        return {
            "narrative": len(narrative_sentences),
            "interrogative": len(interrogative_sentences),
            "imperative": len(imperative_sentences)
        }

    def average_sentence_length(self):
        """
        Calculate the average length of sentences in the text.

        Returns:
            float: Average length of sentences.
        """
        sentences = re.split(r'[.!?]', self.text)
        total_characters = sum(len(sentence) for sentence in sentences)
        return total_characters / len(sentences)

    def average_word_length(self):
        """
        Calculate the average length of words in the text.

        Returns:
            float: Average length of words.
        """
        words = re.findall(r'\b\w+\b', self.text)
        total_characters = sum(len(word) for word in words)
        return total_characters / len(words)

    def count_smileys(self):
        """
        Count the number of smileys in the text.

        Returns:
            int: Number of smileys.
        """
        smileys = re.findall(r'[;:]-*[()\[\]]+', self.text)
        return len(smileys)

    def find_words_in_range(self):
        """
        Find words in the text containing characters from 'g' to 'o'.

        Returns:
            list: List of words.
        """
        words = re.findall(r'\b[g-oG-O]+\b', self.text)
        return words

    def check_email_format(self):
        """
        Check if the text contains a valid email address.

        Returns:
            bool: True if the text contains a valid email address, False otherwise.
        """
        return bool(re.match(r'^\w+@\w+\.\w+$', self.text))

    def count_words(self):
        """
        Count the number of words in the text.

        Returns:
            int: Number of words.
        """
        words = re.findall(r'\b\w+\b', self.text)
        return len(words)

    def longest_word(self):
        """
        Find the longest word in the text and its index.

        Returns:
            tuple: Longest word and its index.
        """
        words = re.findall(r'\b\w+\b', self.text)
        longest_word = max(words, key=len)
        return longest_word, words.index(longest_word) + 1

    def odd_words(self):
        """
        Find words in odd positions in the text.

        Returns:
            list: List of odd words.
        """
        words = re.findall(r'\b\w+\b', self.text)
        return [word for index, word in enumerate(words, start=1) if index % 2 != 0]

    def save_results_to_file(self, filename):
        """
        Save the analysis results to a file.

        Args:
            filename (str): Name of the file to save the results.
        """
        with open(filename, 'w') as file:
            file.write(f"Number of sentences: {self.count_sentences()}\n")
            file.write("Number of sentences by type:\n")
            sentence_types = self.count_sentence_types()
            for sentence_type, count in sentence_types.items():
                file.write(f"{sentence_type.capitalize()}: {count}\n")
            file.write(f"Average sentence length: {self.average_sentence_length()}\n")
            file.write(f"Average word length: {self.average_word_length()}\n")
            file.write(f"Number of smileys: {self.count_smileys()}\n")
            file.write(f"Words including characters from 'g' to 'o': {', '.join(self.find_words_in_range())}\n")
            file.write(f"Is valid email: {self.check_email_format()}\n")
            file.write(f"Number of words: {self.count_words()}\n")
            longest_word, longest_word_index = self.longest_word()
            file.write(f"Longest word: {longest_word}, Index: {longest_word_index}\n")
            file.write("Odd words: ")
            odd_words = self.odd_words()
            file.write(', '.join(odd_words))
