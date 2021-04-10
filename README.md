## Apache_spark

To get start with Spark we must first install it on your computer. If you are using Windows like me just follow the following steps:

### 1. Get started with installation
1. first you need to get java 8/11 installed, preferable at the following directory C:\java\jdk1.8.0_231 
2. Python 3 installed, just follow the steps from https://www.python.org/
3. Download the winutils.exe (If you don't want to google it, you can find in utils\), create new directory C:\hadoop\bin and place it there.
4. Create directory C:\tmp\hive 
5. download spark from https://spark.apache.org/ and unpack it. preferable at this directory C:\spark-3.1.1-bin-hadoop2.7

### 2. Some config in windows
1. Create new PATH as HADOOP_HOME at  C:\hadoop\bin
2. Create new PATH as SPARK_HOME at C:\spark-3.1.1-bin-hadoop2.7
3. Create new PATH as JAVA_HOME at C:\java\jdk1.8.0_231 
4. Add Binary sub-path in the environment variable named PATH e.g. 
      PATH = ...; %HADOOP_HOME%\bin; 
5. Go to C:\spark-3.1.1-bin-hadoop2.7\conf\ find config file log4j.properties.template, copy paste and rename as log4j.properties
6. Open the file and set log4j.rootCategory=ERROR, console

### 3. Try it out
Open the cmd, type pyspark or spark-shell, you should be able to see spark logo pop up in the console. 