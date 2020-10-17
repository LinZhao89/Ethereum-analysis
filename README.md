# Temporal-Analysis-of-the-Entire-Ethereum-Blockchain-Network
<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Data Extraction](#Data-Extraction)
  * [Google_bigquery](#Google-bigquery)
  * [Kaggle](#Kaggle)
  * [Github](#github)
* [Table Explanation](#Table-Explanation)  
* [Useful linkes](#Useful-linkes)



<!-- ABOUT THE PROJECT -->
## About The Project

xxxxxxxxxxxxxxxxxxxxxxxxxx


<!-- Data Extraction -->
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




<!-- Table Explanation -->
## Table Explanation
We extract all relevant data from dataset under the Google Cloud till 2019-12-31 23:59:45 UTC, which amounts to all blocks from genesis (#0) up to #9193265. The entire blockchain data is stored in seven different tables, out of which, we extract data from `contracts`, `token transfers`, `traces`, and `transactions` tables for our temporal analysis.

* The trace table stores executions of all recorded messages and transactions (successful ones) in the Ethereum blockchain. This is the most comprehensive tables for analysis. * The transactions table contains all transaction details such as source and target address, and amount of ether transferred. 
* The contracts table contains all Contract Accounts, their byte code and other properties of byte code such as block_timestamp}, block_number, token types (e.g., ERC721, ERC20). 
* The token transfers table focuses on all transactions with tokens from one 20-byte address to another 20-byte address on the blockchain.


<!-- Useful linkes -->
## Useful linkes
* [Github ethereum](https://github.com/blockchain-etl/ethereum-etl)
* [Google bigquery](https://cloud.google.com/bigquery)
* [Kaggle](https://www.kaggle.com/bigquery/ethereum-blockchain)
