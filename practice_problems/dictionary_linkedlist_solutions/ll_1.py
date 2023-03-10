from node import Node
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

def replace_val(hnode, val1, val2):
    n = hnode

    while n != None:
        if n.data == val1:
            n.data = val2
        n = n.next

h1 = build_ll([10, 4, 6, 23, -5, 4])
replace_val(h1, 4, 7)
print_ll(h1)