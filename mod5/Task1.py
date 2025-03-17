class Node:
    """
    Вспомогательный класс для узлов списка
    """
    def __init__(self, data):
        self.data = data  # храним информацию
        self.pref = None  # ссылка на предыдущий узел

class Stack:
    """
    Основной класс для стека
    """

    def __init__(self):
        self.end = None  # ссылка на конец стека

    def pop(self):
        """
        Возвращает последний элемент из списка с удалением его из списка
        """
        if self.end is None:
            return None  # Стек пуст
        val = self.end.data
        self.end = self.end.pref  # Перемещаем ссылку на предыдущий узел
        return val

    def push(self, val):
        """
        Добавляет элемент val в конец списка
        """
        new_node = Node(val)  # Создаем новый узел
        new_node.pref = self.end  # Устанавливаем ссылку на предыдущий узел
        self.end = new_node  # Новый узел становится концом стека

    def print(self):
        """
        Выводит на печать содержимое стека
        """
        current = self.end
        while current:
            print(current.data, end=" ")
            current = current.pref
        print()  # Переход на новую строку

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.print()
print(stack.pop())
stack.print()