# app/pydantic_models.py

from typing import Literal

import pandas as pd
from pydantic import BaseModel

class Observation(BaseModel):
    """
    An observation of a flower's measurments.
    """
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

    def as_dataframe(self) -> pd.DataFrame:
        """
        Convert this record to a DataFrame with one row.
        """
        return pd.DataFrame([self.as_row()])

    def as_row(self) -> pd.Series:
        row = pd.Series({
            "sepal length (cm)": self.sepal_length,
            "sepal width (cm)": self.sepal_width,
            "petal length (cm)": self.petal_length,
            "petal width (cm)": self.petal_width,
        })
        return row

class Prediction(BaseModel):
    """
    A prediction of the species of a flower.
    """
    flower_type: Literal["setosa", "versicolor", "virginica"]