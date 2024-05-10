import pandas as pd

def import_dataset():
    bgg = pd.read_csv("boardgames_ranks.csv")
    bg_by_data_creation(bgg)

def bg_by_data_creation(bgg):
    print(bgg.shape)
    print(bgg.columns)

    

if __name__ == "__main__":
    import_dataset()