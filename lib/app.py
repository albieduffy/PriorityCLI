from .MinHeap import MinHeap, Node

class CLI:
    def __init__(self):
        self.user_input = ''

    def start(self):
        priority_queue = MinHeap()
        while priority_queue.get_count() == 0:
            print('The queue is currently empty.')
            self.add_new_task(priority_queue)
        while priority_queue.get_count() > 0:
            print("""

            Your current task is:

            {}

            """.format(priority_queue.get_current_task()))
            options = ['add', 'done']
            user_choice = input('Select an option ("add" to add new task, "done" to complete current task): ')
            while user_choice not in options:
                user_choice = input('Please select a valid option (add or done): ')
            if user_choice == 'add':
                self.add_new_task(priority_queue)
            else:
                self.complete_task(priority_queue)

    def add_new_task(self, priority_queue):
        new_task = input('Add a task: ')
        task_priority = input('Set a priority for this task (1-5): ')
        priority_queue.add(Node(task_priority, new_task))

    def complete_task(self, priority_queue):
        completed_task = priority_queue.retrieve_min().get_task()
        print('{} completed.'.format(completed_task))
