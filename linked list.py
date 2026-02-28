#reversal of singly linked list
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head  # as head is initial pointer to linked list thats why we start from there
        previous = None  # head has no previous node, also we use this to make current node point to previous node
        while current:  # we use while as not knowing how many nodes and till current as we stop after last node as then curr will be None
            next_node = current.next  # storing next of current before making any changes as we will lose remaining list if we alter first
            current.next = previous  # making currnet node to point to previous node i.e. reversing it
            # now we change previous,current as we change iterables like i in normal array to point  prev to curr node,curr. to next node
            previous = current  # we make curr. as prev. as for next node this becomes prev. node(prev. assigned first as if we change curr first we lose the curr node)
            current = next_node  # now the next node becomes curr like we do i=i+1 in case of array

        return previous  # at last we return previous as while stops when curr is None i.e. previous has last node or 1st node of reversed linked list
"""

#finding middle(odd) or secondmiddle(even) of singly linked list
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #using two pointer to find middle
        #first moves one by one while moves twice as fast and at end,first will be at middle(odd),close to it(even no. of nodes)
        #initially both start at head
        first=head
        second=head
        #here in ll,head is not some seperate node its just a pointer to 1st node ie. head=1st node or head.next is actually 1st node.next
        while second and second.next: 
            #we check both second and its next as if second is none, its next will give error
            #and also .next might be none so we also need to check it so that we dont acess second.next.next in loop
            first=first.next
            second=second.next.next
        
        return first
        #for both even and odd numbered linked list,fp ends up at either exactly middle or at 2nd middle for even numbered
"""

#merging two sorted linked list's
#(i) creating new final ll
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:  # if first ll empty
            return list2
        elif list2 is None:  # if second ll empty
            return list1
        elif (list1 is None) and (list2 is None):  # if both empty
            return []
        first = list1
        second = list2
        headoffinal = None
        final = None
        while first and second:  # till both list exists  i.e. non empty
            if (first.val > second.val):  # if second's value is smaller
                if (final == None):
                    final = ListNode(second.val,
                                     None)  # create new node in final ll if its empty with value of second's ll current node
                    headoffinal = final
                else:
                    final.next = ListNode(second.val,
                                          None)  # create new node in final ll if it already has a node with value of second's ll current node
                    final = final.next  # move final ll pointer to its next node
                second = second.next  # move seconds points to its next node
            elif (second.val > first.val):  # if first's value is smaller
                if (final == None):
                    final = ListNode(first.val,
                                     None)  # create new node in final ll if its empty with value of first's ll current node
                    headoffinal = final
                else:
                    final.next = ListNode(first.val,
                                          None)  # create new node in final ll if it already has a node with value of first's ll current node
                    final = final.next  # move final ll pointer to its next node
                first = first.next  # move first's points to its next node
            else:  # if both has same value we are taking first ll current node's value 
                if (final == None):
                    final = ListNode(first.val, None)
                    headoffinal = final
                else:
                    final.next = ListNode(first.val, None)
                    final = final.next
                first = first.next

        if first is None:  # if first ll is processed fully add second's remaining values to final ll
            final.next = second
        elif second is None:  # if second ll is processed fully add first's remaining values to final ll
            final.next = first

        return headoffinal
"""
#(ii) using nodes of orignal sorted ll's
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None: #if first ll empty
            return list2
        elif list2 is None: #if second ll empty
            return list1 
        first=list1
        second=list2
        headoffinal=None
        final=None
        while first and second: #till both list exists  i.e. non empty
            if(first.val>second.val): #if second's value is smaller
                if(final==None):
                    final=second #add second ll current node to final
                    #####final.next=None #setting final next pointer to none
                    headoffinal=final #getting pointer to first node of final ll
                else:
                    final.next=second #add second's ll current node to final next
                    final=final.next #move final ll pointer to its next node
                    #####final.next=None #setting final next pointer to none
                second=second.next #move seconds points to its next node
            elif(second.val>first.val): #if first's value is smaller
                if(final==None):
                    final=first #add first's ll current node to final
                    #####final.next=None #setting final next pointer to none
                    headoffinal=final #getting pointer to first node of final ll
                else:
                    final.next=first #add first's ll current node to final next
                    final=final.next #move final ll pointer to its next node
                    #####final.next=None #setting final next pointer to none
                first=first.next #move first's points to its next node
            else: #if both has same value we are taking first ll current node's value (code is same as above when first ll value's small)
                if(final==None):
                    final=first
                    #####final.next=None
                    headoffinal=final
                else:
                    final.next=first
                    final=final.next
                    #####final.next=None
                first=first.next

        if first is None: #if first ll is processed fully add second's remaining values to final ll
            final.next=second
        elif second is None: #if second ll is processed fully add first's remaining values to final ll
            final.next=first
        
        return headoffinal
        """
        #important resons for ##### in (ii) in merging two sorted ll's
        """the main thing in this code is where ##### 5 hash are there we dont need to set .next to none for two reasons: 
        1. as we rewrite the .next in every iteration so no need to put it to none and at the end we just point final
        to remaing non empty list and that list's last node will be empty as input list1 and list2 would obviously have 
        final node's next to None
        2. the most important reason is as when do final=second or final=first we take put reference of that node to final
        as these nodes are ListNode's objects these are not just values that we can copy we take reference of it not copy 
        so if we do final.next=None we just lose remaining list of that ll,thats why we dont set it to None we just let 
        it rewrite normally by loop"""

#removing nth node from end of ll
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        T=0
        curr=head #var to move from node to node
        while curr:
            curr=curr.next #here changing what current does not change head as we are reassigning curr not changing,curr.next or curr.val
                           #so doing this only changes curr not head's value
            T=T+1
        
        if(T==1): #if ll has just 1 node so no need to run below loops
            return None

        fromstart=(T-n)+1 #position of n from start
        temp=head #var to point to node being removed
        prevtemp=None #var to point to node just before the one being removed i.e. temp
        f=1 #temprory var to check if temp is at starting or not to adjust pointers
        while temp:
            fromstart=fromstart-1 #decreasing the counter till 0 i.e. reaching the node to be removed
            if(fromstart==0): #if reached the node to be removed
                if(f==1): #reaching the node to be removed is starting node
                    prevtemp=temp.next #taking and joining remaining list to prevtemp
                    return prevtemp #return remaining list
                else: #starting node is not to be removed, to remove some inner node in ll
                    prevtemp.next=temp.next #we can assign prevtemp.next something as this is when prevtemp is pointing to a node
                    return head
            else: #if not reached the node to be removed
                if(f==1): #if temp at starting node
                    prevtemp=temp
                    temp=temp.next
                    f=0
                else: #if temp is somewhere in middle of ll
                    prevtemp=prevtemp.next
                    temp=temp.next
"""