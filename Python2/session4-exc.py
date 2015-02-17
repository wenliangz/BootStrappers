#!/usr/bin/env python
from collections import defaultdict

class DNASequence(object):
	# add default attributes to classe and keyword arguments
	def __init__(self,sequence, name = None):
		self.sequence = sequence
		self.name = name

	# def __repr__(self):
	# 	if self.name is None:
	# 		return "Unknown " + str(self.gc_content())
	# 	return self.name + " " + str(self.gc_content())

	#problem 1: Base count
	def countbase(self):
		# define a default dict to avoid keywork error in the case that some bases may not be existingin the sequence
		base_count=defaultdict(int)
		for letter in self.sequence:
			base_count[letter]+=1
		return base_count

	#problem 2: RNA
	def transcribe(self):
 		new_rna=self.sequence.replace('T','U')
 		return new_rna

 	#Problem 3: REVC
 	def reverseComplement(self):
 		reverse=self.sequence[::-1]
		compliment={'A':'T','C':'G','G':'C','T':'A'}
		letters=list(reverse)
		RC=[compliment[base] for base in letters]
		RCDNA=''.join(RC)
		return RCDNA

	#Problem 4: GC content	
	def gc_content(self):
		counts=self.countbase()
		gc=counts['G']+counts['C']
		gc_percent=float(gc)/len(self.sequence)
		return gc_percent
	
# class for parsing FASTA file

class FASTAFile(object):
	def __init__(self,path):
		self.path=path

	def seuqence(self):
		found_sequences=[]
		with open(self.path,'r') as input:
			sequence=''
			for i,line in enumerate(input):
				if i==0:
					name=line.rstrip('\n').lstrip('>')
				else:
					if line.startwith('>'):
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

#Define a new class inherited from DNASequence class above
class Gene(DNASequence):
	def Hamm(self,new_sequence):
		seq1_dict={}
		seq2_dict={}
		for position,base in enumerate(self.sequence):
			seq1_dict[position]=base
		for position,base in enumerate(new_sequence):
			seq2_dict[position]=base
		seq1_set=set(seq1_dict.iteritems())
		seq2_set=set(seq2_dict.iteritems())
		Hamm=seq1_set-seq2_set
		return len(Hamm)

class RNAsequence(object):
	def __init__(self, RNAseq):
		self.RNAseq=RNAseq
		self.codon_dict=defaultdict(str)
		with open("codon_table.txt") as f:
			for each in f:
				key=each.split()[0]
				value=each.split()[1]
				self.codon_dict[key]=value
	def translate(self):
		protein_list=[]
		codon=[n for n in xrange(0,len(self.RNAseq),3)]
		for i in codon:
			protein_list.append(self.codon_dict[self.RNAseq[i:i+3]])
		protein=''.join(protein_list)
		protein=protein.replace('STOP','')
		return protein

seq="AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
myRNAsequence=RNAsequence(seq)
print myRNAsequence.translate()



# seq=[]
# with open('rosalind_hamm.txt') as f:
# 	for each in f:
# 		each=each.strip()
# 		seq.append(each)

# seq1=seq[0]
# seq2=seq[1]
# print Gene(seq1).Hamm(seq2)

# DNA=open('rosalind_dna.txt')
# seq=DNA.readlines()[0].strip()
# my_sequence=DNASequence(seq)
# print my_sequence.gc_content()
# my_count=my_sequence.countbase()
# my_RNA=my_sequence.transcribe()
# my_REVC=my_sequence.reverseComplement()
# #print my_REVC


# mylist = [DNASequence("ATCCCG", "sequence 1"), DNASequence("AAAAATTTT", "sequence 2")]
# for seq in mylist:
# 	print seq




