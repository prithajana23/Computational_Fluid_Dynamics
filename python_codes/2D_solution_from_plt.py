# For the 2D advection equation, write a code for creating the plots from the saved .plt files.

import numpy as np
import matplotlib.pyplot as plt

def plot_advection_data(filename):
    """
    Reads data from a .plt file and creates a plot for the 2D advection equation.
    Args:
        filename (str): The path to the .plt file.
    """
    try:
        data = np.loadtxt(filename)
        # Assuming the data is structured as follows: x-coordinates, y-coordinates, solution values
        x = data[:, 0]
        y = data[:, 1]
        u = data[:, 2] 

        # Create a 2D meshgrid
        X, Y = np.meshgrid(np.unique(x), np.unique(y))
        U = u.reshape(X.shape)  
        # Create the contour plot
        plt.figure(figsize=(8, 6))  
        contour = plt.contourf(X, Y, U, levels=20, cmap='viridis')  
        plt.colorbar(contour, label="Solution Value") 
        plt.xlabel('X-coordinate')
        plt.ylabel('Y-coordinate')
        plt.title(f'2D Advection Solution at Time (from file: {filename})') 
        plt.show()

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
plot_advection_data('solution.plt')  
