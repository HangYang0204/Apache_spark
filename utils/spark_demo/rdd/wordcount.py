from pyspark import SparkContext,SparkConf 
import os

os.environ["PYSPARK_PYTHON"] = "C:\Python\python"
os.environ["PYSPARK_DRIVER_PYTHON"] = "C:\Python\python"
if __name__ == '__main__':
    conf = SparkConf().setAppName("word count").setMaster("local[3]")
    sc = SparkContext(conf = conf)
    sc.setLogLevel("ERROR");

    lines = sc.textFile("in/word_count.text")

    words = lines.flatMap(lambda line: line.split(" "))

    wordCounts = words.countByValue()
    for key in wordCounts:
        print(key, " : ", wordCounts[key])

