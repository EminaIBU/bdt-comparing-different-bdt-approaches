Comparison of different Big Data Technologies approaches
==============================

What is this?
---------------

This is a simple Python application intended to provide a working example of three different Big Data Technologies Approaches. In this case, we will cover the problem of counting the Hootel Reviews from large dataset (1.4GB).

We will compare three approaches:
* MapReduce
* Apache Spark
* Conventional Python method for counting items

#### MapReduce
`MapReduce`, originally developed by Google, is a parallel processing framework that divides tasks into smaller chunks, making it suitable for large-scale data processing.\
We will use `MRJob` library to implement MapReduce in Python.

#### Apache Spark
`Apache Spark`, on the other hand, is a powerful, open-source cluster computing framework that offers in-memory data processing capabilities, enabling faster data analytics.\
We will use `pyspark` library to implement this in Python

#### Python's native counting method
In contrast, Python's native counting method relies on traditional loops and data structures for item enumeration.

Prerequisites
-------------

Python 3 (3.11.0)\
Required libraries from `requirements.txt`

How To Run This?
---------------

1. Download/clone this project
2. Download large dataset from this [URL](https://drive.google.com/file/d/1l9n7nPUh3ZcmBJzbnyg3BgDBVvFIMR0_/view?usp=sharing).\
   **NOTE:** We provided smaller dataset inside this project, but best approach is to download the larger one and replace it. 
3. Run `pip install -r requirements.txt` to install required dependencies
4. Run `python main.py`


Results
-------

After script is finished you will be able to see console output which will tell you how many Hotel Review ratings we counted and how long each approach required to count them.

![Console Output](https://i.imgur.com/xaN79cA.png)


#### Logs
After successfull run, there will be two folders generated `timing` and `logs` which will store the times and logs for each of three methods that we used.

Conclusion
-------

We can see that in our case, `Apache Spark` had the best performance, followed by `MapReduce` and we can see that traditional counting method was really slow in this case which confirms that sophisticated Big Data Technologies approaches must be used when we are dealing with large scale datasets.
