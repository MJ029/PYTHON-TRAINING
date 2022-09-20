import pyspark
from delta import *

if __name__ == "__main__":

    builder = pyspark.sql.SparkSession.builder.appName("MyApp") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")

    spark = configure_spark_with_delta_pip(builder).getOrCreate()

    df = spark.read.format("parquet").load("D:\\Github\\PYTHON-TRAINING\\output\\DELTA-WRITE-PARTITION")
    df.show(100, False)