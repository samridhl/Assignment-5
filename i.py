#!/usr/bin/python

import re
import sys
import fileinput
import json
import urllib 

user_gene_name = raw_input('Enter the gene name')


for line in fileinput.input(['/data/Homo_sapiens.GRCh37.75.gtf']):
    if re.match(r'.*\t.*\tgene\t', line):
        text_in_column = re.split('\t',line)
        if len(text_in_column)>3:
            if text_in_column[2] == "gene": 
                gene_name_matches = re.findall('gene_name \"(.*?)\";', line)
                
                if user_gene_name == gene_name_matches[0]:
                    gene_id_matches = re.findall('gene_id \"(.*?)\";', line)
                    

data = urllib.urlopen("http://rest.ensembl.org/overlap/id/ENSG00000130203.json?feature=variation")
for i in data:
    i ['id']
    i ['consequence_type']
    i ['clinical significance']
    print "varaiant" [id] "is a"[consequnece_type] 
    





