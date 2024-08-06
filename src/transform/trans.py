import pandas as pd

def merge(load_dt):
    read_df = pd.read_parquet('~/tmp/test_parquet')
    cols = ['movieCd', #영화의 대표코드를 출력합니다.
            'movieNm', #영화명(국문)을 출력합니다.
            'openDt', #영화의 개봉일을 출력합니다.
            'salesAmt', #해당일의 매출액을 출력합니다.
            'load_dt', # 입수일자
            'repNationCd', #한국외국영화 유무
            ]
    df = read_df[cols]
    # 개봉일을 datetime 형식으로 변환
    df['openDt'] = pd.to_datetime(df['openDt'], format='%Y%m%d')

    # 2016년 9월부터 12월 사이에 개봉한 영화 필터링
    start_date = '2016-09-01'
    end_date = '2016-12-31'
    df_filtered = df[(df['openDt'] >= start_date) & (df['openDt'] <= end_date)]

    # 매출액을 기준으로 상위 10개 영화 추출
    df_filtered['salesAmt'] = pd.to_numeric(df_filtered['salesAmt'], errors='coerce')  # 매출액을 숫자형으로 변환
    df_top10 = df_filtered.sort_values(by='salesAmt', ascending=False).head(10)i

    # 한국 영화만 필터링
    df_korean_movies = df_top10[df_top10['repNationCd'] == 'K']  # 'K'은 한국 영화

    print(df_korean_movies)
    #return df_korean_movies

    #df_w = df[(df['movieCd'] == '20247781') & (df['load_dt'] == int(load_dt))].copy()
    #print(df_w)
    #print(df_w.dtypes)

    # 카테고리 타입 -> Object
    #df_w['load_dt'] = df_w['load_dt'].astype('object')
    #df_w['multiMovieYn'] = df_w['multiMovieYn'].astype('object')
    #df_w['repNationCd'] = df_w['repNationCd'].astype('object')
    
    # NaN 값을 unknown 으로 변경
    #df_w['multiMovieYn'] = df_w['multiMovieYn'].fillna('unknown')
    #df_w['repNationCd'] = df_w['repNationCd'].fillna('unknown')
    #print(df_w.dtypes)
    #print(df_w)

    # 머지
    #u_mul = df_w[df_w['multiMovieYn'] == 'unknown']
    #u_nat = df_w[df_w['repNationCd'] == 'unknown']
    #m_df = pd.merge(u_mul, u_nat, on='movieCd', suffixes=('_m', '_n'))

    # 드랍
    #df_multiMovieYn = df_w[df_w['multiMovieYn'].isnull()].drop(columns='multiMovieYn').reset_index(drop=True)
    #df_repNationCd = df_w[df_w['repNationCd'].isnull()].drop(columns='repNationCd').reset_index(drop=True)
    #df_merge = df_multiMovieYn.merge(df_repNationCd, on=['movieCd', 'movieNm', 'load_dt'], how='outer')
    
    #print(df_merge)
    #return df_merge


merge()
