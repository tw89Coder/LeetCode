/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        // 創建一個虛擬節點以簡化合併過程
        ListNode dummy = new ListNode(-1);
        ListNode current = dummy;

        // 迭代兩個鏈結串列
        while (list1 != null && list2 != null) {
            if (list1.val <= list2.val) {
                current.next = list1;
                list1 = list1.next;
            } else {
                current.next = list2;
                list2 = list2.next;
            }
            current = current.next;
        }

        // 附加剩餘的節點
        if (list1 != null) {
            current.next = list1;
        } else {
            current.next = list2;
        }

        // 返回合併後的鏈結串列，其開始於 dummy.next
        return dummy.next;
    }
}
