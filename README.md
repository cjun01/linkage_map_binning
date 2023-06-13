# Marker Binning

This is a Python script that performs binning on marker data of linkage map from a CSV file.

## Requirements

This script requires Python 3.6 or later versions, and the following Python packages:

- pandas
- argparse

You can install these packages using pip:

```bash
pip install pandas argparse
```

# Usage
You can use this script from the command line by providing the folder path and the file name as arguments:

python <script_name>.py --folder <folder_path> --file <file_name>
- <script_name>: The name of this script file.
- <folder_path>: The path of the folder where the CSV file is located.
- <file_name>: The name of the CSV file.

After the script is run, a new file named <file_name>_binned.csv is created in the same folder as the original file. This file contains the results of the binning operation.

# Notes
Data format see example.csv

The script does not handle missing data. Make sure your CSV file does not contain missing values in the 'lg' and 'Position' columns.
