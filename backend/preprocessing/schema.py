"""
Docstring for backend.preprocessing.schema

This module is a collection of functions to dynamically create a schema from imported data
"""

from typing import BinaryIO
import pandas as pd
from enum import Enum

class FileType(Enum):
    XLS = "xls"
    XLSX = 'xlsx'
    CSV = "csv"

def is_numeric(series: pd.Series, coerced_threshold=0.1) -> bool:
    """
    Docstring for is_numeric
    
    :param series: a features' column values (array values)
    :type series: pd.Series
    :param coerced_threshold: Ratio of NaT to converted numeric values
    :return: true if coerced threshold is not exceeded, else false
    :rtype: bool
    """
    coerced_series = pd.to_numeric(series, errors="coerce")
    ratio_coerced = 1.0 - coerced_series.notna().mean()
    return ratio_coerced <= coerced_threshold

def is_datetime(series: pd.Series, coerced_threshold=0.1) -> bool:
    """
    Docstring for is_datetime
    
    :param series: a features' column values (array values)
    :type series: pd.Series
    :param coerced_threshold: Ratio of NaT to converted numeric values
    :return: true if coerced threshold is not exceeded, else false
    :rtype: bool
    """
    coerced_series = pd.to_datetime(series, errors="coerce")
    ratio_coerced = 1.0 - coerced_series.notna().mean()
    return ratio_coerced <= coerced_threshold

def feature_type(series: pd.Series) -> str:
    """
    Docstring for feature_type
    
    :param series: The data column associated with the feature
    :type series: pd.Series
    :return: string value indicating the data type of the series (e.g. numeric, datetime or categorical)
    :rtype: str
    """

    if is_numeric(series):
        return "numeric"
    elif is_datetime(series):
        return "datetime"
    else:
        return "categorical"


def build_schema(filePath: str, hasHeaders: bool, filetype: FileType) -> dict[str, str]:
    """
    Docstring for build_schema
    
    :param filePath: path to the excel or csv vile
    :type filePath: str
    :param hasHeaders: true if the table has headers, else false
    :type hasHeaders: bool
    :param filetype: Description
    :type filetype: FileType
    :return: Description
    :rtype: dict[str, str]
    """
    if filetype in (FileType.XLS, FileType.XLSX):
        df = pd.read_excel(filePath)
    else:
        df = pd.read_csv(filePath)

    if not hasHeaders:
        df.columns = [f"col_{i}" for i in range(df.shape[1])]

    return {col: feature_type(df[col]) for col in df.columns}



