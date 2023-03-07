import re
import tempfile
import pypdf

fp = tempfile.TemporaryFile()
incidents = []

def extractincidents(data):
	#print("***Extraction Started***")
	fp.write(data)
	fp.seek(0)

	reader = pypdf.PdfReader(fp)
	page = len(reader.pages)

	for p in range(0, page):
		tl = []
		page_data = reader.pages[p].extract_text()
		line = ""
		dualline = 0
		for i in range(0, len(page_data)):
			if (page_data[i] == '\n'):
				
				if(line == 'Date / Time Incident Number Location Nature Incident ORI'):
					pass
				else:
					#print(line)
					s1 = ""
					ori = ""
					word_arr = line.split(" ")
					#print(word_arr[0])
					#print(word_arr[1])
					#print(word_arr[2])
					for i in range(3,len(word_arr)):
						if (word_arr[i] == "OK0140200" or word_arr[i] == "EMSSTAT" or word_arr[i] == "14005" or word_arr[i]=="14009"):
							dualline = 0
							break
						else:
							dualline = 1

					if dualline == 0:
						for i in range(3,len(word_arr)):
							if (word_arr[i] == "OK0140200" or word_arr[i] == "EMSSTAT" or word_arr[i] == "14005" or word_arr[i]=="14009"):
								#print(word_arr[i])
								ori = word_arr[i]

							else:
								s1 += word_arr[i] + " "

						pattern = r"\b(?:[A-Z][a-z]+|911 Call Nature Unknown|MVA With Injuries|MVA Non Injury|COP.*)\b"

						match = re.findall(pattern,s1)

						s2 = ""

						if len(match) == 0 and len(s1.strip()) == 0:
							s2 = "Nan"
							s1 = "Nan"
						elif len(match) == 0:
							s2 = "Nan"
						elif len(s1.strip()) == 0:
							s1 = "Nan"
						else:
							if match[0] == "911 Call Nature Unknown" or match[0] =="MVA With Injuries" or match[0] == "MVA Non Injury":
								s2 = match[0]
							else:
								s2 = s1.split(match[0],1)[1]

						#ntr = matchess[0]+ntr.strip()
								if s2.strip().startswith("/"):
									s2 = match[0] + s2.strip()
								else:
									s2 = match[0] + " " + s2.strip()


						#print(s2)
						#print('subtract this :')
						#print(s1,'--',s2)
						if s1 == "Nan":
							lock = "Nan"
						else:
							lock = s1.replace(s2,"")
						#print(lock)
						tl.append(word_arr[0]+" "+word_arr[1])
						tl.append(word_arr[2])
						tl.append(lock)
						tl.append(s2)
						tl.append(ori)
						incidents.append([tl])



					if dualline == 1:
						dualline = 0
						continue






				tl = []
				line = str()
			else:
				line += page_data[i]







	for i in range(0, len(incidents)):
		for j in range(0, len(incidents[i])):
			dt, icn, loc, nat, incori = [k for k in incidents[i][j]]
		#print(dt,"\t",icn,"\t",loc,"\t",nat,"\t",incori)
	#print('*'*150)


	return incidents
