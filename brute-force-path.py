import requests
import os
print"""
 __ )           |               _|                     		
 __ \   __| |   | __|  _ \       |    _ \   __| __|  _ \   //\	 ||   ||
 |   | |    |   | |    __/_____| __| (   | |   (     __/  //==\  ||   ||
____/ _|   \__,_|\__|\___|      _|  \___/ _|  \___|\___| //    \ ||__ ||__
				
				By Matisact										 
                                         """  

def ReadFile(file):
	in_file = open(file,"r")
	pwdf = in_file.read()
	in_file.close()
	listpbf = pwdf.split('\n')
	return listpbf

def Request(file,url):
	
	listpbf=ReadFile(file)

	for path in listpbf:
		res=requests.get(url+path)
		print url+path,res.status_code

def Request404(file,url):
	#web404
	#if find 404  in web return 404 else return 200
	listpbf=ReadFile(file)
	for path in listpbf:
		victim=requests.post(url+path)
		source=victim.content
		if '404' in source:
			print url+path,"page 404"
		if '404' not in source:
			print url+path,"page 200"


def CheckFile(file):
	#check file exist
	if os.path.isfile(file):
		return True
	else:
		return False

	

def WebPath():
	url=raw_input("Page brute force:")
	file=raw_input("List brute force: ")

	
	
	if CheckFile(file):
		Request(file,url)
	else:
		while CheckFile(file)==False:
				
				print "file not exist!please check path again!"
				file=raw_input("List brute force: ")	
		if CheckFile(file):
			Request(file,url)
def CtfTool():
	request={"robots.txt","sitemap.xml","index.php","flag.txt","flag.php","index.txt",
"index.php.txt","index.html.txt","index.old","index.php.old","index.html.old",
"index.sav","index.php.sav","index.html.sav",
"index.save","index.php.save","index.html.save",
"index.bk","index.php.bk","index.html.bk",
"index.rar","index.php.rar","index.html.rar",
"index.7z","index.php.7z","index.html.7z",
"index.backup","index.php.backup","index.html.backup",".git","index.php~"}

	url=raw_input("We take a url:")


	for i in request:
	  res=requests.get(url+i)
	  print i,res.status_code
def Web404():
	url=raw_input("Page brute force:")
	file=raw_input("List brute force: ")
	
	
	if CheckFile(file):
		Request404(file,url)
	else:
		while CheckFile(file)==False:
				
				print "file not exist!please check path again!"
				file=raw_input("List brute force: ")	
		if CheckFile(file):
			Request404(file,url)



print"""
		Select Function 
	====================================
	|1:-----CTF tools file--------------|
	|2:-----Burp-force web path---------|
	|3:-----Burp-force web error 404----|
	|4:-----Burp-force PassWord --------|
	=====================================
"""
func=raw_input("what do you want to do?:")
if func=='1':
	CtfTool()
if func=='2':
	WebPath()
if func=='3':
	Web404()
else:
	print "i don't think , it here!"

	
	
		



