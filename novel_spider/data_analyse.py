import pandas as pd

if __name__ == '__main__':
    pd.set_option('display.max_colwidth', 10000)
    # pd.set_option("display.colheader_justify", "right")
    data = pd.read_csv('../data/group_data.txt', header=None, names=['x', 'y'], delimiter='\t')
    # print(data)
    data['y'] = data \
        .apply(lambda g: '\'' + g['y'] + '\'', axis=1)
    result = data.astype(str).groupby('y').apply(
        lambda g: ','.join('\'' + g['x'] + '\''))
    # result['x']=
    # print(type(result))
    print(result)
    # print(result.keys())
    # print(result.values())
