# class for parsing FASTA file
from session4_exc import DNASequence

class FASTAFile(object):
	def __init__(self,path):
		self.path=path
	def sequence1(self):
		found_sequences=[]
		with open(self.path,'r') as input:
			sequence=''
			for i,line in enumerate(input):
				if i==0:
					name=line.rstrip('\n').lstrip('>')
				else:
					if line.startswith('>'):
						new_sequence_object=DNASequence(sequence,name)
						found_sequences.append(new_sequence_object)
						sequence=''
						name=line.rstrip('\n').lstrip('>')
					else:
						sequence+=line.rstrip('\n')
			else:
				new_sequence_object=DNASequence(sequence,name)
				found_sequences.append(new_sequence_object)
		return found_sequences
	
	def sequence2(self):
		found_sequences_objects=[]
		sequence=""
		with open(self.path,'r') as input:
			for line in input:
			    #if your line starts with a > then it is the name of the following sequence
			    if line.startswith('>'):
			        name = line[1:-1]
			        sequence_object=DNASequence(sequence,name)
			        if sequence!="":
			        	found_sequences_objects.append(sequence_object)
			        continue #go back to loop, so this means skips to the next line.
			    #This code is only executed if it is a sequence of bases and not a name.
			    sequence+=line.strip()
			else: # this line run only after for loop ends without break
				sequence_object=DNASequence(sequence,name)
				found_sequences_objects.append(sequence_object)
		return found_sequences_objects


s1=FASTAFile("rosalind_gc.txt").sequence1()
s2=FASTAFile("rosalind_gc.txt").sequence2()
print len(s1),s1
print len(s2),s2
print s1[0].sequence
print s1[0].sequence