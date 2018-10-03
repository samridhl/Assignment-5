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
                    

data = urllib.urlopen("http://rest.ensembl.org/overlap/id/"+ gene_id_matches[0] +".json?feature=variation")
json_obj = json.load(data)

for i in json_obj:
    id_names = i['id']
    consequence_type = i['consequence_type']
    consequence_new = consequence_type.replace("_"," ")
    clinical_significance = i['clinical_significance']
    if clinical_significance:
        print "varaint" + id_names + "is a" + consequence_new  + "," + " and is clinically " + clinical_significance[0].upper()
    else:
        print "varaint" + id_names + "is a" + consequence_new  +  ","
   
    





