from node import  Node
def build_ll(glist):
    head = None
    i = 0
    while i < len(glist):
        new_node = Node(glist[i])
        if head == None:
             head = new_node
             n = new_node
        else:
            n.next = new_node
            n = n.next
        i = i + 1

    return head

def print_ll(head):
    n = head

    while n != None:
        print(n.data, end="-->")
        n = n.next

    print("\n")

def insert_before(head, val_before, val):
    prev = None
    n = head
    while n != None:
        if n.data == val_before:
            new_node = Node(val)
            if prev == None:
                new_node.next = n
                head = new_node
            else:
                new_node.next = prev.next
                prev.next = new_node
            break

        prev = n
        n = n.next

    return head

h1 = build_ll([10, 5, 7, 10, 28, 6])
print_ll(h1)
h1 = insert_before(h1, 28, 20)
print_ll(h1)