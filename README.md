# Build iMacro to Download vBulletin Forum
I wanted to download specific information from a vBulletin forum. I found Scrapy more work than I cared for and I couldn't go back and target specific pages without more trouble. I found that the typical web site mirror/scraping program chokes on the number of unnecessary links that vBulletin can generate.

This program targets the two things I cared about downloading: threads and member info pages. You can also go back and easily target specific threads and new members.

Note: While I avoid Internet Explorer sort of like the plague, I found that it was the only browser that would give me a good MHT file.

Use:

- Generate the iMacro file
- Login to the vBulletin forum using IE, preferably in a VM you can do a rollback on after you are done downloading and moving the data out of the VM
- Load iMacro by clicking on the icon in IE
- Click Record on iMacro
- Click Stop Recording
- Click Edit Macro
- Paste in the generated iMacro file
- Click Play
- Wait for the process to complete
- Save the MHT files off to storage

----------
- Written using Python 2.7
- The regex's may have to be tweaked for different forum versions or configurations

----------

Copyright © 2017 Stephen Genusa

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.