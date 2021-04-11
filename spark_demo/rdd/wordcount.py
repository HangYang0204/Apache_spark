from pyspark import SparkContext

if __name__ == '__main__':
    sc = SparkContext("local[3]","word count")
    sc.setLogLevel("ERROR");
    