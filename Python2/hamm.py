from session4_exc import DNASequence
import argparse

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('--booleanExample', action="store_true", default=False)
	parser.add_argument('--file', type=str)
	parser.add_argument('remainingArguments', type=str, nargs='*')
	return parser.parse_args()

args = parse_args()
# print "arguments: file:", args.file
# print "arguments: booleanExample:", args.booleanExample
# print "arguments: remainingArguments:", args.remainingArguments

# seq_objects=[]
# with open('rosalind_hamm.txt') as f:
# 	for each in f:
# 		each=each.strip()
# 		seq_objects.append(DNASequence(each))



seq_objects=[]
#with open(args.file) as f: # use this when run script in command line with arguments
with open('rosalind_hamm.txt') as f: 
	for each in f:
		each=each.strip()
		seq_objects.append(DNASequence(each))  #append sequence object instead of sequence itself
seq1=seq_objects[0]
seq2=seq_objects[1]
print seq1.Hamm2(seq2)

