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

def find_max_ll(head):
    if head != None:
        max = head.data
    else:
        return None

    n = head.next
    while n != None:
        if max < n.data:
            max = n.data
        n = n.next

    return max

head = build_ll([10, 4, 70, 8])
print_ll(head)
print(find_max_ll(head))
