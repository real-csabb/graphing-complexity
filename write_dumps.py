import sys
import json

def write_dumps(data):
  # Dump runtime into a file
  file_name = f"{sys.argv[2]}_results.txt"
  f = open(f"{file_name}", "w")
  f.write(json.dumps(data))
  f.close()

  return file_name