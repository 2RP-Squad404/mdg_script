import pandas as pd 
from google.cloud import bigquery
from pandas_gbq import to_gbq
from google.oauth2 import service_account
from datagen import generate_account
from config import settings


cred = service_account.Credentials.from_service_account_file(
    r'/mnt/c/Estagio/First-demand/mock_data/mock-data-bq/mock_data/big-maxim-430019-g7-6fa6ca43c9b3.json'
)

account_df = pd.DataFrame.from_dict(generate_account(), orient='index')


cols = ['account_id', 'status_id', 'due_day', 'person_id', 'balance']
# for i in 5:
#     account_df[cols[i]] = account_df[cols[i]].astype(str)
    
account_df.astype(int)
    
    
print(account_df.head())
print(account_df.dtypes)
# account_df.to_gbq(destination_table=settings.TABLE_ID, project_id=settings.PROJECT_ID, if_exists='replace', credentials=cred) 