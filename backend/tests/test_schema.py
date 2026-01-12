import pathlib
import pandas as pd
import numpy as np
from preprocessing import schema


TEST_DIR = pathlib.Path(__file__).parent
FILE_DIR = TEST_DIR / "test-files"

class TestSchema:
    def test_is_numeric_passing_threshold(self):
        test_series = pd.Series([10, 20, 30, 40, 50])
        assert schema.is_numeric(test_series) == True
    
    def test_is_numeric_failing_threshold(self):
        test_series = pd.Series([1, 2, 3, "Nan"])
        assert schema.is_numeric(test_series) == False

    def test_is_datetime_passing_threshold(self):
        n_dates = 10
        start_date = pd.to_datetime("2020-01-01")
        end_date = pd.to_datetime("2023-12-31")

        random_dates = pd.to_datetime(
        np.random.randint(start_date.value // 10**9, end_date.value // 10**9, n_dates), unit='s')
        test_series = pd.Series(random_dates)

        assert schema.is_datetime(test_series) == True

    def test_is_datetime_failing_threshold(self):
        test_series = pd.Series([10, 20, 30, 40, 50])
        assert schema.is_datetime(test_series) == False
    
    def test_feature_type_categorical(self):
        test_series = pd.Series(["Hello", "World"])
        assert schema.feature_type(test_series) == "categorical"

    def test_feature_type_numerical(self):
        test_series = pd.Series([10, 20, 30, 40, 50])
        assert schema.feature_type(test_series) == "numeric"

    def test_feature_type_datetime(self):
        start_date = pd.to_datetime("2020-01-01")
        end_date = pd.to_datetime("2023-12-31")
        test_series = pd.Series([start_date, end_date])
        assert schema.feature_type(test_series) == "datetime"



