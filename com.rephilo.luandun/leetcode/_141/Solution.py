from datastructure import ListNode


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """
        快慢指针
        :param head:
        :return:
        """
        if head is None or head.next is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast.next is None or fast.next.next is None:
                return False

            slow = slow.next
            fast = fast.next.next
        return True
