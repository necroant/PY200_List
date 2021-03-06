from typing import Any, Sequence, Optional


class LinkedList:
    # noinspection PyUnresolvedReferences
    class Node:
        """
        Внутренний класс, класса LinkedList.
        Пользователь напрямую не работает с узлами списка, узлами оперирует список.
        """

        def __init__(self, value: Any, next_node: Optional["Node"] = None):
            """
            Создаем новый узел для односвязного списка
            :param value: Любое значение, которое помещено в узел
            :param next_node: следующий узел, если он есть
            """
            self.value = value
            self.next = next_node  # Вызывается сеттер

        @property
        def next(self):
            """Getter возвращает следующий узел связного списка"""
            return self.__next

        @next.setter
        def next(self, next_: Optional["Node"]):
            """Setter проверяет и устанавливает следующий узел связного списка"""
            if not isinstance(next_, self.__class__) and next_ is not None:
                msg = f"Устанавливаемое значение должно быть экземпляром класса {self.__class__.__name__} " \
                      f"или None, не {next_.__class__.__name__}"
                raise TypeError(msg)
            self.__next = next_

        def __repr__(self):
            """Метод должен возвращать строку, показывающую, как может быть создан экземпляр."""
            return f"Node({self.value}, {self.next})"

        def __str__(self):
            """Вызывается функциями str, print и format. Возвращает строковое представление объекта."""
            return f"{self.value}"

    def __init__(self, data: Sequence = None):
        """Конструктор связного списка"""
        self._len = 0
        self.head = None  # Node
        self.tail = None

        if data:
            if self.is_iterable(data):
                for value in data:
                    self.append(value)
            else:
                self.append(data)

    def __str__(self):
        """Вызывается функциями str, print и format. Возвращает строковое представление объекта."""
        result = []
        current_node = self.head

        for _ in range(self._len - 1):
            result.append(current_node.value)
            current_node = current_node.next

        result.append(current_node.value)

        return f"{result}"

    def __repr__(self):
        """Метод должен возвращать строку, показывающую, как может быть создан экземпляр."""
        if self.head is None:
            return f"LinkedList({self.head})"
        else:
            return f"LinkedList({self.head},{self.head.next})"

    def __len__(self):
        return self._len

    def __getitem__(self, index: int) -> Any:
        if index <= self._len:
            item = self.__find_item(index)
            return item
        else:
            raise IndexError(f"Index {index} out of bounds")

    def __setitem__(self, index, value):
        if index <= self._len:
            item = self.__find_item(index)
            item.value = value
        else:
            raise IndexError(f"Index {index} out of bounds")

    def __find_item(self, index: int) -> Any:
        current_node = self.head
        if not index == 0:
            for _ in range(index):
                current_node = current_node.next
        return current_node

    @staticmethod
    def __linked_nodes(left: Node, right: Optional[Node]) -> None:
        left.next = right

    def append(self, value: Any):
        """Добавление элемента в конец связного списка"""
        append_node = self.Node(value)
        if self.head is None:
            self.head = append_node
            self.tail = None
        else:
            tail = self.head
            for _ in range(self._len - 1):
                tail = tail.next
            self.__linked_nodes(tail, append_node)
            self.tail = tail
        self._len += 1

    def to_list(self) -> list:
        output = [self.head]
        if self._len > 0:
            current = self.head
            for _ in range(self._len):
                current = current.next
                output.append(current)

        return output

    def insert(self, index: int, value: Any) -> None:
        ...

    def clear(self) -> None:
        ...

    def index(self, value: Any) -> int:
        ...

    def remove(self, value: Any) -> None:
        ...

    def sort(self) -> None:
        ...

    @staticmethod
    def is_iterable(data) -> bool:
        """Метод для проверки является ли объект итерируемым"""
        try:
            _ = (e for e in data)
            return True
        except TypeError:
            return False


if __name__ == '__main__':
