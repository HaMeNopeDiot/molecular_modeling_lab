import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

eps = 1
sigma = 1
m = 10
iter_count = 1

# не менее 10 молекул, визуализация
x=[-0.0, 1.1, 2.2, 0.0, 1.09, 2.18, 0.0, 1.1, 2.2, -0.0, 1.09, 2.17, 0.0, 1.07, 2.15, 0.0, 1.09, 2.18, 0.0, 1.1, 2.2, 0.0, 1.09, 2.18, -0.01, 1.09, 2.19]
y=[-0.0, -0.0, -0.0, 1.1, 1.08, 1.1, 2.2, 2.17, 2.2, -0.0, -0.0, -0.0, 1.09, 1.07, 1.08, 2.17, 2.15, 2.17, -0.0, -0.0, 0.0, 1.1, 1.09, 1.1, 2.2, 2.17, 2.2]
z=[-0.0, -0.0, -0.0, 0.0, -0.0, -0.0, 0.0, -0.0, -0.0, 1.1, 1.08, 1.1, 1.09, 1.07, 1.09, 1.1, 1.09, 1.1, 2.2, 2.17, 2.2, 2.18, 2.14, 2.17, 2.2, 2.17, 2.2]

#x = [-2, 0, 2, 0, -2, 0, 2, 0]
#y = [0, 2, 0, -2, 0, 2, 0, -2]
#z = [0, 0, 0, 0, 2, 2, 2, 2]

X_ = x+y+z
N = len(x)

plt.plot(x, y, 'bo', markersize=12)
plt.grid()
plt.savefig('Start position1')
plt.cla()


def U(i, j, X):
    x_ = X[:N]
    y_ = X[N:(2*N)]
    z_ = X[-N:]
    global eps, sigma
    r_ij = np.sqrt((x_[i]-x_[j])**2+(y_[i]-y_[j])**2+(z_[i]-z_[j])**2)
    return 4*eps*((sigma/r_ij)**12-(sigma/r_ij)**6)


def U_total(X):
    # записывать энергию и координаты в текстовый файл
    sum = 0
    for i in range(N):
        for j in range(i+1, N):
            sum += U(i, j, X)
    """
    x_end = X[:N]
    y_end = X[N:(2*N)]
    z_end = X[-N:]
    # запись координат в файл        
    with open("animate_coords", "a") as file:
        file.write('\n')
        for i in range(N):
            file.write('A'+str(i)+' '+ str(x_end[i]) + ' ' + str(y_end[i]) + ' ' + str(z_end[i]) + '\n')
            
    with open("animate_Etot", "a") as file:
       file.write(str(sum) + '\n')
    """
    
    return sum


with open("animate_coords", "w") as file:
    file.write(str(N))
    file.write('\n')
    x_end = X_[:N]
    y_end = X_[N:(2*N)]
    z_end = X_[-N:]
    for i in range(N):
        file.write('A'+str(i)+' '+ str(x_end[i]) + ' ' + str(y_end[i]) + ' ' + str(z_end[i]) + '\n')
    
with open("animate_Etot", "w") as file:
    energy = U_total(X_)
    file.write(str(energy) + '\n')
    
    
def save_iteration(X):
    global iter_count
    iter_count += 1
    if iter_count % 15 == 0:
        energy = U_total(X)
        x_end = X[:N]
        y_end = X[N:(2*N)]
        z_end = X[-N:]
        # запись координат в файл        
        with open("animate_coords", "a") as file:
            file.write('\n')
            for i in range(N):
                file.write('A'+str(i)+' '+ str(x_end[i]) + ' ' + str(y_end[i]) + ' ' + str(z_end[i]) + '\n')
                
        with open("animate_Etot", "a") as file:
           file.write(str(energy) + '\n')
    
result = opt.fmin(U_total, X_, xtol=1.0e-5, ftol=1.0e-5, full_output=1, callback=save_iteration)
res1 = result[0]
with open('animate_coords', 'r') as file:
    old_content = file.read()

    # Открываем файл в режиме записи ('w')
    # Этот режим перезаписывает файл или создаёт новый, если он не существует
with open('animate_coords', 'w') as file:
    # Записываем новый текст
    file.write(str(iter_count) + '\n')
    # Дописываем старое содержимое
    file.write(old_content)

x_end = res1[:N]
y_end = res1[N:(2*N)]
z_end = res1[-N:]

print(U_total(res1))
plt.plot(x_end, y_end, 'bo', markersize=12)
plt.grid()
plt.savefig('End position1')
plt.cla()

str0 = str(N)
str1 = 'A '
str2 = 'B '
str3 = 'C '
for i in range(N):
    str1 += str(x_end[i]) + ' '
for i in range(N):
    str2 += str(y_end[i]) + ' '
for i in range(N):
    str3 += str(z_end[i]) + ' '

with open("my_example.xyz", "w") as file:
    file.write(str0 + '\n')
    file.write('Argon\n')
    for i in range(N):
        file.write('A'+str(i)+' '+ str(x_end[i]) + ' ' + str(y_end[i]) + ' ' + str(z_end[i]) + '\n')
        
print('x=[', end='')
for i in range(N):
    print(str(round(x_end[i],2)) + ', ', end='')
print(']')

print('y=[', end='')
for i in range(N):
    print(str(round(y_end[i],2)) + ', ', end='')
print(']')

print('z=[', end='')
for i in range(N):
    print(str(round(z_end[i],2)) + ', ', end='')
print(']')
