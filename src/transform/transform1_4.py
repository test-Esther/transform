import pandas as pd

def merge(load_dt='20160101'):
    read_df=pd.read_parquet('~/tmp/team_parquet')
    cols=['movieNm',
        'salesAmt',
        'openDt',
        'load_dt'
            ]
    df=read_df[cols]
    df['load_dt']=df['load_dt'].astype("object")
    df['movieNm']=df['movieNm'].astype('object')
    df['salesAmt']=df['salesAmt'].astype('object')
    df['openDt']=df['openDt'].astype('object')

    df.to_parquet('~/tmp/test_parquet_transform', partition_cols=['load_dt'])
    



