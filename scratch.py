fns = [
    'unique users with recording_202504151728_annual.csv',
    'unique users with recording_202504151739_monthly.csv',
    'unique users with recording_202504151742_quarterly.csv',
]

"""
'Annual New Recordings_GPDB_202504091533.csv',
'Annual New Recordings_HEDB_202504091544.csv',
'Annual New Users_GPDB_202504091535.csv',
'Annual New Users_HEDB_202504091549.csv',
'Monthly New Recordings_GPDB_202504091531.csv',
'Monthly New Users_GPDB_202504091536.csv',
'Monthly New Users_HEDB_202504091548.csv',
'Quarterly New Recordings_GPDB_202504091533.csv',
'Quarterly New Recordings_HEDB_202504091540.csv',
'Quarterly New Users_GPDB_202504091536.csv',
'Quarterly New Users_HEDB_202504091549.csv',
]"""

path = '/Users/zacwhitney/Documents/Misc Requests/'

for file in fns:
    print(f'Working on {file}')
    
    df = pd.read_csv(path + file)
    try:
        df['cumulative'] = df['count'].cumsum()
    except KeyError as e:
        print(df.columns)
        breakpoint()
        
    output_fn = (path + 'reports with cumsum/' +
                 file.rstrip('.csv') + '_withCumsum.csv')
    df.to_csv(output_fn, index=False)


fns2 = [
    'unique users with recording_202504151728_annual_withCumsum.csv',
    'unique users with recording_202504151739_monthly_withCumsum.csv',
    'unique users with recording_202504151742_quarterly_withCumsum.csv',
]

"""
'Annual New Recordings_HEDB_202504091544_withCumsum.csv',
'Annual New Users_GPDB_202504091535_withCumsum.csv',
'Annual New Users_HEDB_202504091549_withCumsum.csv',
'Monthly New Recordings_GPDB_202504091531_withCumsum.csv',
'Monthly New Users_GPDB_202504091536_withCumsum.csv',
'Monthly New Users_HEDB_202504091548_withCumsum.csv',
'Quarterly New Recordings_GPDB_202504091533_withCumsum.csv',
'Quarterly New Recordings_HEDB_202504091540_withCumsum.csv',
'Quarterly New Users_GPDB_202504091536_withCumsum.csv',
'Quarterly New Users_HEDB_202504091549_withCumsum.csv',
]"""

path += 'reports with cumsum/'

import gspread
from gspread_dataframe import set_with_dataframe

gc = gspread.oauth()

statsSheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/1JqsY5377yFzItgFun54uL7r1zI-nkjOP0TF1F4iLhjI/edit?gid=1818390421#gid=1818390421')
destTab = statsSheet.worksheet('Unique Users with Recordings')

import re

col = 1
for fn in fns2:
    df = pd.read_csv(path + fn)
    #fn = re.sub('_\d+.*', '', fn)
    #newTab = statsSheet.add_worksheet(fn, 5, 200)

    set_with_dataframe(destTab, df, col=col)
    col += 4
    

    
#    = ifs(month(E2) = 1, concat("Q1 ", year(E2)), month(E2) = 4, concat("Q2 ", year(E2)), month(E2)=7, concat("Q3 ", year(E2)), month(E2)=10, concat("Q4 ", year(E2)), TRUE, "")
