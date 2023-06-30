class WordCounter:
    # sentence = "This is a test of the emergency broadcast system"
    def __init__(self, sentence):
        self.sentence = sentence
        self.word_count = None
    def count_words(self):
        self.word_count = len(self.sentence.split())
    def get_word_count(self):
        return self.word_count
    def get_shortest_word(self):
        words = self.sentence.split()
        if words:
            return min(len(word) for word in words)
    def get_longest_word(self):
        words = self.sentence.split()
        if words:
            return max(len(word) for word in words)





    # print(word_count.get_word_count())  # Returns the number of all the words.
    # print(word_count.get_shortest_word())  # Returns the length of the shortest word.
    # print(word_count.get_longest_word())





    # def count_words(self):
    #     with open(self.sentence, 'r') as f:
    #         for line in f:
    #             for word in line.split():
    #                 if word in self.word_count:
    #                     self.word_count[word] += 1
    #                 else:
    #                     self.word_count[word] = 1
    #
    # def print_word_count(self):
    #     for word, count in self.word_count.items():
    #         print(word, count)
    #
    # def get_shortest_word(self):
    #     return min(self.word_count, key=len)
    #
    # def get_longest_word(self):
    #     return max(self.word_count, key=len)