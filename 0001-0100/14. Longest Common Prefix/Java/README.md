# 解題思路

### 目的：
尋找最長的共用開頭字串。
### 方法：
- 先拿第一個字串當作 prefix，使用 indexOf() 去檢查剩下的是否 index 為 0，也就是是否在首位。
- 如果不是就 prefix 的字元減少一個，直到 indexOf() == 0 就輪至下一個，直到所有的都輪到。
- 若是輸入的 str 或是 prefix 為空，則直接 return ""。
### Language：
Java
### Runtime：
0 ms
### Memory： 
42 MB

---
## Java String indexOf() Method

### Definition and Usage
The indexOf() method returns the position of the first occurrence of specified character(s) in a string.

**Tip:** Use the lastIndexOf method to return the position of the last occurrence of specified character(s) in a string.

[W3C Link](https://www.w3schools.com/java/ref_string_indexof.asp)
