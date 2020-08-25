# apriori-algorithm-in-python

This program implements a simplified version of the Apriori algorithm ([Agrawal & Srikant, 1994](http://www.vldb.org/conf/1994/P487.PDF)).

The Apriori algorithm is used for frequent item set mining and association rule learning over relational databases. The frequent item sets determined by Apriori can be used to determine association rules which highlight general trends in the database: this has applications in domains such as market basket analysis.

The main principle behind the Apriori algortithm is the Downward Closure Lemma, which states that if an item set 'X' is not frequent, then any item set that contains 'X' is guaranteed to be not frequent.

In order to optimize the search, the Apriori algorithm starts by determining the support of all 1-attribute item sets, discarding all that fall below the desired frequency threshold. It then proceeds to search all 2-attribute item sets whose attributes have not been discarded in the first step, and so on with item sets of increasing number of attributes, until the desired size is reached. At each level, item sets that fall below the desired frequency threshold are discarded (aka "pruning"). This decrease in the number of possible combinations obtained by pruning is the root of Apriori's efficiency.

As an example of the performance gain obtained when using the Apriori algorithm, let's calculate who long it would take to find all item sets with 4 attributes and support >= 0.6.

In the data base that is being used with this program, there are 1,620,163 different item sets with 4 attributes. I profiled the Python code used to count the item set occurences, and measured its execution time as approximately 1.41 ms for each combination, in my machine. Thus, the total time for a brute force search would be 2,284 seconds (approximately 38 minutes).
In my machine, the same search is carried out in 15 seconds, using my implementation of the Apriori algorithm.
In other words, it runs 152 times faster.
