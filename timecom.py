import matplotlib.pyplot as plt

# Function to plot hypothetical quadratic graphs
def plot_quadratic_graphs():
    # Number of orders
    num_orders = list(range(0, 1000, 50))  # Hypothetical range of number of orders
    # Time complexities for different operations
    loading_time = [n for n in num_orders]  # Linear loading time
    saving_time = [n**2 for n in num_orders]  # Quadratic saving time
    deleting_time = [n**2 for n in num_orders]  # Quadratic deleting time
    modifying_time = [n for n in num_orders]  # Linear modifying time

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(num_orders, loading_time, label='Loading Orders (O(n))')
    plt.plot(num_orders, saving_time, label='Saving Orders (O(n^2))')
    plt.plot(num_orders, deleting_time, label='Deleting Orders (O(n^2))')
    plt.plot(num_orders, modifying_time, label='Modifying Orders (O(n))')

    plt.title('Hypothetical Time Complexities')
    plt.xlabel('Number of Orders')
    plt.ylabel('Time (arbitrary units)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Plot the graphs
plot_quadratic_graphs()
