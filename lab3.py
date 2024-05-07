import numpy as np
from numpy.linalg import inv, eig

#--------------1.1-------------

#Знаходимо повні випуски для обох продукцій
x11, x12, y1 = 500, 300, 900
x21, x22, y2 = 150, 200, 500
x1 = x11 + x12 + y1
x2 = x21 + x22 + y2

print(f"Випуск для промисловості {x1} . Випуск для сільського господарства {x2}","\n")

#Прогнозовані зростання
p1 ,p2 = 1100,800

#Технологічна матриця
column1, column2 = np.array([x11, x21])/x1 , np.array([x12, x22])/x2
A = np.array([column1, column2]).T
#Матриця повних витрат
E = np.diag([1,1])
B = inv(E-A)
#Повний випуск x = Bc
new_x1, new_x2 = np.dot(B, np.array([p1, p2]))
print("Повний випуск промислової продукції:", new_x1)
print("Повний випуск сільськогосподарської продукції:", new_x2,"\n")

#--------------1.2-------------

#Матриця витрат
A = np.array([[0.5, 0.1, 0.5],[0, 0.3, 0.1],[0.2, 0.3, 0.1]])
print(A)
for x in A: 
    print(f'q ={np.sum(x)}')
    
print("Матриця витрат","\n",A ,"\n")
    
#Модель Леонтьєва за цією матрицею продуктивна. Знаходимо її власні числа та власні вектори:
eigenvalues, eigenvectors = eig(A)
print("Власні числа: ", eigenvalues)
print ("Власні вектори: ", eigenvectors,"\n")

#Знаходимо число Фробеніуса і правий вектор Фробеніуса
lambda_index = np.argmax(eigenvalues)
lambda_A = eigenvalues[lambda_index]
x_rA = eigenvectors[:, lambda_index]
if(np.sum(x_rA)<0):
    x_rA = x_rA * -1
    
print ("Число Фробеніуса",lambda_A, "\n")
print ("Правий вектор Фробеніуса",x_rA,"\n")

#Лівий вектор Фробеніуса
temp_eigenvalues, temp_eigenvectors = eig(A.T)
temp_lambda_index = np.argmax(temp_eigenvalues)

x_lA = temp_eigenvectors[:, temp_lambda_index]
if(np.sum(x_lA)<0):
    x_lA = x_lA * -1
print ("Лівий вектор Фробеніуса",x_lA,"\n")
#Знаходимо поліном по кореням
pol = np.polynomial.Polynomial.fromroots(eigenvalues)
print("Поліном по кореням: ",pol ,"\n")
#Знаходимо матрицю повних витрат
E = np.diag([1,1,1])
B = inv(E-A)
print("Матриця повних витрат ", B,"\n")
#Чи збіжна послідовність повних витрат
def compute_series(A, n):
    d = np.diag([1,1,1])
    res = np.diag([1,1,1])
    for i in range(n):
        d = np.dot(A,d)
        res= res + d
    return res
N = 0
print("Чи збіжна послідовність повних витрат")
while(np.max(B-compute_series(A,N))>0.01):
    print(f"N={N}, d={np.max(B-compute_series(A,N))}")
    N+=1
print(f"N={N}, d={np.max(B-compute_series(A,N))}")

#Знаходимо вектор цін p = s(E-A)^-1
s=np.array([0.3, 0.4, 0.5])
p=np.dot(s,B)

print("Вектор цін: ",p)