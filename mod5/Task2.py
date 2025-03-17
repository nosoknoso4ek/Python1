class Node:
    """
    Вспомогательный класс для узлов списка
    """
    def __init__(self, data):
        self.data = data  # храним информацию
        self.nref = None  # ссылка на следующий узел
        self.pref = None  # ссылка на предыдущий узел

class Queue:
    """
    Основной класс для очереди
    """

    def __init__(self):
        self.start = None  # ссылка на начало очереди
        self.end = None  # ссылка на конец очереди

    def pop(self):
        """
        Возвращает элемент из начала списка с удалением его из списка
        """
        if self.start is None:
            return None  # Очередь пуста
        val = self.start.data
        self.start = self.start.nref  # Перемещаем начало на следующий узел
        if self.start is not None:
            self.start.pref = None  # Убираем ссылку на предыдущий узел
        else:
            self.end = None  # Если очередь стала пустой, обнуляем конец
        return val

    def push(self, val):
        """
        Добавляет элемент val в конец списка
        """
        new_node = Node(val)  # Создаем новый узел
        if self.end is None:  # Если очередь пуста
            self.start = new_node
            self.end = new_node
        else:
            new_node.pref = self.end  # Устанавливаем ссылку на предыдущий узел
            self.end.nref = new_node  # Устанавливаем ссылку на новый узел
            self.end = new_node  # Новый узел становится концом очереди

    def insert(self, n, val):
        """
        Вставляет элемент val между элементами с номерами n-1 и n
        """
        if n <= 0:
            return  # Некорректный индекс
        current = self.start
        count = 0
        while current and count < n:
            current = current.nref
            count += 1
        if current is None and count != n:
            return  # Некорректный индекс
        new_node = Node(val)
        if current is None:  # Вставка в конец
            self.push(val)
        else:
            new_node.nref = current
            new_node.pref = current.pref
            if current.pref is not None:
                current.pref.nref = new_node
            else:
                self.start = new_node  # Вставка в начало
            current.pref = new_node

    def print(self):
        """
        Выводит на печать содержимое очереди
        """
        current = self.start
        while current:
            print(current.data, end=" ")
            current = current.nref
        print()  # Переход на новую строку

# Пример использования
queue = Queue()
queue.push(10)
queue.push(20)
queue.push(30)
queue.print()  # Вывод: 10 20 30
queue.insert(1, 15)
queue.print()  # Вывод: 10 15 20 30
print(queue.pop())  # Вывод: 10
queue.print()  # Вывод: 15 20 30