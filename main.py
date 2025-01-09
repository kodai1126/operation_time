import time
import random
from my_stack import Stack
from my_queue import Queue
from linked_list import LinkedList
from maxheap import MaxHeap
from bst import BST

def nanosec_to_sec(ns):
    BILLION = 1_000_000_000
    return ns/BILLION

#Popping a single item from a stack
def pop_single_stack():
    #list for the number of elements
    pop_single_stack_element = list(range(1000, 100001, 1000))
    pop_single_stack_time = []
    for n in pop_single_stack_element:
        #create a stack
        my_stack = Stack()
        for i in range(n):
            my_stack.push(i)
        #timer start
        start_time = time.process_time_ns()
        my_stack.pop()
        #timer end
        end_time = time.process_time_ns()
        total_time = end_time - start_time
        pop_single_stack_time.append(nanosec_to_sec(total_time))
    return pop_single_stack_element, pop_single_stack_time

#Popping all items from a stack
def pop_all_stack():
    pop_all_stack_elements = list(range(1000, 100001, 1000))
    pop_all_stack_time = []
    for n in pop_all_stack_elements:
        my_stack = Stack()
        for i in range(n):
            my_stack.push(i)
        start_time = time.process_time_ns()
        #pop all
        for i in range(n):
            my_stack.pop()
        end_time = time.process_time_ns()
        total_time = end_time - start_time
        pop_all_stack_time.append(nanosec_to_sec(total_time))
    return pop_all_stack_elements, pop_all_stack_time

#Queue's enqueue
def queue_enqueue():
    queue_enqueue_elements = list(range(1000, 100001, 1000))
    queue_enqueue_time = []

    for n in queue_enqueue_elements:
        my_queue = Queue()
        for i in range(n):
            my_queue.enqueue(i)
        start_time = time.process_time_ns()
        #enqueue
        my_queue.enqueue(0)
        end_time = time.process_time_ns()
        total_time = end_time - start_time
        queue_enqueue_time.append(nanosec_to_sec(total_time))
    return queue_enqueue_elements, queue_enqueue_time

#Linked List get_entry at specifically the last index
def linkedlist_get_last():
    #when i generate graph, i used list(range(1000, 10001, 1000))since it took too much time
    linkedlist_get_last_elements = list(range(1000, 100001, 1000))
    linkedlist_get_last_time = []

    for n in linkedlist_get_last_elements:
        my_list = LinkedList()
        for i in range(n):
            my_list.insert(i, i)
        start_time = time.process_time_ns()
        my_list.get_entry(my_list.length()-1)
        end_time = time.process_time_ns()
        total_time = end_time - start_time
        linkedlist_get_last_time.append(nanosec_to_sec(total_time))
    return linkedlist_get_last_elements, linkedlist_get_last_time

#Printing all elements in a LinkedList using get_entry
def print_all_linkedlist():
    #when i generate graph, i used list(range(1000, 10001, 1000))since it took too much time
    print_all_linkedlist_elements = list(range(1000, 100001, 1000)) 
    print_all_linkedlist_time = []
    for n in print_all_linkedlist_elements:
        my_list = LinkedList()
        for i in range(n):
            my_list.insert(i, i)
        start_time = time.process_time_ns()
        for i in range(n):
            print(my_list.get_entry(i))
        end_time = time.process_time_ns()
        total_time = end_time - start_time
        print_all_linkedlist_time.append(nanosec_to_sec(total_time))
    return print_all_linkedlist_elements, print_all_linkedlist_time

#Adding a value to a Max Heap (our list-based implementation)
def add_maxheap():
    add_maxheap_elements = list(range(1000, 100001, 1000)) 
    add_maxheap_time = []

    for n in add_maxheap_elements:
        my_maxheap = MaxHeap()
        for i in range(n):
            my_maxheap.insert(i)
        start_time = time.process_time_ns()
        my_maxheap.insert(n+1)
        end_time = time.process_time_ns()
        total_time = (end_time - start_time)
        add_maxheap_time.append(nanosec_to_sec(total_time))
    return add_maxheap_elements, add_maxheap_time

#Searching for a value in a BST (our node-based implementation)
def search_bst():
    search_bst_elements = list(range(1000, 100001, 1000)) 
    search_bst_time = []

    for n in search_bst_elements:
        my_bst = BST()
        for i in range(n):
            random_value = random.randint(0, n)
            my_bst.insert(random_value)
        key = n // 2
        start_time = time.process_time_ns()
        my_bst.search(key)
        end_time = time.process_time_ns()
        total_time = end_time - start_time
        search_bst_time.append(nanosec_to_sec(total_time))
    return search_bst_elements, search_bst_time


'''
Generating Graph
uncomment the following code
also change list(range(1000, 100001, 1000)) -> list(range(1000, 100001, 1000)) for linkedlist
otherwise, it takes significant amount of time to generate the graph
'''

#generating graph by using matplotlib
import matplotlib.pyplot as plt
def generate_graph(title, xlabel, ylabel, elements, loop_times):
    plt.figure(figsize = (10,6))
    plt.plot(elements, loop_times, marker = 'o', linestyle='-', color = 'b')
    plt.title(title, fontsize = 14)
    plt.xlabel(xlabel, fontsize = 12)
    plt.ylabel(ylabel, fontsize=12)
    plt.grid(True)
    plt.show()


pop_single_stack_elements, pop_single_stack_time = pop_single_stack()
generate_graph("Popping a single item from a stack", 'element', 'time', pop_single_stack_elements, pop_single_stack_time)

pop_all_stack_elements, pop_all_stack_time = pop_all_stack()
generate_graph("Popping all items from a stack", 'element', 'time', pop_all_stack_elements, pop_all_stack_time)

queue_enqueue_elements, queue_enqueue_time = queue_enqueue()
generate_graph("Queue's enqueue", 'element', 'time', queue_enqueue_elements, queue_enqueue_time)

linkedlist_get_last_elements, linkedlist_get_last_time = linkedlist_get_last()
generate_graph("Linked List get_entry at specifically the last index", 'element', 'time', linkedlist_get_last_elements, linkedlist_get_last_time)

add_maxheap_elements, add_maxheap_time = add_maxheap()
generate_graph("Adding a value to a Max Heap (our list-based implementation)", 'element', 'time', add_maxheap_elements, add_maxheap_time)

search_bst_elements, search_bst_time = search_bst()
generate_graph("Searching for a value in a BST (our node-based implementation)", 'element', 'time', search_bst_elements, search_bst_time)   

print_all_linkedlist_elements, print_all_linkedlist_time = print_all_linkedlist()
generate_graph("Printing all elements in a LinkedList using get_entry", 'element', 'time', print_all_linkedlist_elements, print_all_linkedlist_time)