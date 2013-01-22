#!/usr/bin/env python

from remotezip import RemoteZip

url = ""
remoteZip = RemoteZip(url)
remoteZip.getTableOfContents()

print remoteZip.tableOfContents

# sample extraction
uncompressedFile = remoteZip.extractFile(remoteZip.tableOfContents[0]['filename'])
