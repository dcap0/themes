from pathlib import Path
import json

out = {}

j = Path("/home/ddmac/repo/themes/smokey-dawn/smokey-dawn-palette.txt").open()

for line in j.readlines():
    
    out[line[8:].strip().upper().replace(" ","_")] = line[0:7]

outfile = open("./colors.json","w+")

outfile.write(json.dumps(out))
