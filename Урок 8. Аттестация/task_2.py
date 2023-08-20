"""
Задание 2.
Доработайте пример структуры "дерево",
рассмотренный на уроке.
Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).
Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""

# Добавлена валидация значений левого и правого потомка для корня дерева. Я ещё думал как бы сделать валидацию для
# всех последующих потомков, но для этого надо переписать половину скрипта, если не весь, и к тому же потом я посмотрел
# пример и в нём этого нет, так что оставил валидацию только для правого и левого потомков корня.


class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    # добавить левого потомка
    def insert_left(self, new_node):
        if new_node < self.get_root_val():
            # если у узла нет левого потомка
            if self.left_child is None:
                # тогда узел просто вставляется в дерево
                # формируется новое поддерево
                self.left_child = BinaryTree(new_node)
            # если у узла есть левый потомок
            else:
                # тогда вставляем новый узел
                tree_obj = BinaryTree(new_node)
                # и спускаем имеющегося потомка на один уровень ниже
                tree_obj.left_child = self.left_child
                self.left_child = tree_obj
        else:
            print("Impossible. Too big")

    # добавить правого потомка
    def insert_right(self, new_node):
        if new_node > self.get_root_val():
            # если у узла нет правого потомка
            if self.right_child is None:
                # тогда узел просто вставляется в дерево
                # формируется новое поддерево
                self.right_child = BinaryTree(new_node)
            # если у узла есть правый потомок
            else:
                # тогда вставляем новый узел
                tree_obj = BinaryTree(new_node)
                # и спускаем имеющегося потомка на один уровень ниже
                tree_obj.right_child = self.right_child
                self.right_child = tree_obj
        else:
            print("Impossible. Too small")

    # метод доступа к правому потомку
    def get_right_child(self):
        if self.right_child:
            return self.right_child
        else:
            print('Нет правого потомка')

    # метод доступа к левому потомку
    def get_left_child(self):
        if self.left_child:
            return self.left_child
        else:
            print('Нет левого потомка')

    # метод установки корня
    def set_root_val(self, obj):
        if self.left_child.root < obj < self.right_child.root:
            self.root = obj
        else:
            print('Impossible value')

    # метод доступа к корню
    def get_root_val(self):
        if self.root:
            return self.root
        else:
            print('Нет корня')


r = BinaryTree(8)
r.insert_left(12)
r.insert_left(4)
r.insert_right(2)
r.insert_right(12)
print(r.get_root_val())
print(r.left_child.get_left_child())
print(r.left_child.get_right_child())