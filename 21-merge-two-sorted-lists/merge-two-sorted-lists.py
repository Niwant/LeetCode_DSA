# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newlist = ListNode()
        res = newlist

        while (list1 or list2):
            if list1 is None:
                newlist.next = list2
                break
            elif list2 is None:
                newlist.next = list1
                break

            if list1.val <= list2.val:
                node=ListNode(list1.val)
                newlist.next=node
                list1 = list1.next
            else:
                node=ListNode(list2.val)
                newlist.next=node
                list2 = list2.next
            newlist = newlist.next
        return res.next