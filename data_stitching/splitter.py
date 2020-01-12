import csv
rf = open('unified/lcd-stations.txt')     #input file handle
wf = open('lcd-stations.csv','w', newline='') #output file handle
writer = csv.writer(wf)
for row in rf.readlines():
    writer.writerow(row.split())
rf.close()  # close input file handle
wf.close()  # close output file handle