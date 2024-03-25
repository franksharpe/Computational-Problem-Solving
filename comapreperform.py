import matplotlib.pyplot as plt

# Memory usage data for the original version
original_memory_usage = [
    54.8, 54.8, 54.8, 54.8, 54.8, 54.8, 54.8, 54.8, 54.8, 54.8, 
    54.8, 54.8, 54.8, 54.8, 54.8, 54.8, 54.8, 54.7, 54.7, 54.7, 
    54.7, 54.7, 54.7, 54.7, 54.7, 54.7, 54.7, 54.7, 54.7, 54.7, 
    54.7, 54.7, 54.7, 54.7, 54.7, 54.7, 54.7, 54.7, 54.7, 54.7, 
    54.7, 54.7, 54.7, 54.7, 54.7, 54.7, 54.7, 54.7, 54.7, 54.7
]

# Memory usage data for the modified version
modified_memory_usage = [
    54.7, 54.7, 54.7, 54.7, 54.7, 54.7, 54.7, 54.7, 54.7, 54.7, 
    54.7, 54.7, 54.7, 54.7, 54.7, 54.7, 54.7, 54.7, 54.7, 54.7, 
    54.7, 54.7, 54.7, 54.7, 54.7, 54.7, 54.7, 54.7, 54.7, 54.7, 
    54.7, 54.7, 54.7, 54.7, 54.7, 54.7, 54.7, 54.7, 54.7, 54.7, 
    54.7, 54.7, 54.7, 54.7, 54.7, 54.7, 54.7, 54.7, 54.7, 54.7
]

# Line numbers
line_numbers = list(range(1, len(original_memory_usage) + 1))

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(line_numbers, original_memory_usage, label='Task 1')
plt.plot(line_numbers, modified_memory_usage, label='Task 2')
plt.xlabel('Line Number')
plt.ylabel('Memory Usage (MiB)')
plt.title('Memory Usage Comparison')
plt.legend()
plt.grid(True)
plt.show()
