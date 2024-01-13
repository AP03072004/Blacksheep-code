
import csv
import matplotlib.pyplot as plt

def read_csv(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

def plot_csv(data):
    # Extract x-axis values from the first column
    x = [float(row[0]) for row in data]
    
    # Extract y-axis values from the remaining columns
    y_data = list(map(list, zip(*data[1:])))
    
    # Plot each column as a separate line
    for i, column in enumerate(y_data):
        plt.plot(x, column, label=f'Column {i+1}')

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.show()

# Example usage
filename = 'step_50.csv'  # Replace with your CSV file name
data = read_csv(filename)
plot_csv(data)