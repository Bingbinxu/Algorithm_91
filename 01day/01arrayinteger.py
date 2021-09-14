
class Solution:
    def __init__(self, A: list, K: int) -> list:
        self.A=A
        self.K=K
    def addToArrayForm(self):
        A=self.A
        K=self.K
        carry = 0
        for i in range(len(A) - 1, -1, -1):
            A[i], carry = (carry + A[i] + K % 10) % 10, (carry + A[i] + K % 10) // 10  # //"表示整数除法。
            K //= 10
        B = []
        # 如果全部加完还有进位，需要特殊处理。 比如 A = [2], K = 998
        carry = carry + K
        while carry:
            B = [(carry) % 10] + B
            carry //= 10
        return B + A
        
P = [1,2,3,4]      
a = Solution(P,22) 
print(a.addToArrayForm())