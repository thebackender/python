#https://leetcode.com/problems/remove-duplicates-from-sorted-list/
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        temp = head
        #temp.next - next element in linked list
        while temp and temp.next:
            if temp.val == temp.next.val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head
            