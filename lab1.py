import numpy as np
from math import sqrt
import matplotlib.pyplot as plt

class Lab1:
    def __init__(self, n: int = 1001, gamma: int = 1, m1: int = 1) -> np.ndarray:
        self.matrix = np.zeros((n,n))
        self.gamma = gamma
        self.matrix_len = n
        self.m1 = m1
        self.m2 = 2 * m1


    def fill_matrix(self) -> bool:
        for i in range(self.matrix_len):
            for j in range(self.matrix_len):
                abs_diff = abs(i - j)

                if abs_diff > 1:
                    self.matrix[i][j] = 0
                elif abs_diff == 1:
                    self.matrix[i][j] = -self.gamma
                elif i == j:
                    if i == 0 or i == self.matrix_len - 1:
                        self.matrix[i][j] = self.gamma
                    else:
                        self.matrix[i][j] = 2 * self.gamma
                else:
                    print("Something get wrong")
                    return False
        print("Matrix fill complete!")
        print(self.matrix)
        return True


    def get_phi(self, index: int) -> int:
        phi_val = 0
        for i in self.matrix_len:
            phi_val -= self.matrix[index][i]
        return phi_val

    
    def get_m(self, index: int) -> int:
        if index & 0b1 == 1:
            return self.m1
        else:
            return self.m2


    def get_d(self, index: int, jndex: int) -> float:
        return ((self.matrix[index][jndex]) / sqrt(self.get_m(index) * self.get_m(jndex)))


    def get_d_matrix(self):
        self.d_matrix = np.zeros((self.matrix_len, self.matrix_len)) 
        for i in range(self.matrix_len):
            for j in range(self.matrix_len):
                self.d_matrix[i][j] = self.get_d(i, j)



Lab1 = Lab1()

Lab1.fill_matrix()
Lab1.get_d_matrix()
print("D matrix complete!")
print(Lab1.d_matrix)

eigenvalues, eigenvectors = np.linalg.eig(Lab1.d_matrix)

print("Eigen values complete!")
print(eigenvalues)
plt.scatter(eigenvalues, [1 for i in range(Lab1.matrix_len)])
plt.show()
    # plt.savefig("name.pdf", dpi =300)
