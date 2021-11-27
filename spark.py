## Imports
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession

## Module Constants
APP_NAME = "My Spark Application"

## Closure Functions

## Main functionality

def main(sc):
    print("**************Hello from Spark***************")

if __name__ == "__main__":
   # Configure Spark
   # conf = SparkConf() .setAppName (APP_NAME)
   # conf = conf.setMaster('spark://10.88.0.28:7077').setSparkHome('/opt/bitnami/spark')
   conf = SparkSession.builder.master('http://ocp-spark-test.apps.ocp.insurkart.in/').getOrCreate ()
   sc  = SparkContext(conf=conf)

   # Execute Main functionality
   main(sc)
