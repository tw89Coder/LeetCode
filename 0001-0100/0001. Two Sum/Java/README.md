# 解題思路

### 目的：
給定一個整數陣列 nums 和一個整數結果 target，陣列中會有兩個元素加起來等於整數結果 target，回傳這兩個元素的位置。
你可能假設每個輸入只會對應一個答案，而且你不能使用同樣的元素兩次，你可以回傳任何順序的答案。
### 方法：
- 使用 HashMap 去做為資料儲存的方式，用空間換取時間避免出現巢狀迴圈。
- 做 nums 陣列長度次數的遞迴，遍歷 nums 陣列的每個元素。
  - 當發 現HashMap 中存在一個數字，其值為 target 減去當前元素的值時，返回這兩個數字的索引。
  - 如果 HashMap 中不存在這個數字，則將當前元素及其索引存入 HashMap。
- 如果遍歷整個陣列後仍未找到符合條件的數字組合，則返回空的整數陣列。
### Language：
Java
### Runtime：
2 ms
### Memory： 
44.6 MB

---
## Java HashMap

### Definition and Usage
One object is used as a key (index) to another object (value). It can store different types: String keys and Integer values, or the same type, like: String keys and String values.


[W3C Link](https://www.w3schools.com/java/java_hashmap.asp)
