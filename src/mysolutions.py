from ex5 import WordCounter
from ex6 import TaxMan

# def hello():
#     print('Hello exercises for Python II!')

sentence = "This is a test of the emergency broadcast system"
items = [
        {"id": 1, "desc": "clock", "price": 1.00},
        {"id": 2, "desc": "socks", "price": 2.00},
        {"id": 3, "desc": "razor", "price": 3.00},
    ]


def main():

    word_counter = WordCounter(sentence)
    word_counter.count_words()
    print(word_counter.get_word_count())  # Returns the number of all the words.
    print(word_counter.get_shortest_word())  # Returns the length of the shortest word.
    print(word_counter.get_longest_word())  # Returns the length of the longest word.

    tm = TaxMan(items, "10%")
    tm.calc_total()
    print(tm.get_total())




main()




# if __name__ == '__main__':
#     main(sentence)

