#Part 1
import pandas

InFile=open("Lecture11.fasta","r") #Open fasta file as read-only

sequenceLength=[] #Set up variables to accept/store sequence data as it is calculated
percentGC=[]

for line in InFile: #Loop through each line in fasta file
    if '>' in line: #Check line for >, if present, skip to next line
        continue
    else:
        seqLen=float(len(line)) #Calculate length of sequence
        nG=line.count("G") #Count individual G and C contents
        nC=line.count("C")
        percGC=float(((nG+nC)/seqLen)*100) #Calculate % GC
    
        sequenceLength.append(seqLen) #Append length of individual sequences to list
        percentGC.append(percGC) #Append %GC of individual sequences to list
