# linkage_map_binning

# Marker Binning

The `marker_binning.py` script performs marker binning on a CSV file containing marker data. It reads the data, performs the binning operation, and saves the binned data as a new CSV file.

## Usage

1. Install the required dependencies:

```bash

pip install pandas
2. Download the marker_binning.py script and place it in your project folder.

3. In your Python script, import the marker_binning class:

from marker_binning import marker_binning

4. Create an instance of the marker_binning class:
binning_instance = marker_binning("data_folder", "data_file.csv")

5. Perform the binning operation:
binning_instance.binning()


This project is licensed under the [MIT License]
