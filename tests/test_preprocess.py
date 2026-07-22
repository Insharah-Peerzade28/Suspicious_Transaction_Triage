import pandas as pd
from src.preprocess import remove_duplicates

def test_remove_duplicates():

    data = {
        "A":[1,1,2],
        "B":[5,5,6]
    }

    df = pd.DataFrame(data)

    cleaned = remove_duplicates(df)

    assert len(cleaned) == 2
    