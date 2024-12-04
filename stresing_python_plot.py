import h5py
import numpy as np
import matplotlib.pyplot as plt

def read_and_plot_hdf5(file_path):
	"""
	Reads an HDF5 file and plots the specified dataset.
	"""
	try:
		# Open the HDF5 file in read mode
		with h5py.File(file_path, 'r') as hdf:
			data = np.empty(0, dtype=np.uint16)
			# Check the datasets
			boards = list(hdf.keys())
			for board in boards:
				for camera in hdf[board]:
					for block in hdf[board][camera]:
						for sample in hdf[board][camera][block]:
							data = np.append(data, hdf[board][camera][block][sample])
			# Plot the data
			plt.figure(figsize=(8, 6))
			plt.plot(data)
			plt.xlabel("Index")
			plt.ylabel("Value")
			plt.legend()
			plt.show()
	except FileNotFoundError:
		print(f"File '{file_path}' not found.")
	except Exception as e:
		print(f"An error occurred: {e}")

if __name__ == "__main__":
	hdf5_file_path = "example.h5"  # Path to your HDF5 file
	
	read_and_plot_hdf5(hdf5_file_path)