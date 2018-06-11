#!/usr/bin/python
import pyspark
sc = pyspark.SparkContext()
rdd = sc.parallelize(['Hello,', 'world!'])
words = sorted(rdd.collect())
print words

# -------------------------------------------------------------------------------
from pyspark.sql import functions as F
from pyspark.sql.types import *
df_ies_2016 = sqlContext.read.format(formatPackage).options(header=’true’, delimiter = ‘|’).load(“/FileStore/tables/6dzmn5ul1509579188749/DM_IES_2016.CSV”)

# -------------------------------------------------------------------------------
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

medicare = spark.read.format(
   "com.databricks.spark.csv").option(
   "header", "true").option(
   "inferSchema", "true").load(
   's3://awsglue-datasets/examples/medicare/Medicare_Hospital_Provider.csv')
medicare.printSchema()
medicare_dynamicframe = glueContext.create_dynamic_frame.from_catalog(
       database = "payments",
       table_name = "medicare")
medicare_dynamicframe.printSchema()
medicare_res = medicare_dynamicframe.resolveChoice(specs = [('provider id','cast:long')])
medicare_res.printSchema()
medicare_res.toDF().where("'provider id' is NULL").show()
medicare_dataframe = medicare_res.toDF()
medicare_dataframe = medicare_dataframe.where("'provider id' is NOT NULL")

chop_f = udf(lambda x: x[1:], StringType())
medicare_dataframe = medicare_dataframe.withColumn(
        "ACC", chop_f(
            medicare_dataframe["average covered charges"])).withColumn(
                "ATP", chop_f(
                    medicare_dataframe["average total payments"])).withColumn(
                        "AMP", chop_f(
                            medicare_dataframe["average medicare payments"]))
medicare_dataframe.select(['ACC', 'ATP', 'AMP']).show()

Below code is Spark 2+
spark = pyspark.sql.SparkSession.builder.appName('test').getOrCreate()
spark.range(10).collect()

# -------------------------------------------------------------------------------
from pyspark.sql.functions import *
import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._

val txtFile = "README.md"
val txtData = sc.textFile(txtFile)
txtData.cache()

txtData.count()
val wcData = txtData.flatMap(l => l.split(" ")).map(word => (word, 1)).reduceByKey(_ + _)

wcData.collect().foreach(println)
