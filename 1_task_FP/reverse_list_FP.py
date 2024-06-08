
from linked_list_FP import LinkedList

def reverse_list(linked_list):
    prev = None
    current = linked_list.head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    linked_list.head = prev

# Приклад використання
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    print("Оригінальний список:")
    ll.print_list()

    reverse_list(ll)
    print("Реверсований список:")
    ll.print_list()
