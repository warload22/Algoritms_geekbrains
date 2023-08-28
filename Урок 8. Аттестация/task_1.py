"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою!!! версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.
2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.
"""

# Реализовано через ООП


from collections import Counter



class Node:

    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.frequency = self.left.frequency + self.right.frequency


class Symbol:

    def __init__(self, symbol, frequency):
        self.symbol = symbol
        self.frequency = frequency
        self.code = ''

    def __str__(self):
        return self.symbol


class Phrase:

    def __init__(self, phrase):
        self.tree = []
        self.symbols = {}
        self.frequency_count(phrase)
        self.create_tree()
        self.symbols_code(self.tree)
        self.code = self.phrase_code(phrase)

    def frequency_count(self, phrase):
        count_dict = Counter(phrase)
        for i in count_dict:
            symbol = Symbol(i, count_dict[i])
            self.tree.append(symbol)
            self.symbols[i] = symbol
        self.tree.sort(key=lambda k: f'{k.frequency}')

    def frequency_sort(self, node):
        self.tree.insert(0, node)
        for i in range(len(self.tree) - 1):
            if self.tree[i].frequency > self.tree[i + 1].frequency:
                self.tree[i], self.tree[i + 1] = self.tree[i + 1], self.tree[i]
            else:
                break

    def create_tree(self):
        while len(self.tree) > 1:
            node = Node(self.tree[0], self.tree[1])
            self.tree = self.tree[2:]
            self.frequency_sort(node)
        self.tree = self.tree[0]

    def symbols_code(self, tree, code=''):
        if isinstance(tree, Symbol):
             tree.code = code
        else:
            self.symbols_code(tree.left, code + '0')
            self.symbols_code(tree.right, code + '1')

    def phrase_code(self, phrase):
        code = ''
        for i in phrase:
            code += ' ' + self.symbols[i].code
        return code

    def __str__(self):
        return self.code


print(Phrase(input('Введите текст: ')))
