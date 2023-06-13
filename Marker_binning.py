import pandas as pd
class marker_binning:
    def __init__(self,folder,file):
        map=pd.read_csv(f"{folder}/{file}", dtype='str')

    def binning(self):
        map['full_count'] = map.apply(lambda x: x.count(), axis=1)
        map['LG_position'] = map['lg'] + '_' + map['Position']
        map = map.sort_values('full_count', ascending=False).drop_duplicates('LG_position').sort_index()

        map.to_csv(f"{self.folder}/{self.file}_binned.csv")
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--folder', help='Path to the folder containing the CSV file')
    parser.add_argument('--file', help='Name of the CSV file')
    args = parser.parse_args()

    binning_instance = marker_binning(args.folder, args.file)
    binning_instance.binning()
