import pandas as pd
class marker_binning:
    def __init__(self,folder,file):
        self.folder=folder
        self.file=file
    def binning(self):
        map=pd.read_csv(f"{self.folder}/{self.file}", dtype='str')
        map['LG_position'] = map['lg'].astype(str) + '_' + map['Position'].astype(str)
        duplicates = map['LG_position'].duplicated()
        map['No_Markers_binned'] = duplicates.groupby(map['LG_position']).transform('sum')
        map.drop_duplicates('LG_position', inplace=True)
        map.drop('LG_position', axis=1, inplace=True)
        self.map.to_csv(f"{self.folder}/{self.file}_binned.csv")
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--folder', help='Path to the folder containing the CSV file')
    parser.add_argument('--file', help='Name of the CSV file')
    args = parser.parse_args()

    binning_instance = marker_binning(args.folder, args.file)
    binning_instance.binning()
