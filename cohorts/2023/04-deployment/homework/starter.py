import pickle
import pandas as pd
import sys
import numpy as np

with open('model.bin', 'rb') as f_in:
    dv, model = pickle.load(f_in)


categorical = ['PULocationID', 'DOLocationID']

def read_data(filename):
    df = pd.read_parquet(filename)
    
    df['duration'] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

    df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')
    
    return df

def get_processed_df(year,month):
    df = read_data(f'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year:04d}-{month:02d}.parquet')
    return df

def prediction(df):
    dicts = df[categorical].to_dict(orient='records')
    X_val = dv.transform(dicts)
    y_pred = model.predict(X_val)
    return y_pred

def output_file_path(year,month):
    return f'gs://mlops-data-2023/yellow/year={year:04d}/month={month:02d}/homework.parquet'

def save_results(df, y_pred,year,month):
    df_result = pd.DataFrame()
    df_result['ride_id'] = f'{year:04d}/{month:02d}_' + df.index.astype('str')
    df_result['predicted_duration'] = y_pred
    df_result.to_parquet(output_file_path(year,month),engine='pyarrow',compression=None, index=False)

# save_results(df, y_pred,2022,2)
def stats(y_predication):
    print("std. dev of prediction: ",np.std(y_predication),"Mean of prediction: ",np.mean(y_predication))

def run():
    year = int(sys.argv[1]) 
    month = int(sys.argv[2])
    processed_data=get_processed_df(year,month)
    preds=prediction(processed_data)
    stats(preds)
    
if __name__ == '__main__':
    run()