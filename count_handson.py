import datetime
import requests as rq
import pandas as pd
import matplotlib.pyplot as plt

file = 'image_pull_count.pkl.gz'
targets = [["kata", "irixjp/katacoda"], ["lint", "irixjp/lint-rules"]]

def save_df_to_pkl(df, file):
    df.to_pickle(file, compression='gzip')

def load_from_pkl(file):
    df = pd.read_pickle(file, compression='gzip')
    return df.copy()

def get_pull_count(image):
    ret = rq.get('https://registry.hub.docker.com/v2/repositories/' + image + '/')
    json = ret.json()
    return pd.to_numeric(json['pull_count'])

def make_data(targets):
    result = []
    
    for key, image in targets:
        ret = get_pull_count(image)
        result.append(ret)

    return result

def main():
    df_orig = load_from_pkl(file)
    today_data = make_data(targets)
    dt_now = pd.to_datetime(datetime.datetime.now())

    df_orig.loc[dt_now] = today_data
    save_df_to_pkl(df_orig, file)
    
    df = df_orig['kata'].dropna()
    plt.figure(facecolor="white")
    df.plot(figsize=(16, 12))
    plt.savefig('kata.png')
    plt.close('all')

    df = df_orig['lint'].dropna()
    plt.figure(facecolor="white")
    df.plot(figsize=(16, 12))
    plt.savefig('lint.png')
    plt.close('all')

main()
