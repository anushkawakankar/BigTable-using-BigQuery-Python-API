from google.cloud import bigquery

client = bigquery.Client()
#------------------------------------------------------------------------------
print("Enter project id")
pid = raw_input()
print("Enter instance id")
inid = raw_input()
# TODO(developer): Set table_id to the ID of the table to create.
table_id = pid+"."+inid+".AssignmentTable1217"

print(table_id)
job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV, skip_leading_rows=1, autodetect=True,
)
print("Enter filepath")
file = raw_input()
with open(file, "rb") as source_file:
    job = client.load_table_from_file(source_file, table_id, job_config=job_config)

job.result()  # Waits for the job to complete.

table = client.get_table(table_id)  # Make an API request.
print(
    "Loaded {} rows and {} columns to {}".format(
        table.num_rows, len(table.schema), table_id
    )
)
#------------------------------------------------------------------------------
while (True):
    print("Which query do you wanna run?")
    print("1) int[] top(userID, K) : Get the top K items for a given userID with the highest view count.")
    print("2) int interested(itemID) : Get the number of users interested in a given itemID.")
    print("3) int[] top_interested(itemID,K) : For a given itemID, find the top K items that are of interest to those who viewed this item. ")
    print("4) int view_count(itemID) : Get the total view count for a given itemID. ")
    print("5) int popular() : Get the itemID of the most popular item in the database.")
    print("0 to exit\n")

    num = raw_input()
    num = int(num)
    if num==1:
        print("Question 1\n")
        print("Enter userID and K")
        inp = raw_input()
        inp = inp.split(' ')

        # uid = "'"+inp[0]+"'"
        uid = int(inp[0])
        k = int(inp[1])

        query_job = client.query(
            """
            SELECT * FROM {0}
            WHERE userID = {1}
            ORDER BY viewCount DESC
            LIMIT {2}
            """.format(table_id,uid,k)

        )

        results = query_job.result()  # Waits for job to complete.

        print("itemID"+"\t"+"viewCount")
        for row in results:
            print(row.itemID, row.viewCount)

        print("\n")
    #------------------------------------------------------------------------------
    if num == 2:
        print("Question 2\n")
        print("Enter itemID")
        iid = raw_input()
        # iid = "'"+iid+"'"
        iid = int(iid)

        query_job = client.query(
            """
            SELECT COUNT(*) FROM {0}
            WHERE itemID = {1} AND viewCount != 0
            """.format(table_id,iid)

        )

        results = query_job.result()  # Waits for job to complete.
        print("No. of users")
        for row in results:
            print(row[0])
        print("\n")
    #------------------------------------------------------------------------------
    if num == 3:
        print("\n")
        print("Question 3\n")
        print("Enter itemID and K")
        inp = raw_input()
        inp = inp.split(' ')
        # iid = "'"+inp[0]+"'"
        iid = int(inp[0])
        k = int(inp[1])

        query_job = client.query(
            """
            SELECT userID FROM {0}
            WHERE itemID = {1} AND viewCount != 0
            """.format(table_id,iid)

        )

        results = query_job.result()
        print("userID"+"\t"+"itemID")
        for row in results:
            # name = "'"+row[0]+"'"
            query_job2 = client.query(
                """
                SELECT * FROM {0}
                WHERE userID = {1}
                ORDER BY viewCount DESC
                LIMIT {2}
                """.format(table_id,row[0],k)

            )

            results2 = query_job2.result()
            for row2 in results2:
                print(row2.userID, row2.itemID)


        print("\n")
    #------------------------------------------------------------------------------

    if num == 4:
        print("Question 4\n")
        print("Enter itemID")
        iid = raw_input()
        iid = int(iid)
        # iid = "'"+iid+"'"

        query_job = client.query(
            """
            SELECT SUM(viewCount) FROM {0}
            WHERE itemID = {1}
            """.format(table_id,iid)

        )
        results = query_job.result()
        print("Total Views")
        for row in results:
            print(row[0])

        print("\n")
    #------------------------------------------------------------------------------

    if num == 5:
        print("Question 5\n")
        query_job = client.query(
            """
            SELECT itemID, COUNT(userID) FROM {0}
            GROUP BY itemID
            LIMIT 1
            """.format(table_id)

        )

        print("itemID"+"\t"+"Total People Interested")
        results = query_job.result()
        for row in results:
            print(row[0],row[1])

        print("\n")
    #------------------------------------------------------------------------------
    if num == 0:
        exit()
