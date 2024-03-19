import matplotlib.pyplot as plt

# Function to plot time complexities for Task 1 and Task 2 algorithms
def plot_time_complexities(task1_complexities, task2_complexities):
    # Number of orders
    num_orders = list(range(0, 1000, 50))  # Hypothetical range of number of orders

    # Plotting
    plt.figure(figsize=(14, 6))

    # Plot Task 1 complexities
    plt.subplot(1, 2, 1)
    plt.plot(num_orders, task1_complexities['loading'], label='Loading Orders (O(n))')
    plt.plot(num_orders, task1_complexities['saving'], label='Saving Orders (O(n^2))')
    plt.plot(num_orders, task1_complexities['deleting'], label='Deleting Orders (O(n^2))')
    plt.plot(num_orders, task1_complexities['modifying'], label='Modifying Orders (O(n))')
    plt.title('Task 1 Algorithm Time Complexities')
    plt.xlabel('Number of Orders')
    plt.ylabel('Time (arbitrary units)')
    plt.legend()
    plt.grid(True)

    # Plot Task 2 complexities
    plt.subplot(1, 2, 2)
    plt.plot(num_orders, task2_complexities['loading'], label='Loading Orders (O(n))')
    plt.plot(num_orders, task2_complexities['saving'], label='Saving Orders (O(n^2))')
    plt.plot(num_orders, task2_complexities['deleting'], label='Deleting Orders (O(n^2))')
    plt.plot(num_orders, task2_complexities['modifying'], label='Modifying Orders (O(n))')
    plt.title('Task 2 Algorithm Time Complexities')
    plt.xlabel('Number of Orders')
    plt.ylabel('Time (arbitrary units)')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()

# Define hypothetical time complexities for Task 1 and Task 2
task1_complexities = {
    'loading': [n for n in range(0, 1000, 50)],  # Linear loading time
    'saving': [n**2 for n in range(0, 1000, 50)],  # Quadratic saving time
    'deleting': [n**2 for n in range(0, 1000, 50)],  # Quadratic deleting time
    'modifying': [n for n in range(0, 1000, 50)]  # Linear modifying time
}

task2_complexities = {
    'loading': [n for n in range(0, 1000, 50)],  # Linear loading time
    'saving': [n**2 for n in range(0, 1000, 50)],  # Quadratic saving time
    'deleting': [n**2 for n in range(0, 1000, 50)],  # Quadratic deleting time
    'modifying': [n for n in range(0, 1000, 50)]  # Linear modifying time
}

# Plot the time complexities
plot_time_complexities(task1_complexities, task2_complexities)
