#!/usr/python

import os
import datetime
import sys
import boto
import gzip
from boto.s3.key import Key
from boto.s3.connection import S3Connection

conn=S3Connection('AKIAJULDYSFQQWUZHVJA','GJhOCgkQ5oTePb5W4F8KXtnzhwZGhushvaLT7R4I')
bucket=conn.get_bucket('3kricegenome');

def look_up(bucket,filename,output):
	nonexistent=bucket.lookup(filename)
	if nonexistent is None:
		print "No such file in bucket."
	else:
		print nonexistent.key
		file_key = bucket.get_key(filename)
		file_key.get_contents_to_filename(output)


def decompress(gzfile,output):
	f = gzip.open(gzfile,'rb')
	o = open(output,'wb')
	o.write(f.read())
	f.close()
	o.close()
		

if __name__ == '__main__':
#download(bucket,'Nipponbare/B001.realigned.bam')
	reference=sys.argv[1]
	variety=sys.argv[2]
	output=sys.argv[3]
	finput=reference+"/"+variety+".snp.vcf.gz"
	foutput="temp.vcf.gz"

	look_up(bucket,finput, foutput)
	#decompress(foutput,output)
	with gzip.open(foutput,'rb') as f_in, gzip.open(output,'wb') as f_out:
		f_out.write(f_in.read())
