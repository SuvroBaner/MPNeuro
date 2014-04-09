# -*- coding: utf-8 -*-
"""
Created on Mon Apr 07 16:58:09 2014

@author: palmiteradmin
"""

from __future__ import division
import csv
import numpy
import pdb

def parse_feedtimes_csv(filename):
    csvfile = open(filename)
    csvreader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC, delimiter = ' ')
    
    # initiliaze the feedtimes and watertimes counters
    feedtimes = []
    watertimes = []
    # go through all ines of csv, and append times to proper place
    for row in csvreader:
        if row[0] == 'f':
            feedtimes.append(int(row[1]))
            feedtimes.append(int(row[2]))
        elif row[0] == 'w':
            watertimes.append(int(row[1]))
            watertimes.append(int(row[2]))
    
    # convert the format
    feedtimes_sec = map(convert_mmss_to_sec, feedtimes)
    watertimes_sec = map(convert_mmss_to_sec, watertimes)
    
    # need to do this INELEGANT mapping and reshaping because I can't figure out python
    feedtimes_sec = numpy.reshape(feedtimes_sec, [numpy.size(feedtimes_sec) / 2, 2])
    watertimes_sec = numpy.reshape(watertimes_sec, [numpy.size(watertimes_sec) / 2, 2])
            
    return feedtimes_sec, watertimes_sec
    
    # this function converts a timestamp of for mmss to simply number of seconds
def convert_mmss_to_sec(mmss):
    return numpy.floor(mmss / 100) * 60 + mmss % 100