# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
from logging import Logger

from pydantic import Field
from pyspark.sql import SparkSession

from data_rafting_kit.common.base_spec import BaseSpec
from data_rafting_kit.common.pipeline_dataframe_holder import PipelineDataframeHolder
from data_rafting_kit.common.str_enum import StrEnum


class TransformationEnum(StrEnum):
    """Enumeration class for transformation types."""

    AGG = "agg"
    ANONYMIZE = "anonymize"
    DISTINCT = "distinct"
    DROP = "drop"
    DROP_DUPLICATES = "drop_duplicates"
    FILTER = "filter"
    GROUP_BY = "group_by"
    INTERSECT = "intersect"
    JOIN = "join"
    WITH_COLUMNS = "with_columns"
    WITH_COLUMNS_RENAMED = "with_columns_renamed"
    WINDOW = "window"
    SELECT = "select"
    FILL_NA = "fill_na"
    LIMIT = "limit"
    OFFSET = "offset"
    DROP_NA = "drop_na"
    ORDER_BY = "order_by"


class TransformationBaseSpec(BaseSpec):
    """Base output specification."""

    input_df: str | None = Field(default=None)


class TransformationBase:
    """Represents a transformation object for data pipelines.

    Attributes
    ----------
        _spark (SparkSession): The SparkSession object.
        _logger (Logger): The logger object.
        _dfs (PipelineDataframeHolder): The ordered dictionary of DataFrames.

    """

    def __init__(
        self,
        spark: SparkSession,
        logger: Logger,
        dfs: PipelineDataframeHolder,
        env,
        run_id: str | None = None,
    ):
        """Initializes an instance of the Transformation class.

        Args:
        ----
            spark (SparkSession): The SparkSession object.
            logger (Logger): The logger object.
            dfs (PipelineDataframeHolder): The ordered dictionary of DataFrames.
            env (EnvSpec): The environment specification.
            run_id (str | None): The run ID.

        """
        self._spark = spark
        self._logger = logger
        self._dfs = dfs
        self._env = env
        self._run_id = run_id
