
from typing import Any


class Node:
    def __init__(self, value: Any = None, next=None):
        self.value: Any = value
        self.next: 'Node' = next


class LinkedList:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None

    # umieści nowy węzeł na początku listy
    def push(self, value: Any) -> None:
        new = Node(value, self.head)
        self.head = new

    # umieści nowy węzeł na końcu listy
    def append(self, value: Any) -> None:
        if self.head is None:
            self.head = Node(value, None)
            return
        a = self.head
        while a.next:
            a = a.next

        a.next = Node(value, None)

    # zwróci węzeł znajdujący się na wskazanej pozycji
    def node(self, at: int) -> Node:
        a = self.head
        licznik = 0
        while a is not None:
            if licznik == at:
                return a
            licznik += 1
            a = a.next

    # #wstawi nowy węzeł tuż za węzłem wskazanym w parametrze
    # def insert(self, value: Any, after: Node) -> None:
    #     a = self.head
    #     while a is not None:
    #         if after==a.value:
    #             break
    #         a = a.next
    #     if a is None:
    #         print("tego elementu nie ma na liscie")
    #     else:
    #         nowe = Node(value)
    #         nowe.next = a.next
    #         a.next = nowe

    def insert(self, value: Any, after: Node) -> None:
        node = Node(value)
        if after.next is not None:
            a = after.next
            after.next = node
            node.next = a
        else:
            after.next = node
            self.tail = node

    # usunie pierwszy element z listy i go zwróci
    def pop(self) -> Any:
        if self.head is not None:
            a = self.head
            print(f'element usuniety {self.head.value}')
            self.head = self.head.next
            return a.value

    # usunie ostatni element z listy i go zwróci
    def remove_last(self) -> Any:
        if self.head is not None:
            a = self.head
            while a.next.next is not None:
                a = a.next
            print(f'element usuniety {a.next.value}')
            a.next = None

    # usunie z listy następnik węzła przekazanego w parametrze
    def remove(self, after: Node) -> Any:
        if after == self.head.value:
            self.head = self.head.next
            return
        licznik = 0
        a = self.head
        while a:
            if licznik == after:
                a.next = a.next.next
                break

            a = a.next
            licznik += 1

    # wypisz
    def print(self):
        a = self.head
        b = ''
        while a:
            b += str(a.value)
            if a.next is not None:
                b += ' ---> '
            a = a.next
        print(b)

    # dlugosc
    def __len__(self):
        licznik = 0
        a = self.head
        while a:
            licznik += 1
            a = a.next
        print(f'ilosc elementow w liscie: {licznik}')
        return licznik

    def __str__(self):
        a = self.head
        b = ''
        while a:
            b += str(a.value)
            if a.next is not None:
                b += ' ---> '
            a = a.next
        return (b)

###############################################################
# Stack


class Stack:
    def __init__(self):
        self._storage: LinkedList = LinkedList()

    # umieści nową wartość "na szczycie" stosu,
    # czyli zostanie dodana na końcu wewnętrznej listy
    def push(self, element: Any) -> None:
        return self._storage.push(element)

    # zwróci i usunie wartość ze szczytu stosu
    def pop(self) -> Any:
        return self._storage.pop()


    def print(self):
        a = self._storage.head
        while a is not None:
            print(a.value)

    def __len__(self):
        return self._storage.__len__()

#######################################################
# Kolejka

class Queue:
    def __init__(self):
        self._storage: LinkedList = LinkedList()

    # zwróci wartość pierwszego elementu w kolejce
    def peek(self) -> Any:
        return self._storage.head.value

    # umieści nowy element na końcu kolejki
    def enqueue(self, element: Any) -> None:
        return self._storage.append(element)

    # zwróci i usunie pierwszy element w kolejce
    def dequeue(self) -> Any:
        return self._storage.pop()

    def print(self):
        a = self._storage.head
        b = ''
        while a:
            b += str(a.value)
            if a.next is not None:
                b += ', '
            a = a.next
        print(b)

    def __len__(self):
        return self._storage.__len__()

    def __str__(self):
        a = self._storage.head
        b = ''
        while a:
            b += str(a.value)
            if a.next is not None:
                b += ', '
            a = a.next
        return b

##################################################
# TEST LISTA

# list_ = LinkedList()
# list_.push(1)
# list_.push(0)
# list_.append(9)
# list_.append(10)


# middle_node = list_.node(at=1)
# list_.insert(5, after=middle_node)

# list_.print()
# list_.remove_last()
# list_.remove(1)
# list_.pop()
# # list_.node()
# # list_.insert(5,1)
# list_.print()
# list_.len()

##################################################
# TEST STOS

# stack = Stack()
# assert len(stack) == 0
# stack.push(3)
# stack.push(10)
# stack.push(1)
# assert len(stack) == 3
# top_value = stack.pop()
# assert top_value == 1
# assert len(stack) == 2


##################################################
# TEST KOLEJKA

# queue = Queue()
# assert len(queue) == 0
# queue.enqueue('klient1')
# queue.enqueue('klient2')
# queue.enqueue('klient3')
# assert str(queue) == 'klient1, klient2, klient3'
# client_first = queue.dequeue()
# assert client_first == 'klient1'
# assert str(queue) == 'klient2, klient3'
# assert len(queue) == 2
