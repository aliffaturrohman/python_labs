from importnb import Notebook
with Notebook():
    from PenugasanPraktikum1.ipynb import fill_missing_values  # Ensure the notebook is named 'PenugasanPraktikum1.ipynb' and is in the same directory
import pandas as pd

def test_fill_missing_values():
    data = {
        "c1": [120.0, 130.0, 140.0, 150.0, None, 170.0],
        "c2": [7.0, None, 10.0, None, 5.5, 16.5]
    }
    index = pd.to_datetime([
        "2000-01-03",
        "2000-01-04",
        "2000-01-05",
        "2000-01-06",
        "2000-01-07",
        "2000-01-10"
    ])
    df_input = pd.DataFrame(data, index=index)

    expected_data = {
        "c1": [120.0, 130.0, 140.0, 150.0, 160.0, 170.0],
        "c2": [7.0, 8.5, 10.0, 7.75, 5.5, 16.5]
    }
    df_expected = pd.DataFrame(expected_data, index=index)

    user_output = fill_missing_values(df_input)
    
    assert isinstance(user_output, pd.DataFrame), "Output harus berupa DataFrame"
    assert user_output.equals(df_expected), f"\nOutput salah:\n{user_output}\n\nSeharusnya:\n{df_expected}"
    print("✅ Test passed!")
