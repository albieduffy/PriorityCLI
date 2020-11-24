class MinHeap:
    def __init__(self):
        self.heap_list = [None]
        self.count = 0

    def parent_idx(self, idx):
        return idx // 2

    def left_child_idx(self, idx):
        return idx * 2

    def right_child_idx(self, idx):
        return idx * 2 + 1

    def child_present(self, idx):
        return self.left_child_idx(idx) <= self.count

    def add(self, element):
        self.count += 1
        self.heap_list.append(element)
        self.heapify_up()

    def retrieve_min(self):
        if self.count == 0:
            print('No items in queue')
            return None
        else:
            min = self.heap_list[1]
            self.heap_list[1] = self.heap_list[self.count]
            self.count -= 1
            self.heap_list.pop()
            self.heapify_down()
            return min

    def heapify_up(self):
        idx = self.count
        while self.parent_idx(idx) > 0:
            if self.heap_list[self.parent_idx(idx)].get_priority() > self.heap_list[idx].get_priority():
                tmp = self.heap_list[self.parent_idx(idx)]
                self.heap_list[self.parent_idx(idx)] = self.heap_list[idx]
                self.heap_list[idx] = tmp
            idx = self.parent_idx(idx)

    def heapify_down(self):
        idx = 1
        while self.child_present(idx):
            smaller_child_idx = self.get_smaller_child_idx(idx)
            if self.heap_list[idx].get_priority() > self.heap_list[smaller_child_idx].get_priority():
                tmp = self.heap_list[self.smaller_child_idx]
                self.heap_list[smaller_child_idx] = self.heap_list[idx]
                self.heap_list[idx] = tmp
            idx = smaller_child_idx

    def get_smaller_child_idx(self, idx):
        if self.right_child_idx(idx) > self.count:
            return self.left_child_idx(idx)
        else:
            left_child = self.heap_list[self.left_child_idx(idx)].get_priority()
            right_child = self.heap_list[self.right_child_idx(idx)].get_priority()
            if left_child < right_child:
                return self.left_child_idx(idx)
            else:
                return self.right_child_idx(idx)

    def get_count(self):
        return self.count

    def get_current_task(self):
        return self.heap_list[1].get_task()

class Node:
    def __init__(self, priority, task):
        self.priority = int(priority)
        self.task = task

    def get_priority(self):
        return self.priority

    def get_task(self):
        return self.task

    def set_priority(self, priority):
        self.priority = priority

    def set_task(self, task):
        self.task = task
