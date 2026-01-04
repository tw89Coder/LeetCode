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
        // 創建一個虛擬節點作為合併鏈結串列的起點
        ListNode dummy = new ListNode(-1);
        // current 指針初始化為虛擬節點，用於構建合併後的鏈結串列
        ListNode current = dummy;

        // 當 list1 和 list2 都不為空時，進行迭代
        while (list1 != null && list2 != null) {
            // 比較 list1 和 list2 當前節點的值
            if (list1.val <= list2.val) {
                // 如果 list1 的值小於或等於 list2 的值，將 list1 的節點接到 current 的後面
                current.next = list1;
                // 將 list1 指針後移一位
                list1 = list1.next;
            } else {
                // 如果 list2 的值小於 list1 的值，將 list2 的節點接到 current 的後面
                current.next = list2;
                // 將 list2 指針後移一位
                list2 = list2.next;
            }
            // 將 current 指針後移一位，指向剛剛添加的節點
            current = current.next;
        }

        // 當其中一個鏈結串列耗盡時，將剩餘的另一個鏈結串列接到 current 的後面
        if (list1 != null) {
            // 如果 list1 還有剩餘節點，將其全部接到合併鏈結串列的末尾
            current.next = list1;
        } else {
            // 如果 list2 還有剩餘節點，將其全部接到合併鏈結串列的末尾
            current.next = list2;
        }

        // 返回合併後的鏈結串列，從 dummy.next 開始，因為 dummy 是虛擬節點
        return dummy.next;
    }
}