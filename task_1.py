import random


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None
 
    def __str__(self):
        result = "head -> "
        current = self.head
        while current:
            result += str(current.data) + " -> "
            current = current.next
        result += "None"
        return result

#-------------------------------ВИКОНАННЯ ЗАВДАННЯ---------------------------------------#    

def get_reversed(list: LinkedList) -> LinkedList:
    '''
    Створення нового реверсованого зв'язаного списку
    '''
    result = LinkedList()
    current = list.head
    while current:
        result.insert_at_beginning(current.data)
        current = current.next
    return result

def merge_sort(list: LinkedList):
    '''
    Розбиваємо список на 2 частини
    '''
    current = list.head
    if not current.next:
        return list
    
    left_half = LinkedList()
    right_half = LinkedList()

    while current:
        left_half.insert_at_end(current.data)
        current = current.next
        if current:
            right_half.insert_at_end(current.data)
            current = current.next

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left: LinkedList, right: LinkedList):
    merged = LinkedList()
    left_current = left.head
    right_current = right.head

    # Спочатку об'єднуємо менші елементи
    while left_current and right_current:
        if left_current.data <= right_current.data:
            merged.insert_at_end(left_current.data)
            left_current = left_current.next
        else:
            merged.insert_at_end(right_current.data)
            right_current = right_current.next

    # Якщо в лівій або правій половині залишилися елементи, 
	# додаємо їх до результату
    while left_current:
        merged.insert_at_end(left_current.data)
        left_current = left_current.next

    while right_current:
        merged.insert_at_end(right_current.data)
        right_current = right_current.next

    return merged

def merge_two_sorted_lists(lst1: LinkedList, lst2: LinkedList) -> LinkedList:
    '''
    Оскільки списки вже відсортовані, то достатньо викликати метод "merge"
    '''
    return merge(lst1, lst2)

if __name__ == "__main__":
    llist = LinkedList()

    # Вставляємо вузли в початок
    llist.insert_at_beginning(5)
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(15)

    # Вставляємо вузли в кінець
    llist.insert_at_end(20)
    llist.insert_at_end(25)

    # Друк зв'язного списку
    print(f"\nЗв'язний список:\n{llist}")

    # Створюємо інвертований список
    reversed_list = get_reversed(llist)
    print(f"\nЗв'язний реверсований список:\n{reversed_list}")

    # Видаляємо вузол
    llist.delete_node(10)

    print(f"\nЗв'язний список після видалення вузла з даними 10:\n{llist}")

    # Пошук елемента у зв'язному списку
    print("\nШукаємо елемент 15:")
    element = llist.search_element(15)
    if element:
        print(element.data)

    # Відсортований інвертований список
    sorted_list = merge_sort(reversed_list)
    print(f"\nВідсортований зв'язний реверсований список:\n{sorted_list}")

    # 2 відсортовані списки
    lst1 = LinkedList()
    for _ in range (5):
        lst1.insert_at_end(random.randint(0, 100))
    lst1 = merge_sort(lst1)

    lst2 = LinkedList()
    for _ in range (5):
        lst2.insert_at_end(random.randint(0, 100))
    lst2 = merge_sort(lst2)

    print(f"\nДва відсортованих списки:\n{lst1}\n{lst2}")

    two_sorted_lists = merge_two_sorted_lists(lst1, lst2)
    print(f"\nОб'єднанні два відсортованих списки:\n{two_sorted_lists}")