import csv

def get_visitors():
  filestream = open( 'dordt/purl_visits.csv', 'r' )
  reader = csv.reader( filestream )
  headers = next( reader )
  efcid_index = headers.index( 'EFCID' )
  visitors = set()

  for row in reader:
    visitors.add( row[efcid_index] )

  return visitors