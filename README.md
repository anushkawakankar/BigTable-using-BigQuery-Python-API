# BigTable Homework
##### Anushka Wakankar 20171112
##### Aditya Khandelwal 20171117
---
This code uses BigQuery's python API to load a CSV table into a specified instance and project on the Google Cloud Platform. It then performs certain queries on the generated BigTable.

### Installation
Install the bigquery API using the command
```sh
$ pip install --upgrade google-cloud-bigquery
```
Make sure to create a Project and Instance on GCP and note down their names.

### Running the code

Use this command to delete any pre-existing tables with the same name as the table we are going to create. Alternatively, you could change the default name of the table on line 10.

```sh
$ bq rm datasetID.AssignmentTable1217
```

Use the following command to run the code after installing the API. Make sure the source file for the data is uploaded to your GCP Shell.

```sh
$ python code_20171112_20171117.py
```
Ignore any warnings about using python2. You can also remove these warnings by creating the following file before running the code.
```sh
$ touch ~/.cloudshell/no-python-warning
```

### The Assignment
- Input the project ID and instance ID when prompted. A table called AssignmentTable1217 will be created. The name is kept as such so it is unique even if you have other tables in your instance.
- Check whether the table path is generated correctly. If you have another table with the same path, you can change the path for this table on line 10.
```python
table_id = projectID+"."+datasetIDid+".AssignmentTable1217"
```
- Once this part of the code runs, you can reload your BigQuery page to find the table under your specified project and instance.
- This assignment was done assuming that the userID and itemID are integers. If these values are strings, we can simply comment the lines where the input is typecasted to int. Uncomment the lines right before these ones.
- There is first a menu which appears after every query. You can select the option required, and input the arguments for each query.

### The Questions
- int[] top(userID, K) : Get the top K items for a given userID with the highest view count. The input to this function will be the userID and K.
- int  interested(itemID) : Get the number of users interested in a given itemID. The input to this function will be the itemID.
- int[] top_interested(itemID,K) : For a given itemID, find the top K items that are of interest to those who viewed this item. The itemID and K are part of the input.
- int view_count(itemID) : Get the total view count for a given itemID. The input to this function is the itemID.
- int popular() : Get the itemID of the most popular item in the database.

Input your choices and the arguments to the functions as and when prompted.
