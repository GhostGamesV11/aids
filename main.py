from typing import Any

class Node:
    def __init__(self, value: Any = None, next = None):
        self.value: Any = value
        self.next: 'Node' = next

class LinkedList:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None



    #umieści nowy węzeł na początku listy
    def push(self,value:Any) -> None:
        new = Node(value, self.head)
        self.head = new


    #umieści nowy węzeł na końcu listy
    def append(self,value:Any)-> None:
        if self.head is None:
            self.head = Node(value ,None)
            return
        a = self.head
        while a.next:
            a = a.next

        a.next = Node(value,None)

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

    def insert(self, value: Any, after: Node) ->None:
        node = Node(value)
        if after.next is not None:
            a = after.next
            after.next = node
            node.next = a
        else:
            after.next = node
            self.tail = node


    #usunie pierwszy element z listy i go zwróci
    def pop(self) -> Any:
        if self.head is None:
            print("blad")
        else:
            print(f'element usuniety {self.head.value}')
            self.head = self.head.next

    #usunie ostatni element z listy i go zwróci
    def remove_last(self) -> Any:
        if self.head is None:
            print("blad")
        else:
            a = self.head
            while a.next.next is not None:
                a = a.next
            print(f'element usuniety {a.next.value}')
            a.next = None

    #usunie z listy następnik węzła przekazanego w parametrze
    def remove(self,after: Node) -> Any:
        if self.head is None:
            print('lista jest pusta')
        if after==self.head.value:
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


    #wypisz
    def print(self):
        # if self.head is None:
        #     print("lista jest pusta")
        #     return
        a = self.head
        b = ''
        while a:
            b += str(a.value)
            if a.next is not None:
                b += ' ---> '
            a = a.next
        print(b)

    # dlugosc
    def len(self):
        licznik = 0
        a = self.head
        while (a):
            licznik += 1
            a = a.next
        return print(f'ilosc elementow w liscie: {licznik}')



###############################################################
# Stack


class Stack:
    def __init__(self):
        self.head = _storage = LinkedList



#umieści nową wartość "na szczycie" stosu,
# czyli zostanie dodana na końcu wewnętrznej listy
#     def push(self, element: Any) -> None:
#         element = self.element
#         self._storage.append(element)



#zwróci i usunie wartość ze szczytu stosu
    def pop(self) -> Any:
        pass


    # def print(self):
    #     # if self.head is None:
    #     #     print("lista jest pusta")
    #     #     return
    #     a = LinkedList
    #     b = ''
    #     while a:
    #         b += str(a.)
    #         if a.next is not None:
    #             b += ' ---> '
    #         a = a.next
    #     print(b)
    #
    # def len(self):
    #     licznik = 0
    #     a = self.head
    #     while (a):
    #         licznik += 1
    #         a = a.next
    #     return print(f'ilosc elementow w liscie: {licznik}')





#######################################################
# Kolejka

class Queue:
    def __init__(self):
        self.front = self.rear = None


    #zwróci wartość pierwszego elementu w kolejce
    def peek(self) -> Any:
        pass

    #umieści nowy element na końcu kolejki
    def  enqueue(self, element: Any) -> None:
        pass

    #zwróci i usunie pierwszy element w kolejce
    def  dequeue(self) -> Any:
        pass


##################################################
# TEST LISTA

list_ = LinkedList()
list_.push(1)
list_.push(0)
list_.append(9)
list_.append(10)


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
# stack.print()
# stack.len()



##################################################
# TEST KOLEJKA
