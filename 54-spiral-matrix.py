class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        L = 0
        R = len(matrix[0])-1
        T = 0
        B = len(matrix)-1
        result = []
        while B>=T and R>=L: #while as long B>=T and R>=L:
            for i in range(L, R+1):#loop from L until R:
                result.append(matrix[T][i])#add element to result
            T +=1 #top+1
            for i in range(T, B+1):#loop from top to bottom:
                result.append(matrix[i][R])#append right to res
            R -= 1 #right - 1
            if not (B>=T and R>=L):
                break

            for i in range(R, L-1, -1): #loop from right to L on matrix[B]:
                print("---")
                print(R,L)
                print(matrix[B][i])
                result.append(matrix[B][i]) #append ele to res
            B -= 1 #bottom-1

            for i in range(B, T-1, -1):#loop from b to top:
                result.append(matrix[i][L]) #append Left ele too res
            L += 1 #left + 1

        return result
