# Step1, 2
それぞれカウントして比較するだけだと思ったけど、模範解答を見て比較はキーをイテレートしなくても良いなって思った。
模範解答: 
```Python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
```
defaultdictを使いたかったためdefaultdictのequalityの仕様を調べていた
->調べたけどわからない。イテレートせずに比較したいならdictを使った方が無難。面接官にequalityについて突っ込まれたときに自信を持って答えられない

defaultdictはdictを継承しており、個別にeqを実装してないためdictと同じだと考えていい。
https://github.com/python/cpython/blob/3.13/Modules/_collectionsmodule.c#L2802

あとよく見たら長さでアーリーリターンするのも良いところだな。

# Step3
時間を測ったら1:54だった。
