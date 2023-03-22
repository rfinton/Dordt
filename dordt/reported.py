import csv
import glob

def get_reported():
  csv_files = glob.glob( 'dordt/inq*' )
  reported = set()

  for csv_file in csv_files:
    inq_file = open( csv_file, 'r' )
    reader = csv.reader( inq_file )

    for row in reader:
      if row[1] != "EFCID":
        reported.add( row[1] )

    inq_file.close()

  return reported