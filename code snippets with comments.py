#matplotlib - drawing of the signatures
'''
fig, ax = plt.subplots()

ax.plot(first[0]['X'], first[0]['Y'])

ax.set(xlabel='X')
ax.set(ylabel='Y')

plt.show()

'''

import matplotlib.pyplot as plt

import matplotlib.pyplot as plt

# Step 3: Load the data with row skip
x = []
y = []
row_skip = 1  # Adjust this value according to the number of rows you want to skip
with open('C:\\Users\\ASUS\\Documents\\BME\\6. félév\\Önálló laboratórium\\Signature Verification\\training\\U41S46.txt', 'r') as file:
    for i, line in enumerate(file):
        if i < row_skip:
            continue  # Skip the rows
        data = line.split()  # Assuming space-separated data
        x.append(float(data[0]))  # Assuming x values are in the first column
        y.append(float(data[1]))  # Assuming y values are in the second column

# Step 4: Plot the data
plt.plot(x, y)
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')
plt.title('Your Title Here')
plt.grid(True)
plt.show()
