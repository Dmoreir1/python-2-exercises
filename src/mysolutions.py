from ex5 import WordCounter
from ex6 import TaxMan
from ex7 import Calculator
from ex8 import CarCollector

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

    calculator1 = Calculator(4, 3)
    calculator1.add()
    print(calculator1.get_result())

    calculator2 = Calculator(4, 3)
    calculator2.sub()
    print(calculator2.get_result())

    calculator3 = Calculator(2, 3)
    calculator3.mul()
    print(calculator3.get_result())

    calculator4 = Calculator(8, 2)
    calculator4.div()
    print(calculator4.get_result())

    print(CarCollector.get_data())

main()




# if __name__ == '__main__':
#     main(sentence)

