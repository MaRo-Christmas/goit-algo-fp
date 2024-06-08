
from linked_list_FP import LinkedList, Node

def merge_sort(linked_list):
    if linked_list.head is None or linked_list.head.next is None:
        return linked_list

    middle = get_middle(linked_list.head)
    next_to_middle = middle.next
    middle.next = None

    left = LinkedList()
    left.head = linked_list.head

    right = LinkedList()
    right.head = next_to_middle

    left = merge_sort(left)
    right = merge_sort(right)

    sorted_list = merge(left, right)
    return sorted_list

def get_middle(node):
    if not node:
        return node

    slow = node
    fast = node

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def merge(left, right):
    result = LinkedList()
    dummy = Node(0)
    tail = dummy

    left_current = left.head
    right_current = right.head

    while left_current and right_current:
        if left_current.data <= right_current.data:
            tail.next = left_current
            left_current = left_current.next
        else:
            tail.next = right_current
            right_current = right_current.next
        tail = tail.next

    tail.next = left_current if left_current else right_current
    result.head = dummy.next
    return result

# Приклад використання
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(4)
    ll.append(2)
    ll.append(1)
    ll.append(3)
    print("Несортований список:")
    ll.print_list()

    sorted_ll = merge_sort(ll)
    print("Відсортований список:")
    sorted_ll.print_list()
