import pandas as pd

def merge(load_dt="20160101"):
    read_df = pd.read_parquet('/home/manggee/tmp/team_parquet')
    cols = [
       'movieNm', #영화명(국문)을 출력합니다.
        'openDt', #영화의 개봉일을 출력합니다.
        'salesAmt',
        'load_dt'
       ]
    df = read_df[cols]
    # 울버린만 조회
    # print(df.head(100))
    # dw = df[(df['movieCd'] == '20235974') & (df['load_dt'] == int(load_dt))].copy() #날짜조건 load_dt 인자 받기 print(dw)
    # print(dw.dtypes)

    # 카테고리 타입 -> Object
    df['movieNm'] = df['movieNm'].astype('object')
    df['openDt'] = df['openDt'].astype('object')
    df['salesAmt'] = df['salesAmt'].astype('object')
    df['load_dt'] = df['load_dt'].astype('object')
    print(df)

merge()
