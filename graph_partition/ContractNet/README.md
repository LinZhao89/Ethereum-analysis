# ContractNet data preparation

## Annual graph 
The raw data obtained from Google Bigquery is in annual basis.
Scripts named as "xx_Annual_xx.py" is to process annual-based raw data, form the annual based edge list and corresponding hash table. 

## Monthly graph 
Script named as "xx_Monthly_xx.py" will not only form the edgelist and hash table but also help to partition the edgelist into different month by matching with the timestamp in raw data.

## Result
Due to the file size limitation in github, only ContractNet 2015 annual edgelist and hash table is uploaded as a reference in folder "contractNet_address_hash" and "contractNet_edgelist_example".
