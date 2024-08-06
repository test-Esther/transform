import pandas as pd

def merge(load_dt='20160101'):
    read_df=pd.read_parquet('~/tmp/team_parquet')
    cols=['movieNm',
        'salesAmt',
        'openDt'
            ]
    df=read_df[cols]

    df['movieNm']=df['movieNm'].astype('object')
    df['salesAmt']=df['salesAmt'].astype('object')
    df['openDt']=df['openDt'].astype('object')

    print(df)
    
    


merge()
