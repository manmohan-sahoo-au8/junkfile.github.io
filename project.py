# junk file organiser

# importinf modules from python library

import os
import math
import datetime
import shutil
# for command line
import sys
import argparse

CURRENT_DIRECTORY=r"E:\folder"

#organize by extension:

def organizeByExtension(path):
  files=os.listdir(path)
  all_files=[]

#split file extension
  for i in files:
    _, split = os.path.splitext(i)
    if split not in all_files:
      all_files.append(split)

# creating the separate folders 
  for extension in all_files:
    if extension:
      os.mkdir(os.path.join(path,extension))

#moving all the files to their specific folder
  for i in files:
    _, extension = os.path.splitext(i)
    old_path=os.path.join(path,i)
    new_path=os.path.join(path,extension,i)
    os.rename(old_path, new_path)

#organize by size

def organizeBySize(path):
  dirs=os.listdir(path)
  dir_size1={}

  for j in dirs:
    dir_size1[j]=os.stat(os.path.join(path,j)).st_size

  sorted_dir=sorted(dir_size1.items(),key=lambda c:c[1])
  dir_size0 = []
  size_types = []

  for j in sorted_dir:
    a1 = (os.stat(os.path.join(path,j[0])).st_size)
    a2 = convert_size(a1)
    a3 = str(a2).split("_")

    if a3 == [] or a3 == ["0B"]:
      pass
    else:
      dir_size0.append(a3)
  types=[]
  sub = "."
  for j in sorted_dir:
    if sub in j[0]:
      b1=j[0][::-1].find(".")
      b2=j[0][-b1:]
      if b2 not in types:
        types.append(b2)

#creating folder
  for j in dir_size0:
    if j[1] not in size_types:
      size_types.append(j[1])
  for j in size_types:
    for k in dir_size0:
      if k[1] == j and int(k[0]) < 50 :
        if not os.path.exists(os.path.join(path,"Less Than 50" + k[1])):
          os.mkdir(os.path.join(path,"Less Than 50"+k[1]))
      elif k[1] == j and int(k[0]) > 50:
        if not os.path.exists(os.path.join(path,"Grater Than 100" + k[1])):
          os.mkdir(os.path.join(path,"Grater Than 100" + k[1]))

#moving files to folder
  newFiles = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path,file))]
  x = [x for x in newFiles if checkFIle(x) == False]
  for j in x:
    new_size = convert_size(os.stat(os.path.join(path,j)).st_size)
    new_size = new_size.split("_")
    if int(new_size[0]) < 50 :
      shutil.move(os.path.join(path,j),os.path.join(path,"Less Than 50" + new_size[1]))
    else:
      shutil.move(os.path.join(path,j),os.path.join(path,"Grater Than 100" + new_size[1]))

# converting bytes to readable size
def convert_size(size_bytes):
  if size_bytes == 0:
    return "0B"

  size_name=("B","KB","MB","GB","TB","PB","EB","ZB","YB")
  i=int(math.floor(math.log(size_bytes,1024)))
  p=math.pow(1024,i)
  s=round(size_bytes/p,2)
  return "%s_%s" % (round(s),size_name[i])

def checkFIle(fileName):
  d = os.path.basename(__file__)
  if fileName == d:
    return True
  return False

#organize by date
def organizeByDate(path):
  files = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path,file))]
  m = [m for m in files if checkFIle(m) == False]

  for i in m:
    time=(os.stat(os.path.join(path,i)).st_atime)
    timestamp = datetime.datetime.fromtimestamp(time).strftime("%Y-%m-%d")
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    t1 = datetime.date(int(timestamp[:4]),int(timestamp[5:7]),int(timestamp[8:]))
    d1 = datetime.date(int(current_date[:4]),int(current_date[5:7]),int(current_date[8:]))
    d2 = str(d1-t1)
    d3 = d2.split(",")[0]
    if d3[-4:] == "days" :
      if int(d2[:-14] < 10):
        if not os.path.exists(os.path.join(path,"Less Than 10 Days")):
          os.mkdir(os.path.join(path,"Less than 10 Days"))
        shutil.move(os.path.join(path,i),os.path.join(path,"Less Than 10 Days"))
      elif int(d2[:-14]) < 20:
        if not os.path.exsits(os.path.join(path,"Less Than 20 Days")):
          os.mkdir(os.path.join(path,"Less Than 20 Days"))
        shutil.move(os.path.join(path,i),os.path.join(path,"Less Than 20 Days"))
      else:
        if not os.path.exists(os.path.join(path,"More Than 20 Days")):
          os.mkdir(os.path.join(path,"More Than 20 Days"))
        shutil.move(os.path.join(path,i),os.path.join(path,"More Than 20 Days"))
    else:
      if not os.path.exists(os.path.join(path,"Less Than 10 Days")):
        os.mkdir(os.path.join(path,"Less Than 10 Days"))
      shutil.move(os.path.join(path,i),os.path.join(path,"less Than 10 Days"))

#define the function for command line parsing
def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("--path",default=".",help="Which folder to organize ?")
  parser.add_argument("--o",default="extension",help="organize by?",choices=["extension","size","date"])

  args=parser.parse_args()
  path=args.path
  organize_by=args.o

  if organize_by == "extension":
    organizeByExtension(path)
  elif organize_by == "size":
    organizeBySize(path)
  elif organize_by == "date":
    organizeByDate(path)
  else:
    print("wrong input")


if __name__ == "__main__":
    main()
















