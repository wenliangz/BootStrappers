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

	def Hamm(self,new_sequence): #new_sequence is a sequence input
		#print type(new_sequence)
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
	
	def Hamm2(self,new_sequence): #new_sequence need to be an sequence object input
		#print type(new_sequence)
		seq1_dict={}
		seq2_dict={}
		for position,base in enumerate(self.sequence):
			seq1_dict[position]=base
		for position,base in enumerate(new_sequence.sequence):
			seq2_dict[position]=base
		seq1_set=set(seq1_dict.iteritems())
		seq2_set=set(seq2_dict.iteritems())
		Hamm=seq1_set-seq2_set
		return len(Hamm)


	
#Define a new classs for RNA sequence input
class RNAsequence(object):
	def __init__(self, RNAseq):
		self.RNAseq=RNAseq
		self.codon_dict=defaultdict(str)
		with open("codon_table.txt") as f:
			for each in f:
				toks = each.split()
				self.codon_dict[toks[0]] = toks[1]
	def translate(self):
		codon_list=[]
		codon=[n for n in xrange(0,len(self.RNAseq),3)]
		for i in codon:
			if self.codon_dict[self.RNAseq[i:i+3]]=="STOP":
				break
			codon_list.append(self.codon_dict[self.RNAseq[i:i+3]])
		protein=''.join(codon_list)
		#protein=protein.replace('STOP','')
		return protein

class output:
	@staticmethod
	def print_translate():
		seq="AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
		myRNAsequence=RNAsequence(seq) #define a sequence object(or instance)
		print myRNAsequence.translate() #sequence object can then use method or variable by dot notation syntax
	@staticmethod	
	def print_Hamm():
		seq=[]
		with open('rosalind_hamm.txt') as f:
			for each in f:
				each=each.strip()
				seq.append(each)  #append sequence
		seq1=seq[0]
		seq2=seq[1]
		print DNASequence(seq1).Hamm(seq2)
	@staticmethod
	def print_Hamm2():
		seq_objects=[]
		with open('rosalind_hamm.txt') as f:
			for each in f:
				each=each.strip()
				seq_objects.append(DNASequence(each))  #append sequence object instead of sequence itself
		seq1=seq_objects[0]
		seq2=seq_objects[1]
		print seq1.Hamm2(seq2)

if __name__ == '__main__':  # Run the following code only when the code is runing as a main program, but not when it is called by other script. 
	DNA=open('rosalind_dna.txt')
	seq=DNA.readlines()[0].strip()
	my_sequence=DNASequence(seq)
	print my_sequence.gc_content()
	print my_sequence.countbase()
	print my_sequence.transcribe()
	print my_sequence.reverseComplement()

    #output.print_translate()
    #output.print_Hamm()
    #output.print_Hamm2()


# my_count=my_sequence.countbase()
# my_RNA=my_sequence.transcribe()
# my_REVC=my_sequence.reverseComplement()
# #print my_REVC


# mylist = [DNASequence("ATCCCG", "sequence 1"), DNASequence("AAAAATTTT", "sequence 2")]
# for seq in mylist:
# 	print seq