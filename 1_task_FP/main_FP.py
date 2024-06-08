
from linked_list_FP import LinkedList
from reverse_list_FP import reverse_list
from merge_sort_FP import merge_sort
from merge_sorted_lists_FP import merge_sorted_lists

# Приклад використання реверсування списку
ll1 = LinkedList()
ll1.append(1)
ll1.append(2)
ll1.append(3)
ll1.append(4)
print("Оригінальний список:")
ll1.print_list()

reverse_list(ll1)
print("Реверсований список:")
ll1.print_list()

# Приклад використання сортування списку
ll2 = LinkedList()
ll2.append(4)
ll2.append(2)
ll2.append(1)
ll2.append(3)
print("Несортований список:")
ll2.print_list()

sorted_ll2 = merge_sort(ll2)
print("Відсортований список:")
sorted_ll2.print_list()

# Приклад використання об'єднання двох відсортованих списків
ll3 = LinkedList()
ll3.append(1)
ll3.append(3)
ll3.append(5)

ll4 = LinkedList()
ll4.append(2)
ll4.append(4)
ll4.append(6)

print("Перший відсортований список:")
ll3.print_list()
print("Другий відсортований список:")
ll4.print_list()

merged_ll = merge_sorted_lists(ll3, ll4)
print("Об'єднаний відсортований список:")
merged_ll.print_list()
