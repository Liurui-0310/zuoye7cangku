#!/usr/bin/env python3

def calculate_gc_content(dna_sequence):
   """Calculate the GC content of a DNA sequence."""
   # Convert to uppercase to handle both upper and lower case letters
   dna = dna_sequence.upper()
 
   # Count G and C nucleotides
   g_count = dna.count('G')
   c_count = dna.count('C')
 
   # Calculate total valid nucleotides (removing any non-ATGC characters)
   valid_nucleotides = sum(dna.count(nuc) for nuc in 'ATGC')
 
   # Calculate GC content as percentage
   if valid_nucleotides > 0:
       gc_content = (g_count + c_count) / valid_nucleotides * 100
   else:
       gc_content = 0
 
   return gc_content

if __name__ == "__main__":
   # Example usage
   dna_seq = input("Enter a DNA sequence: ")
   gc_percent = calculate_gc_content(dna_seq)
   print(f"The GC content is: {gc_percent:.2f}%")

