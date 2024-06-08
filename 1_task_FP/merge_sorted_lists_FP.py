
from linked_list_FP import LinkedList, Node

def merge_sorted_lists(ll1, ll2):
    dummy = Node(0)
    tail = dummy

    current1 = ll1.head
    current2 = ll2.head

    while current1 and current2:
        if current1.data <= current2.data:
            tail.next = current1
            current1 = current1.next
        else:
            tail.next = current2
            current2 = current2.next
        tail = tail.next

    tail.next = current1 if current1 else current2

    merged_list = LinkedList()
    merged_list.head = dummy.next
    return merged_list

# Приклад використання
if __name__ == "__main__":
    ll1 = LinkedList()
    ll1.append(1)
    ll1.append(3)
    ll1.append(5)

    ll2 = LinkedList()
    ll2.append(2)
    ll2.append(4)
    ll2.append(6)

    print("Перший відсортований список:")
    ll1.print_list()
    print("Другий відсортований список:")
    ll2.print_list()

    merged_ll = merge_sorted_lists(ll1, ll2)
    print("Об'єднаний відсортований список:")
    merged_ll.print_list()
