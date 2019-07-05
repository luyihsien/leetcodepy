'''
Python的內建型別list底層是由C陣列實現的，list在功能上更接近C 的vector（因為可以動態調整陣列大小）。
我們都知道，陣列是連續列表，連結串列是連結列表，二者在概念和結構上完全不同，因此list不能用於實現連結串列。
在C/C 中，通常採用“指標 結構體”來實現連結串列；而在Python中，則可以採用“引用 類”來實現連結串列。
'''
import sys
a=[1,2,3,4]
print(sys.getsizeof(a),a)
a.append(5)
a.append(6)

print(sys.getsizeof(a),a)
a=[]
print(sys.getsizeof(a),a)
a.append(2)
print(sys.getsizeof(a),a)