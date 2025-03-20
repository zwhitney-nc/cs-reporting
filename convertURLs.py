import pandas as pd
from numpy import nan
from datetime import datetime
import re

#update these before running each time
path = '/Users/zacwhitney/Documents/CS_Reporting/'
database = 'hedb'
input_fns = [
    'rccd_HEDB_recordings_2025.03.20_lti1.3.csv',
    'rccd_HEDB_recordings_2025.03.20_lti1.1.csv',
    
]
             

output_fn = input_fns[0].rstrip('.csv') + '_converted.csv'
dedupe = True
#recordCols = ['recording']

# date/time formats
sqlformat = '%Y-%m-%d %H:%M:%S.%f'
excelformat = '%m/%d/%Y %I:%M:%S %p'
# 12 hour time: '%I:%M %p'


if len(input_fns) == 1:
    df = pd.read_csv(path + input_fns[0])
else:
    df = pd.concat([pd.read_csv(path + x) for x in input_fns])
    output_fn = re.sub(r'_lti1\.\d', '', output_fn, flags=re.I)

    
if database == 'hedb':
    prefix = 'https://us-nc-recordings.s3.amazonaws.com/'

    def convertURL_HEDB(rec_id):
        if pd.isna(rec_id):
            return rec_id
        else:
            return (prefix + rec_id + '.mp3')

    df['recording'] = df['recording'].apply(convertURL_HEDB)

elif database == 'gpdb':
    prefix = 'https://nc-library-recordings.s3.us-west-1.amazonaws.com/uploads/recording/'
    
    def convertURL_GPDB(x):
        #if any(pd.isna([x['id'], x['raw_s3_location']])):
        #    return nan
        if pd.isna(x['id']):
            return nan
        elif pd.notna(x['raw_s3_location']):
            return (prefix + 'raw_s3_location/' + x['id'] + '/' +
                    x['raw_s3_location'])
        
        elif pd.notna(x['s3_location']):
            return (prefix + 's3_location/' + x['id'] + '/' +
                    x['s3_location'])
        else:
            return nan

    df['recording_url'] = df.apply(convertURL_GPDB, axis = 1)


        

# convert datetimes to play nicer with excel formatting
def convertTime(x):
    temptime = datetime.fromisoformat(x)
    return temptime.strftime(excelformat)


if 'created_at' in df.columns:
    df['created_at'] = df['created_at'].apply(convertTime)

if 'updated_at' in df.columns:
    df['updated_at'] = df['updated_at'].apply(convertTime)

    
# sort and dedupe
if 'created_at' in df.columns:
    df.sort_values(by='created_at',
                   ascending=False,
                   inplace=True,
                   key = lambda x: pd.to_datetime(x, format='ISO8601'))

if dedupe:
    if database == 'hedb':
        df.drop_duplicates(subset='email', inplace=True)
    elif database == 'gpdb':
        df.drop_duplicates(subset='speaker_worker_id', inplace=True)



df.to_csv(path + output_fn, index = False)

    



### scratch
"""
from datetime import timedelta
from dateutil.relativedelta import relativedelta

#df['created_at'] = df['created_at'].apply(lambda x: datetime.strptime(x, excelformat))
df['created_at'] = df['created_at'].apply(
    lambda x: datetime.strptime(x, sqlformat))

start = datetime(2020, 1, 1)
end = start + relativedelta(months=+6)
mdy = '%m/%d/%Y'

results = {}

while start < datetime.now():
    temp = df.loc[(df['created_at'] >= start) & (df['created_at'] < end)]
    key = f"{start.strftime(mdy)} ~ {end.strftime(mdy)}"

    results[key] = temp.shape[0]

    start = end
    end = start + relativedelta(months=+6)


"""
