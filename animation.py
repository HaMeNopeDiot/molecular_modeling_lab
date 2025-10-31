import numpy as np
import matplotlib.pyplot as plt
 
 
elements_number = 1000
x = np.linspace(1, 100, elements_number)
y = np.sin(x)
partition = 10
 
 
def draw_graphs(x, y, partition):
    one_step = int(len(y) / partition)
    
    for i in range(1, partition + 1):
        left_index = 0
        right_index = one_step * i
        not_enough = elements_number - right_index
    
        current_y = np.concatenate((y[:right_index], np.full((not_enough), np.nan)))
        plt.scatter(101, 0, color='white')
        plt.plot(x, current_y )
        plt.savefig(f'graph_{i - 1}.pdf', format='pdf')
        plt.cla()
 
 
draw_graphs(x, y, partition)