import numpy as np

class MatrixMultiply:  
    
    def __init__(self, A, B):
        if A.shape[1] != B.shape[0]:
            print('Dimensions dont fit')
        else:
            self.A = A
            self.B = B
            self.Am = A.shape[0]
            self.An = A.shape[1]
            self.Bm = A.shape[0]
            self.Bn = A.shape[1]
    
    def Times(self):
        C = np.zeros((self.Am, self.Bn))

        for row in range(0, self.Am):
            for column in range(0, self.Bn):
                sum = 0
                for entry in range(0, self.An):
                    sum += self.A[row, entry] * self.B[entry, column]
                C[row, column] = sum

        return C

C = np.array([[1, 2], [3, 4]])
D = np.array([[1, 2], [3, 4]])

mjr = MatrixMultiply(C, D)

mjr.Times()