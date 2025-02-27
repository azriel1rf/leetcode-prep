問題文: https://neetcode.io/problems/reverse-a-linked-list

# Step 1
7:17かかってしまった。何をするべきなのかは即座に思い浮かんだが`while current is not None`を`while current.next is not None`にしてしまったり、
`return previous`を`return current`にしてしまったりした。

NeetCodeの動画を見て視覚的にイメージして、終了するときはcurrがNoneになるときで、そのときprevが新しいheadであると感覚的に理解できるようになった。
https://www.youtube.com/watch?v=G0_I-ZF0S38
