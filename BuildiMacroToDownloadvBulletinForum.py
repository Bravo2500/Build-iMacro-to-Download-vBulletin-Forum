#!/usr/bin/env python

"""
Copyright © 2017 by Stephen Genusa

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice,
this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
this list of conditions and the following disclaimer in the documentation
and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.
"""

import argparse
import re

import requests

class iMacroVBulletinBuilder:
    
    
    def __init__(self, url, begin_thread, end_thread, begin_member, end_member, outputlocation):
        self.iMacroFilename = 'imacro.txt'
        self.url = url        
        self.begin_thread = begin_thread
        self.end_thread = end_thread
        self.begin_member = begin_member
        self.end_member = end_member
        self.outputlocation = outputlocation.replace(" ", "<SP>")
    

    def writeiMacro(self):
        with open(self.iMacroFilename, 'w') as textfile:
            textfile.write("VERSION BUILD=11.5.498.2403\n")
            textfile.write("TAB T=1\n")
            
            if self.end_thread > 0:
                textfile.write("'\n")
                textfile.write("' Forum Thread Updates\n")
                textfile.write("'\n")
                for x in range(self.end_thread, self.begin_thread, -1):
                    textfile.write("URL GOTO=" + self.url + "/showthread.php?" + str(x) + "&pp=40\n")
                    textfile.write("WAIT SECONDS=1\n")
                    textfile.write("SAVEAS TYPE=MHT FOLDER=" + self.outputlocation + " FILE=Thread_" + str(x) + ".mht\n")
    
            if self.end_member > 0:
                textfile.write("'\n")
                textfile.write("' Member Profile Updates\n")
                textfile.write("'\n")
                for x in range(self.begin_member, self.end_member + 1):
                    textfile.write("URL GOTO=" + self.url + "/member.php?" + str(x) + "\n")
                    textfile.write("WAIT SECONDS=1\n")
                    textfile.write("SAVEAS TYPE=MHT FOLDER=" + self.outputlocation + " FILE=Member_" + str(x) + ".mht\n")
        print "iMacro file written", self.iMacroFilename 


def main():
    # Parse commandline arguments
    parser = argparse.ArgumentParser(description='Build an iMacro file to download vBulletin forum threads and member info')
    parser.add_argument("-u", "--url", dest="url", default = "", help="vBulletin URL", required=True)
    parser.add_argument("-o", "--output", dest="outputlocation", default = "", help="Output location", required=True)
    parser.add_argument("-a", "--autoparse", dest="autoparse", action="store_true", default = False,
                      help="Attempt to get last thread number and last member number from url")
    parser.add_argument("-t", "--beginthread", dest="beginthread", default = 1, type=int,
                      help="Beginning thread number")
    parser.add_argument("-e", "--endthread", dest="endthread", default = 0, type=int,
                      help="Ending thread number")
    parser.add_argument("-m", "--beginmember", dest="beginmember", default = 1, type=int,
                      help="Beginning member number")
    parser.add_argument("-l", "--endmember", dest="endmember", default = 0, type=int,
                      help="Ending member number")
    args = parser.parse_args()
    
    print "URL of vBulletin forum is", args.url
 
    # Check if we are attempting to parse last thread and end members from live forum
    if args.autoparse:
        "Print attempting to get end thread and last member number"
        r = requests.get(args.url)
        search_html = r.text.replace("\n", "").replace("\r", "").replace("\t", "")
    
        # Get last thread #
        match = re.search(r"Threads<\/dt><dd>(\d{1,3}(?:[,]\d{3}))<\/dd", search_html)
        if match:
            args.endthread = int(match.group(1).replace(",", ""))
            print "End thread is", args.endthread
        
        # Get last thread #
        match = re.search(r"newest member.*\?(\d{1,6})-", search_html)
        if match:
            args.endmember = int(match.group(1))
            print "Last member number is", args.endmember
    
    # Build output iMacro file
    builder = iMacroVBulletinBuilder(args.url, args.beginthread, args.endthread, args.beginmember, args.endmember, args.outputlocation)
    builder.writeiMacro()

if __name__ == "__main__":
    main()