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

def sum_ll(head):
    sum = 0
    n = head

    while n != None:
        sum = sum + n.data
        n = n.next

    return sum

head = build_ll([10, 4, 5, 6])
print_ll(head)
print(sum_ll(head))
