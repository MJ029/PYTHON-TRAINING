import pyspark
from delta import *

if __name__ == "__main__":

    builder = pyspark.sql.SparkSession.builder.appName("MyApp") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")

    spark = configure_spark_with_delta_pip(builder).getOrCreate()

    df = spark.read.format("CSV").option("header", "true").load("C:\\Users\\manij\\Downloads\\WIPRO.BO.csv")
    # df.show(10, False)

    # df.write.format("csv").mode("overwrite").option("header", "true").save("D:\\Github\\PYTHON-TRAINING\\output\\CSV-WRITE")
    # df.write.format("delta").mode("overwrite").save(
    #     "D:\\Github\\PYTHON-TRAINING\\output\\DELTA-WRITE")
    # df.write.format("parquet").mode("overwrite").partitionBy("Date").save(
    #     "D:\\Github\\PYTHON-TRAINING\\output\\DELTA-WRITE-PARTITION")


    table = DeltaTable.forPath(sparkSession=spark, path="D:\\Github\\PYTHON-TRAINING\\output\\DELTA-WRITE")
    table.alias("src").merge(df.alias("tgt"), "src.Date=tgt.Date").whenMatchedUpdateAll().whenNotMatchedInsertAll().execute()
    table.history().show(10, False)