#!/usr/bin/env python

from remotezip import RemoteZip

url = "http://ak.englishtown.com/Juno/FierceRabbit/FullContentPackages/Revision1/0A/1/courseware-full-0A-381-1.zip"
remoteZip = RemoteZip(url)
remoteZip.getTableOfContents()

print remoteZip.tableOfContents

# sample extraction
uncompressedFile = remoteZip.extractFile(remoteZip.tableOfContents[0]['filename'])
