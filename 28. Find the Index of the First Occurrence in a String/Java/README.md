# 解題思路

### 目的：
找出子字符串 needle 在字符串 haystack 中首次出現的位置索引。如果 needle 不存在於 haystack 中，則返回 -1。
### 方法：
- 使用 Java 提供的內建方法 indexOf，該方法返回子字符串在字符串中第一次出現的索引，如果子字符串不存在，則返回 -1。
- 首先檢查 needle 是否為空字符串，若是，根據問題定義應返回 0。
- 調用 haystack.indexOf(needle) 獲取結果。
### Language：
Java
### Runtime：
0 ms
### Memory： 
41.35 MB
