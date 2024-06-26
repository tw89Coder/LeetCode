# 解題思路

### 目的：
當讀入的數字讀取的正反順序皆為一樣時，return true 否則 return false。
### 方法：
- 先判斷讀入的數字是否為負數或小數，若為是則直接 return false，當數字取 mod 為 0 且數字本身不為 0 則為小數。
- 使用 long 去宣告要去做翻轉的數值 `reversed` 避免超出題目的限定範圍。同時宣告一個  `temp` 去將讀入的 `x` 的值複製過去後準備做後續處理。
- 做 `while` 直到 `temp` 的值等於 `0`。
- `while` 內，將 `reversed` 存入原本的值乘 `10` 加上 `temp` 取 `10` 的餘數。
- 取餘數即為取最末端的值，乘 `10` 是將值向前移一位，加是讓餘數填充進 `reversed`。
- 迴圈完成後 return 回 `reversed` 是否與讀入 `x` 的值相等的布林值。
### Language：
Java
### Runtime：
5 ms
### Memory： 
43.4 MB
