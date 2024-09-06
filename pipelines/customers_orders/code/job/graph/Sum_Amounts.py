from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def Sum_Amounts(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df1 = in0.groupBy(col("account_open_date"))

    return df1.agg(
        first(col("order_id")).alias("order_id"), 
        first(col("amount")).alias("amount"), 
        first(col("first_name")).alias("first_name"), 
        first(col("last_name")).alias("last_name")
    )
