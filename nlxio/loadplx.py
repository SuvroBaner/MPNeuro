# -*- coding: utf-8 -*-
"""
Created on Tue Mar 04 18:02:30 2014

@author: palmiteradmin
"""

import neo
import csv

def loadspiketimes(filename):
    """
    This should be run from the python IDE in a directory with two files:
    filename.plx        A Plexon file containing clustered units
    filename.csv        A CSV that contains channel number and unit number
       
    """
    unitinfo = []
    
    # open the csv
    csvfile =  open(filename+'.csv')
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        unitinfo.append(map(int, row)) # unit info is list of [electrode, unit] pairs
    
    # open the plexon file
    reader = neo.io.PlexonIO(filename = filename+'.plx')
    seg = reader.read_segment()
    
    # extract the spike times for the desired units
    spiketrains = []
    electrodecursor = 0
#    prevelectrode = unitinfo[0][0]
    for index, (electrode, unitnum) in enumerate(unitinfo): # if I understand for loops, this will go through each row, and assign electrode to 1st item in row, and unitnum to 2nd item
        if  electrode > unitinfo[index-1][0]:
            electrodecursor = 4*(index)
 #           prevelectrode = electrode # move electrode cursor
        spiketrains.append(seg.spiketrains[electrodecursor +unitnum -1])
        
    
    return spiketrains, unitinfo
    