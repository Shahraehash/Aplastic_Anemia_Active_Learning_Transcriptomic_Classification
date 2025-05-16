import pandas as pd


if __name__ == "__main__":
    AA_cells = "/Users/raehash/Desktop/CMU/CMU Masters Year/Spring Semester/02-750 Automation of Scientific Research/GSE145668_AA_cells_counts.txt"
    control_cells = "/Users/raehash/Desktop/CMU/CMU Masters Year/Spring Semester/02-750 Automation of Scientific Research/GSE145668_Ctrl_cells_counts.txt"

    AA_df = pd.read_csv(AA_cells, delimiter='\t', header=0)
    Ctrl_df = pd.read_csv(control_cells, delimiter='\t', header=0)
    print(AA_df.shape, Ctrl_df.shape)
    combined_df = merged_df = Ctrl_df.merge(AA_df, on=['GeneName', 'GeneSymbol'], how='inner')
    print(combined_df.shape)
    combined_df.to_csv("GSE145668_combined_data.csv", sep = ",", index=False)