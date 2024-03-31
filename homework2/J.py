import sys


class Device:
    inventory = []
    sharedUpdates = []

    def __init__(self, update_count, gadget_count):
        self.pending_updates = [False] * update_count
        self.importance = [0] * gadget_count
        self.incoming_requests = []
        self.completed_updates = 0
        self.selected_update = -1
        self.iteration_count = 0
        self.index = len(Device.inventory)
        self.is_request_approved = False
        self.requesting_gadget_index = -1
        Device.inventory.append(self)

    def select_update(self):
        self.selected_update = -1
        least_shared_updates = sys.maxsize
        for i, status in enumerate(self.pending_updates):
            if not status and Device.sharedUpdates[i] < least_shared_updates:
                least_shared_updates = Device.sharedUpdates[i]
                self.selected_update = i
        if self.selected_update != -1:
            self.iteration_count += 1

    def find_request_source(self):
        if self.selected_update == -1:
            return
        least_updates = sys.maxsize
        source_gadget = None
        for gadget in Device.inventory:
            if gadget.pending_updates[self.selected_update]:
                if gadget.completed_updates < least_updates:
                    source_gadget = gadget
                    least_updates = gadget.completed_updates
        if source_gadget:
            source_gadget.incoming_requests.append(self)

    def evaluate_requests(self):
        min_completed_updates = sys.maxsize
        best_request_index = -1
        highest_importance = -1
        for i, gadget in enumerate(self.incoming_requests):
            if self.importance[gadget.index] > highest_importance:
                best_request_index = gadget.index
                min_completed_updates = gadget.completed_updates
                highest_importance = self.importance[gadget.index]
            elif self.importance[gadget.index] == highest_importance:
                if min_completed_updates > gadget.completed_updates:
                    best_request_index = gadget.index
                    min_completed_updates = gadget.completed_updates
        self.incoming_requests = []
        if best_request_index != -1:
            gadget = Device.inventory[best_request_index]
            gadget.is_request_approved = True
            gadget.requesting_gadget_index = self.index

    def approve_request(self):
        if not self.is_request_approved:
            return
        self.completed_updates += 1
        self.pending_updates[self.selected_update] = True
        Device.sharedUpdates[self.selected_update] += 1
        self.importance[self.requesting_gadget_index] += 1
        self.is_request_approved = False

def orchestrate(n, k):
    Device.inventory.clear()
    Device.sharedUpdates = [1] * k
    for _ in range(n):
        Device(k, n)
    Device.inventory[0].completed_updates = k
    Device.inventory[0].pending_updates = [True] * k
    while True:
        operation_complete = 0
        for gadget in Device.inventory:
            if gadget.completed_updates == k:
                operation_complete += 1
                continue
            gadget.select_update()
        if operation_complete == n:
            break

        for gadget in Device.inventory:
            if gadget.completed_updates == k:
                continue
            gadget.find_request_source()

        for gadget in Device.inventory:
            if not gadget.incoming_requests:
                continue
            gadget.evaluate_requests()

        for gadget in Device.inventory:
            if not gadget.is_request_approved:
                continue
            gadget.approve_request()

    results = [gadget.iteration_count for gadget in Device.inventory]
    return results

def main(input_filename, output_filename):
    with open(input_filename, 'r') as input_file:
        n, k = map(int, input_file.readline().split())

    outcomes = orchestrate(n, k)

    with open(output_filename, 'w') as output_file:
        output_file.write(' '.join(map(str, outcomes[1:])))

if __name__ == "__main__":
    main("input.txt", "output.txt")
