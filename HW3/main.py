import math 


def swap_elements(index_1, index_2, list):
    temp = list[index_1]
    list[index_1] = list[index_2]
    list[index_2] = temp


def get_parent(child_i):
    return math.floor((child_i - 1) / 2)


def get_left_child(index):
    return (2 * index) + 1


def get_right_child(index):
    return (2 * index) + 2


def heap_insert(element, list):
    list.append(element)
    i = len(list) - 1
    parent_i = get_parent(i)
    while i > 0 and list[parent_i] > list[i]:
        swap_elements((parent_i), i, list)
        i = parent_i
        parent_i = get_parent(i)


def create_heap(unordered_list):
    heap = []
    for num in unordered_list:
        heap_insert(num, heap)
    print("heap: ", heap)
    return heap
    

def heap_remove(heap):
    max_index = len(heap) - 1
    temp = heap[0]
    heap[0] = heap[max_index]
    heap.pop() 
    max_index = max_index - 1
    i = 0
    while i <= max_index:
        left = get_left_child(i)
        right = get_right_child(i)
        if right <= max_index:  # if there are two internal children
            if heap[i] <= heap[left] and heap[i] <= heap[right]:
                return temp  # heap order has been restored
            else:
                j = left if heap[left] < heap[right] else right
                swap_elements(i, j, heap)
                i = j
        else:  # node has 0 or 1 children
            if (left <= max_index):
                if heap[i] > heap[left]:
                    swap_elements(i, left, heap)
            return temp
    return temp


def create_sorted_list(heap):
    sorted_list = []
    while len(heap) > 0:
        sorted_list.append(heap_remove(heap))  # heap size decreases in remove
    return sorted_list


def heapsort(hlist):
    if hlist is None:
        return None
    if len(hlist) == 0:
        return []
    heap = create_heap(hlist)
    return create_sorted_list(heap)
