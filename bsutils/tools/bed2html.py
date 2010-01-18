#!/usr/bin/env python

# bed2html 
# Song Qiang <qiang.song@usc.edu> 2010
# this program convert 6-column BED file to html file
# it is used to display DMR files and / or hypo-methylated regions 
# in html format

import sys, string


#  html header and footer
html_header = """
<html>
<head>
<title> </title>
<link rel="stylesheet" href="css/table.css" type="text/css">
</head>
<body>
<table class="dmrtable" cellspacing="0">
"""
html_footer = """
</table>
</body>
</html>
"""

odd_line_template = """\t<tr class="odd"><td> %(INDEX)d </td><td><a href="http://genome.ucsc.edu/cgi-bin/hgTracks?position=%(CHROM)s%%3A%(START)d-%(END)d">%(CHROM)s:%(START)d-%(END)d</a></td><td>%(SCORE)s</td><td>%(CPG_NUM)s</td></tr>\n"""

even_line_template = """\t<tr><td> %(INDEX)d </td><td><a href="http://genome.ucsc.edu/cgi-bin/hgTracks?position=%(CHROM)s%%3A%(START)d-%(END)d">%(CHROM)s:%(START)d-%(END)d</a></td><td>%(SCORE)s</td><td>%(CPG_NUM)s</td></tr>\n"""

output_file = open(sys.argv[2], "w")
output_file.write(html_header)

index = 1

for line in open(sys.argv[1]):
	(chrom, start, end, readName, score, strand) = line.split()
	start = int(start)
	end = int(end)
	width = end - start
	extension = int(width / (1 - 0.618) * 0.618 / 2)
	start -= extension
	end += extension
	score = str( float(score) / 1000)
	cpg_num = readName.split(":")[1]
	if index % 2 == 1:
		row = odd_line_template % {"INDEX" : index, \
								   "CHROM" : chrom, \
								   "START" : start, \
									"END" : end, \
								   "SCORE" : score, \
								   "CPG_NUM" : cpg_num} 	
	else:
		row = even_line_template % {"INDEX" : index, \
								   "CHROM" : chrom, \
								   "START" : start, \
								   "END" : end, \
								   "SCORE" : score, \
								   "CPG_NUM" : cpg_num} 	
	output_file.write(row)
	index += 1

output_file.write(html_footer)
output_file.close()
	