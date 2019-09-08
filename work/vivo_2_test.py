class node():
    def __init__(self, val):
        self.val = val
        self.next = None

def get_arraylist(nums):
    i = 0
    if nums != []:
        head = node(nums[0])
    temp = head
    while i < len(nums)-1:
        i += 1
        temp.next = node(nums[i])
        temp = temp.next

    return head

def show(head):

    temp = head
    while temp != None:
        print(temp.val)
        temp = temp.next

def convert_arraylist(head, m, n):
    if m == 1:
        cur1 = head
        next1 = cur1.next

        pre2 = head
        for i in range(n-2):
            pre2 = pre2.next
        cur2 = pre2.next
        next2 = cur2.next

        cur2.next = next1
        pre2.next = cur1
        cur1.next = next2
        return cur2
    else:
        pre1 = head
        for i in range(m-2):
            pre1 = pre1.next
        cur1 = pre1.next
        next1 = cur1.next
        pre2 = head
        for i in range(n-2):
            pre2 = pre2.next
        cur2 = pre2.next
        next2 = cur2.next
        pre1.next = cur2
        cur2.next = next1
        pre2.next = cur1
        cur1.next = next2
        return head

def convert_arraylist_only1(head, m, n):
    dummyhead = node(0)
    dummyhead.next = head
    pre1 = dummyhead
    for i in range(m-1):
        pre1 = pre1.next
    cur1 = pre1.next
    next1 = cur1.next

    pre2 = dummyhead
    for i in range(n-1):
        pre2 = pre2.next
    cur2 = pre2.next
    next2 = cur2.next

    pre1.next = cur2
    cur2.next = next1
    pre2.next = cur1
    cur1.next = next2
    return dummyhead.next



if __name__ == '__main__':
    nums = [1,2,3,4,5,6]
    head = get_arraylist(nums)
    show(head)
    head = convert_arraylist_only1(head,2,5)
    show(head)
