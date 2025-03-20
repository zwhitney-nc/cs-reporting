import pandas as pd
from pprint import pprint
from datetime import datetime

rdf_hedb = pd.read_csv('/Users/zacwhitney/Documents/CS_Reporting/HEDB total recordings 2024.csv')
rdf_gpdb = pd.read_csv('/Users/zacwhitney/Documents/CS_Reporting/GPDB total recordings 2024.csv')

pdf_hedb = pd.read_csv('/Users/zacwhitney/Documents/CS_Reporting/HEDB total playbacks 2024.csv')
pdf_gpdb = pd.read_csv('/Users/zacwhitney/Documents/CS_Reporting/GPDB total playbacks 2024.csv')

sqlformat = '%Y-%m-%d %H:%M:%S.%f'
rdf_hedb['created_at'] = rdf_hedb['created_at'].apply(
    lambda x: datetime.strptime(x, sqlformat))
rdf_gpdb['created_at'] = rdf_gpdb['created_at'].apply(
    lambda x: datetime.strptime(x, sqlformat))

pdf_hedb['created_at'] = pdf_hedb['created_at'].apply(
    lambda x: datetime.strptime(x, sqlformat))
pdf_gpdb['created_at'] = pdf_gpdb['created_at'].apply(
    lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))

q1hedb = len(rdf_hedb[
    (rdf_hedb['created_at'] >= '2024-01-01') &
    (rdf_hedb['created_at'] <= '2024-03-31')
])
q2hedb = len(rdf_hedb[
    (rdf_hedb['created_at'] > '2024-03-31') &
    (rdf_hedb['created_at'] <= '2024-06-30')
])
q3hedb = len(rdf_hedb[
    (rdf_hedb['created_at'] > '2024-06-30') &
    (rdf_hedb['created_at'] <= '2024-09-30')
])
q4hedb = len(rdf_hedb[
    (rdf_hedb['created_at'] > '2024-09-30') &
    (rdf_hedb['created_at'] <= '2024-12-31')
])

q1gpdb = len(rdf_gpdb[
    (rdf_gpdb['created_at'] >= '2024-01-01') &
    (rdf_gpdb['created_at'] <= '2024-03-31')
])
q2gpdb = len(rdf_gpdb[
    (rdf_gpdb['created_at'] > '2024-03-31') &
    (rdf_gpdb['created_at'] <= '2024-06-30')
])
q3gpdb = len(rdf_gpdb[
    (rdf_gpdb['created_at'] > '2024-06-30') &
    (rdf_gpdb['created_at'] <= '2024-09-30')
])
q4gpdb = len(rdf_gpdb[
    (rdf_gpdb['created_at'] > '2024-09-30') &
    (rdf_gpdb['created_at'] <= '2024-12-31')
])

recordings_result = f"""
Recordings:
Q1:
HEDB: {q1hedb}
GPDB: {q1gpdb}
Total: {q1hedb + q1gpdb}

Q2:
HEDB: {q2hedb}
GPDB: {q2gpdb}
Total: {q2hedb + q2gpdb}

Q3:
HEDB: {q3hedb}
GPDB: {q3gpdb}
Total: {q3hedb + q3gpdb}

Q4:
HEDB: {q4hedb}
GPDB: {q4gpdb}
Total: {q4hedb + q4gpdb}


"""

q1hedb = len(pdf_hedb[
    (pdf_hedb['created_at'] >= '2024-01-01') &
    (pdf_hedb['created_at'] <= '2024-03-31')
])
q2hedb = len(pdf_hedb[
    (pdf_hedb['created_at'] > '2024-03-31') &
    (pdf_hedb['created_at'] <= '2024-06-30')
])
q3hedb = len(pdf_hedb[
    (pdf_hedb['created_at'] > '2024-06-30') &
    (pdf_hedb['created_at'] <= '2024-09-30')
])
q4hedb = len(pdf_hedb[
    (pdf_hedb['created_at'] > '2024-09-30') &
    (pdf_hedb['created_at'] <= '2024-12-31')
])

q1gpdb = len(pdf_gpdb[
    (pdf_gpdb['created_at'] >= '2024-01-01') &
    (pdf_gpdb['created_at'] <= '2024-03-31')
])
q2gpdb = len(pdf_gpdb[
    (pdf_gpdb['created_at'] > '2024-03-31') &
    (pdf_gpdb['created_at'] <= '2024-06-30')
])
q3gpdb = len(pdf_gpdb[
    (pdf_gpdb['created_at'] > '2024-06-30') &
    (pdf_gpdb['created_at'] <= '2024-09-30')
])
q4gpdb = len(pdf_gpdb[
    (pdf_gpdb['created_at'] > '2024-09-30') &
    (pdf_gpdb['created_at'] <= '2024-12-31')
])

playbacks_result = f"""
Playbacks:
Q1:
HEDB: {q1hedb}
GPDB: {q1gpdb}
Total: {q1hedb + q1gpdb}

Q2:
HEDB: {q2hedb}
GPDB: {q2gpdb}
Total: {q2hedb + q2gpdb}

Q3:
HEDB: {q3hedb}
GPDB: {q3gpdb}
Total: {q3hedb + q3gpdb}

Q4:
HEDB: {q4hedb}
GPDB: {q4gpdb}
Total: {q4hedb + q4gpdb}
"""

result = recordings_result + playbacks_result


pprint(result)


"""
Recordings:
Q1:
HEDB: 591776
GPDB: 567
Total: 592343

Q2:
HEDB: 275810
GPDB: 651
Total: 276461

Q3:
HEDB: 617644
GPDB: 2396
Total: 620040

Q4:
HEDB: 269643
GPDB: 778
Total: 270421



Playbacks:
Q1:
HEDB: 713291
GPDB: 774
Total: 714065

Q2:
HEDB: 597936
GPDB: 470
Total: 598406

Q3:
HEDB: 615228
GPDB: 0
Total: 615228

Q4:
HEDB: 309907
GPDB: 0
Total: 309907
"""
