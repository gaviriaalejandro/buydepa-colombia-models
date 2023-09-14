import warnings
from sqlalchemy import create_engine
from multiprocessing import Pool
warnings.filterwarnings("ignore") 

def upload_data_massive(df, tabla, user, password, host, schema):
    engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{schema}')
    df.to_sql(tabla, engine, if_exists='append', index=False, chunksize=1000)

def process_data(data, tabla, chunk, user, password, host, schema):
    pool        = Pool(10)
    futures     = [] 
    datadivided = [data[i:i + data.shape[0]//chunk] for i in range(0, data.shape[0], data.shape[0]//chunk)]
    for x in datadivided:
        futures.append(pool.apply_async(upload_data_massive,args = (x, tabla, user, password, host, schema, )))
    for future in futures:
        future.get()