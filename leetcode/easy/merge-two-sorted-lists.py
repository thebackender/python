#https://leetcode.com/problems/merge-two-sorted-lists/
class Solution:
    def mergeTwoLists(self, l1, l2):
        l = ListNode(None) # new list
        temp = l # keep the location of the current last node

        while l1 != None and l2 != None: 
            # while none of the two remaining lists is empty, keep going
            if l1.val <= l2.val:
                # when the value in l1's head node is less than 
                # that in l2's,
                # put it in the new list
                temp.next = l1
                l1 = l1.next
                temp = temp.next
            else:
                # else put that in l2's head node in new list
                temp.next = l2
                l2 = l2.next
                temp = temp.next
        
        # going out of the loop, put the rest of l1 or l2 in new list
        if l1 == None: temp.next = l2
        else: temp.next = l1
        
        return l.next
        return pt
print(Solution().mergeTwoLists([1,2,4], [1,3,4]))