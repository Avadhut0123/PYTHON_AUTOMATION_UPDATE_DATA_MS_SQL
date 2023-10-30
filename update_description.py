import pyodbc
import pandas as pd
import os

class Update_DESCRIPTION:
    global cur
    conn = ("""driver={SQL Server};server=10.10.10.56;database=EMIZA-AUGMENTED-TEST;
        trusted_connection=no;UID=CCS02;PWD=Pass@1234;IntegratedSecurity = true;""")
    conx = pyodbc.connect(conn)
    cur = conx.cursor()

    def reading_csv(self):
        Dataset = pd.read_csv(r'C:\Users\Emiza\Desktop\Dummy_file.csv')
        Dict_data = Dataset.to_dict(orient='records')

        for x in range(len(Dict_data)):
            TABLE_DATA = Dict_data[x]
            # print(TABLE_DATA)
            ITEMID = str(TABLE_DATA["ItemId"])              #SKU CODE
            # print(ITEMID)
            DESCRIPTION = str(TABLE_DATA["Description"])    #Decription of SKU
            # print(DESCRIPTION)
            self.Update(DESCRIPTION,ITEMID)

    def Update(self,DESCRIPTION,ITEMID):
        # reading_csv = self.reading_csv()

        Update_query = "UPDATE ItemMaster SET Description = '"+DESCRIPTION+"' WHERE ItemId = '"+ITEMID+"'"
        # print(Update_query)
        exe2 = cur.execute(Update_query)
        cur.commit()
        print("Description Updated Successfully")

a1 =Update_DESCRIPTION()
a1.reading_csv()

