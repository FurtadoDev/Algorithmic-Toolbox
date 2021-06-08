# python3

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.count = 1


class Bst:
    def __init__(self):
        self.root = None

    def insert_node(self, data):
        count = 0
        if self.root is None:
            self.root = Node(data)
            count = self.root.count
        else:
            # pass in the current node and the data to be inserted into the recursive call
            count = self.insert_recursive(self.root, data)
        return count

    def insert_recursive(self, current_node, data):
        count = 0
        if data == current_node.data:
            current_node.count += 1
            count = current_node.count
        elif data < current_node.data:
            # recurse on the left side
            if current_node.left is None:
                current_node.left = Node(data)
                count = current_node.left.count
            else:
                count = self.insert_recursive(current_node.left, data)
        else:
            # recurse on the right side
            if current_node.right is None:
                current_node.right = Node(data)
                count = current_node.right.count
            else:
                count = self.insert_recursive(current_node.right, data)
        return count


def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0


def majority_element(elements):
    assert len(elements) <= 10 ** 5
    length_elements = len(elements)
    majority_length = length_elements / 2
    bst_tree = Bst()
    exists = 0
    for i in range(length_elements):
        temp_count = bst_tree.insert_node(elements[i])
        if temp_count > majority_length:
            exists = 1
            break
    return exists


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
