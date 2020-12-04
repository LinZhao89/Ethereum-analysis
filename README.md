# Temporal-Analysis-of-the-Entire-Ethereum-Blockchain-Network
<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Data Extraction](#Data-Extraction)
  * [Google_bigquery](#Google-bigquery)
  * [Kaggle](#Kaggle)
  * [Github](#github)
* [Tables Explanation](#Table-Explanation)  
* [Scripts Explanation](#Script-Explanation)
  * [Network Extraction](#Network-Extraction)
  * [Graph Analysis](#Graph-Analysis)
  * [Community Detection and Prediction](#Community-Detection-and-Prediction)	
* [Useful linkes](#Useful-linkes)
* [Reference](#Reference)



<!-- ABOUT THE PROJECT -->
## About The Project

In this project, we investigate the evolutionary nature of Ethereum interaction networks from a temporal graph perspective. 


<!-- Data Extraction -->
## Data Extraction 
Due to the size limitation, instead of uploading the dataset, we will introduce the extraction method we are using to obtain the data. We also demonstrate a sample arc list and corresponding address hased table split by year and by month (only for Contract Net) in each folder.
### Google bigquery

1. Apply and login to Google Cloud Platform account.
2. Create a bucket to store your files.
3. Go to BigQuery and find the data set 'ethereum_blockchain'
4. Select the table with desired timestamp you want and 'Export to GCS'.
5. Then select the GCS location (the bucket created in step 2).
6. If csv is preferred: //file*.csv (e.g. tmpbucket/blocks/blocks*.csv).
7. The * will help to number the files as exporting the tables will split the data into multiple files.


Replace .csv with .txt or .json as per your preference.
Pip install gsutil
For downloaded entire folder: gsutil -m cp -r gs://bucketname/folder-name local-location
For downloaded multiple files: gsutil -m cp -r gs://bucketname/folder-name/filename* local-location

### Kaggle

Kaggle can be used to preview the data table columns. 

### Github

Please refer to the github page for more details. 




<!-- Tables Explanation -->
## Table Explanation
We extract all relevant data from dataset under the Google Cloud till 2019-12-31 23:59:45 UTC, which amounts to all blocks from genesis (#0) up to #9193265. The entire blockchain data is stored in seven different tables, out of which, we extract data from `contracts`, `token transfers`, `traces`, and `transactions` tables for our temporal analysis.

* The trace table stores executions of all recorded messages and transactions (successful ones) in the Ethereum blockchain. This is the most comprehensive tables for analysis.  
* The transactions table contains all transaction details such as source and target address, and amount of ether transferred. 

* The contracts table contains all Contract Accounts, their byte code and other properties of byte code such as block_timestamp}, block_number, token types (e.g., ERC721, ERC20). 

* The token transfers table focuses on all transactions with tokens from one 20-byte address to another 20-byte address on the blockchain.


<!-- Scripts Explanation -->
## Scripts Explanation

All the scripts are written in python 3.7. To run the script, please lunch a python tools like Anaconda or directly run "python xx.py" 


### Network Extraction 
[Link to the folder](Network_extraction/)

The folder contains four folders for transactionNet, traceNet,tokenNet and contractNet arc list and accounts extraction. 

For [transactionNet](Network_extraction/TransactionNet), [traceNet](Network_extraction/TraceNet), [tokenNet](Network_extraction/TokenNet)
 1. Annual graph 
 
    The raw data obtained from Google Bigquery is in annual basis.
    Scripts named as "tracexx.py","tokenxx.py" and "transactionxx.py" are to process annual-based raw data, form the annual based arc list and corresponding hash table. 

 2. Result

    Due to the file size limitation in github, only Year2015 annual arc list and hash table is uploaded as a reference 


For [contractNet](Network_extraction/ContractNet)
1. Annual graph 

   The raw data obtained from Google Bigquery is in annual basis.
   Scripts named as "xx_Annual_xx.py" is to process annual-based raw data, form the annual based arc list and corresponding hash table. 

2. Monthly graph 

   Script named as "xx_Monthly_xx.py" will not only form the arc list and hash table but also help to partition the arc list into different month by matching with the timestamp in raw data.

3. Result

   Due to the file size limitation in github, only ContractNet Year2015 annual arc list and hash table is uploaded as a reference in folder "contractNet_address_hash" and "contractNet_edgelist_example".



### Graph Analysis 
[Link to the folder](Graph_analysis/)

1. [Find common account in continuous years](graph_analysis/FindcommonAccount_contract.py)

   An example to analyze contractNet for Figure 2

2. [Find common account in continuous years](graph_analysis/FindcommonAccount_contract.py)

   An example to analyze contractNet for Figure 3

3. [Analyze graph network reciprocity, associtativity, connectedComponent, kcore properties](graph_analysis/igraph_reciprocity_associtativity_connectedComponent_kcore.py)

   [Analyze network pathLength, radius, diameter](graph_analysis/igraph_pathLength_radius_diameter_select500000_rm0.py)

   [Analyze network triangle, transitivity, aveClusteringCoeff](graph_analysis/igraph_triangle_transitivity_aveClusteringCoeff.py)

   [Analyze network vertices and arcs](graph_analysis/networkx_Count_vertex_arc_of_network.py)

   An example for extract network properties for section 4, 5 and 6
   
4. [Find tokenNet top10 degree accounts](graph_analysis/find_tokenNet_degree_top10.py)


### Community Detection and Predition 

1. Community Detection

   [Link to the folder](community_detection_prediction/community_detection/)

   There are 3 steps in community detection

   Step1: Identify communities using Multi-level algorithm
   
	[find_contract2019_community_multilevel_realEdgeIndex_3mon.py ](community_detection_prediction/community_detection/find_contract2019_community_multilevel_realEdgeIndex_3mon.py )
	
	Note: python igraph library output communities arc list using index instead of real value of nodes. In order to perform matching in next step, it is needed to attach values (which is annual basis index) to each nodes. 

    Step2: Match communities in 3-month dataset and 1-month dataset
    
	[Find_continuous_community1_grow_die_compareREALindex.py](community_detection_prediction/community_detection/Find_continuous_community1_grow_die_compareREALindex.py)
	
	This script makes use of vf2 algorithm for subiomorphism matching. The matching not only consider graph shape but also node values to be matched. 

    Step3: Extract properties for each community
    
	[extract_contract2016_properties.py](community_detection_prediction/community_detection/extract_contract2016_properties.py)
	
	The script extract local and global properties of each community to be training/testing data. 

2. Community Predition

   [Link to the folder](community_detection_prediction/community_prediction/)

   Individual 

   Scripts [logistic_regression.py](community_detection_prediction/community_prediction/logistic_regression.py)
   and [random_forest.py ](community_detection_prediction/community_prediction/random_forest.py )are used for each time period prediction. 
   The script are generalized, it only requires to input the class 1 and class 0 training features and labels. 
   There is a random selection function in the script to balance class 1 and class 0. It needs to adjust based input data. 

   Overall

   Scripts [logistic_regression_combine_allMonth.py](community_detection_prediction/community_prediction/logistic_regression_combine_allMonth.py)
   and [random_forest_combine_allMonth.py](community_detection_prediction/community_prediction/random_forest_combine_allMonth.py )are for competed year prediction. 
   So the training data are combined pior to input into the scripts. Therefore, the scipts are almost the same as individual scripts. 








<!-- Useful linkes -->
## Useful linkes
1. [Github ethereum](https://github.com/blockchain-etl/ethereum-etl)
2. [Google bigquery](https://cloud.google.com/bigquery)
3. [Kaggle](https://www.kaggle.com/bigquery/ethereum-blockchain)

<!-- Reference -->
## Reference
1. Evgeny Medvedev and the D5 team, "Ethereum ETL," https://github.com/blockchain-etl/ethereum-etl, 2018.
2. Ethereum Blockchain, https://www.kaggle.com/bigquery/ethereum-blockchain, 2020


