import pandas as pd
class marker_binning:
    def __init__(self,folder,file):
        map=pd.read_csv(f"{folder}/{file}", dtype='str')

    def binning(self):
        self.map['full_count'] = self.map.apply(lambda x: x.count(), axis=1)
        self.map['LG_position'] = self.map['lg'] + '_' + self.map['Position']

        # Count duplicates before dropping
        duplicate_counts = self.map['LG_position'].value_counts() - 1

        self.map = self.map.sort_values('full_count', ascending=False).drop_duplicates('LG_position').sort_index()

        # Add an additional column 'Duplicate_Count' to the DataFrame
        self.map['Duplicate_Count'] = self.map['LG_position'].map(duplicate_counts)

        # Fill NaN values in 'Duplicate_Count' with 0
        self.map['Duplicate_Count'] = self.map['Duplicate_Count'].fillna(0)

        self.map.to_csv(f"{self.folder}/{self.file}_binned.csv")
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--folder', help='Path to the folder containing the CSV file')
    parser.add_argument('--file', help='Name of the CSV file')
    args = parser.parse_args()

    binning_instance = marker_binning(args.folder, args.file)
    binning_instance.binning()
