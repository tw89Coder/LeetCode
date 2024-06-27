# 解題思路

### 目的：
檢查給定的字串 s 是否為有效的括號配對。這裡的「有效括號配對」是指每個開括號 `(`、`{`、`[` 都有對應的閉括號 `)`、`}`、`]`，且它們的順序是正確的。
### 方法：
- 使用 `HashMap` 來存儲開括號和閉括號的對應關係。
- 使用 `Stack` 來存儲遇到的開括號。
- 遍歷字串：
  - 如果當前字元是開括號（存在於 `map` 的鍵中），將其壓入 `Stack` 。
  - 如果當前字元是閉括號，檢查Stack是否為空，如果為空表示括號不匹配，返回 `false`。
  - 如果 `Stack` 不為空，檢查 `Stack` 頂部的開括號是否與當前閉括號匹配，匹配則彈出 `Stack` 頂部的開括號，不匹配則返回 `false`。
- 遍歷完字串後，檢查 `Stack` 是否為空，如果為空表示所有的括號都匹配，返回 `true`，否則返回 `false`。
### Language：
Java
### Runtime：
2 ms
### Memory： 
41.37 MB

---
## Java Class Stack

### Definition and Usage
The **`Stack`** class represents a last-in-first-out (LIFO) stack of objects. It extends class **Vector** with five operations that allow a vector to be treated as a stack. The usual push and pop operations are provided, as well as a method to **peek** at the top item on the stack, a method to test for whether the stack is **empty**, and a method to **search** the stack for an item and discover how far it is from the top.
When a stack is first created, it contains no items.


[Oracle Link](https://docs.oracle.com/javase/8/docs/api/java/util/`Stack`.html)