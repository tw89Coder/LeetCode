# 解題思路

### 目的：
將兩個已排序的鏈結串列合併成一個已排序的鏈結串列。
### 方法：
- 創建一個虛擬節點作為合併鏈結串列的起點。這有助於稍後輕鬆返回合併鏈結串列的頭節點。
- `current` 指針用於跟蹤合併鏈結串列中的最後一個節點。
- 只要兩個鏈結串列都沒有耗盡，`while` 迴圈就會繼續。比較兩個鏈結串列當前節點的值，將較小的節點附加到合併鏈結串列中，並將指針向前移動到取出節點的鏈結串列中。
- 在 `while` 迴圈之後，其中一個鏈結串列可能還有剩餘的節點。將剩餘的節點附加到合併鏈結串列中，通過設置 `current.next` 為非空的鏈結串列。
- 合併後的鏈結串列從 `dummy.next` 開始，因為 `dummy` 本身只是個佔位符。
### Language：
Java
### Runtime：
0 ms
### Memory： 
42.14 MB

---
## Java Class ListNode

### Definition and Usage
All Nodes which have a list representation inherit this. This is also used as generic container for additional information that is not directly evaluated. In particular, f_arg production rule uses this to capture arg information for the editor projects who want position info saved.


[Javadoc Link](https://www.javadoc.io/doc/org.jruby/jruby-core/9.2.8.0/org/jruby/ast/ListNode.html)