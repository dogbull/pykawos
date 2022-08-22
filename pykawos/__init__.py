import datetime
import os

import pandas as pd
import geopandas as gpd
from dateutil.parser import parse as str2datm

from .mapper import STATION_LIST_HEADER_MAPPER

BASE_URL = 'https://raw.githubusercontent.com/dogbull/kawos/master/'


def read(sub_url, cache_dir):
    if cache_dir:
        cache_path = f'{cache_dir}/{sub_url}'
    else:
        cache_path = None

    if cache_path and os.path.exists(cache_path):
        df = pd.read_csv(cache_path)
    else:
        data_url = f'{BASE_URL}/{sub_url}'
        df = pd.read_csv(data_url)
        if cache_path:
            os.makedirs(os.path.dirname(cache_path), exist_ok=True)
            df.to_csv(cache_path, index=False)
    col_set = set(df.columns)
    if len({'lon', 'lat'} - col_set) == 0:
        geometry = gpd.points_from_xy(x=df.lon, y=df.lat)
    elif len({'경도', '위도'} - col_set) == 0:
        geometry = gpd.points_from_xy(x=df['경도'], y=df['위도'])
    elif len({'x', 'y'} - col_set) == 0:
        geometry = gpd.points_from_xy(x=df.x, y=df.y)
    else:
        geometry = None
    if geometry:
        df = gpd.GeoDataFrame(df, crs='epsg:4326', geometry=geometry)
    return df


def read_stations(category, cache_dir='./.kawos', *, kor_header=False):
    df = read(f'/stations/{category}.stations.csv', cache_dir)
    if not kor_header:
        df = df.rename(columns=STATION_LIST_HEADER_MAPPER)
    return df


def read_asos_stations(*, cache_dir='./.kawos', kor_header=False):
    return read_stations('asos', cache_dir, kor_header=kor_header)


def read_aws_stations(*, cache_dir='./.kawos', kor_header=False):
    return read_stations('aws', cache_dir, kor_header=kor_header)


def read_single_point(category, code, begin, until, *, cache_dir='./.kawos'):
    if isinstance(begin, (datetime.date,)):
        begin_year = begin.year
    elif isinstance(begin, (str,)):
        begin = str2datm(begin).date()
        begin_year = begin.year
    else:
        begin_year = int(begin)

    if isinstance(until, (datetime.date,)):
        until_year = until.year
    elif isinstance(until, (str,)):
        until = str2datm(until).date()
        until_year = until.year
    else:
        until_year = int(until)

    df_ary = []
    for year in range(begin_year, until_year + 1):
        df = read(f'/pointly/{category}/{code}/{year}/{code}.{year}.csv', cache_dir)
        df_ary.append(df)
    df = pd.concat(df_ary)

    if isinstance(begin, (datetime.date,)):
        df = df[df['dt'] >= begin.strftime('%Y-%m-%d')]
    if isinstance(until, (datetime.date,)):
        df = df[df['dt'] <= until.strftime('%Y-%m-%d')]

    return df.reset_index()


def read_multi_point(category, date, *, cache_dir='./.kawos'):
    if isinstance(date, (str,)):
        date = str2datm(date)

    df = read(date.strftime(f'/daily/{category}daily/%Y/%m/%d/{category}daily.%Y-%m-%d.csv'), cache_dir)

    return df


def read_asos_single_point(code, begin, until, *, cache_dir='./.kawos'):
    return read_single_point('asos', code, begin, until, cache_dir=cache_dir)


def read_asos_multi_point(date, *, cache_dir='./.kawos'):
    return read_multi_point('asos', date, cache_dir=cache_dir)


def read_aws_single_point(code, begin, until, *, cache_dir='./.kawos'):
    return read_single_point('aws', code, begin, until, cache_dir=cache_dir)


def read_aws_multi_point(date, *, cache_dir='./.kawos'):
    return read_multi_point('aws', date, cache_dir=cache_dir)
