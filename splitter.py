#!/usr/bin/env python

"""
Google Camera Motion Photo splitter.
Google Camera generates a container which encapsulates picture and video. The first part
is a JPEG, ending with the EOI marker (0xFF 0xD9). Second part is the video.

Algorithm:
Count the bytes for each offset and write the files.
JPEG: byte zero to JPEG EOI
MP4: JPEG's EOI + 1 to end of file (size of the file)

"""

import sys
from os import path
from mmap import mmap


# beginning of MP4: EOI + null bytes + 'ftypmp4'
eop = b"\xFF\xD9\x00\x00\x00\x18\x66\x74\x79\x70\x6D\x70\x34"


def write_files(fname,jpeg,mp4):
  """
  Creates videos and files
  """
  sname = fname.replace('.jpg','')
  picture = sname + "_new" + ".jpg"
  video = sname + "_new" +  ".mp4"


  with open(picture,'w+b') as f:
      f.write(jpeg)

  if path.exists(video):
    sys.exit('Error: file %s exists' % video )
  else:
    with open(video,'w+b') as f:
      f.write(mp4)



def spliter(fname):
  """
  Splits video and picture
  """
  with open(fname,'r+b') as f:
    mm = mmap(f.fileno(),0)
    file_size = mm.size()
    # size of the file - len of the magic = processed file
    magic = mm.find(eop)
    magic_lim = file_size - len(eop)
    #Do not process if magic is not found, and if found at the end
    if magic == -1 or magic == magic_lim:
      sys.exit("Error: file %s has no motion photo" % fname)
    else:
      jpeg_offset = magic + 2 # EOI
      mpeg_start = jpeg_offset + 1
      mpeg_end = file_size

      #JPEG  here
      mm.seek(0)
      jpeg = mm.read(jpeg_offset)

      #MP4 here
      #Start in the first byte of the MP4 container
      mm.seek(mpeg_start - 1)
      mp4 = mm.read(mpeg_end)
      write_files(fname,jpeg,mp4)


if len(sys.argv) < 2:
  sys.exit('Usage:: %s <file>' % sys.argv[0])

fname = sys.argv[1]
spliter(fname)
