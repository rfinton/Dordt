import csv
import glob

def get_openers():
  raw_data = "./report-2020-24-1--00-00-53/data.csv"
  openers = {}
  openers_3 = set()

  fs = open( raw_data, 'r' )
  reader = csv.reader( fs )
  headers = next( reader )
  outbound_index = headers.index( 'Outbound' )
  contact_id_index = headers.index( 'contact_id' )

  for row in reader:
    contact_id = row[contact_id_index]
    entry = row[outbound_index]

    if contact_id not in openers:
      openers[contact_id] = { entry }
    else:
      openers[contact_id].add( entry )

  for key, val in openers.items():
    if len( val ) > 2:
      openers_3.add( key )
  
  return openers_3