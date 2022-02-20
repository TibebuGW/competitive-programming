def has_cycle(head):
    count=0
    while head:
       count+=1
       head = head.next
       if count>1000:
            return 1
    return 0
