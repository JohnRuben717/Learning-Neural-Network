input = [1, 2, 3, 2.5]

weights = [0.2, 0.8, -0.5 ,1]
weights2 = [0.5, -0.91, 0.26,-0.5]
weights3 = [-0.26, -0.27 , 0.17 , 0.87]
bias1 = 2
bias2 = 3
bias3 = 0.5

output = input[0]*weights[0] + input[1]*weights[1] + input[2]*weights[2] + input[3]*weights[3] + bias
print(output)