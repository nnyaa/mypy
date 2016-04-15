import tushare as ts
import threading
from time import sleep,ctime

aa=ts.get_stock_basics()
code=aa.index

T0='09:00:00'             # split 80min a day
T1='10:50:00'
T2='13:40:00'
T3='15:00:00'
GroupNum=4               # how many threading use 





def art_hao(O1,O2,O3,C1,C2,C3,V1,V2,V3):  
	# main juget:  O1,O2,O3; C1,C2,C3; V1,V2,V3;
	if O1<O2 and O2<O3 and O1<C1 and O2<C2 and O3<C3 and V1<V3 :
		return 1
	else:
		return 0











def group_list(l,block):   #Founation of split code to small group
	size=len(l)
	return[l[i:i+block] for i in range(0,size,block)]


def get_D_5min(CodeNo):
	t1=ts.get_hist_data(CodeNo,ktype='5')
	t5=t1.head(48)

	vol=0
	#for i in range(33,48):
	#	print t5.index[i],t5.open[i],t5.close[i],t5.volume[i]
	#	vol=vol+t5.volume[i]
	#print "--------------------------"
	#print t5.index[0],t5.index[15]
	#print vol,t5.close[0],t5.close[15],t5.p_change[0]

	vol1=0
	vol2=0
	vol3=0

	for i in range(len(t5)):
		sstr=t5.index[i].split(" ")
		TimeGe=sstr[1]
		if (TimeGe>=T0) and (TimeGe<=T1):
			vol1=vol1+t5.volume[i]
			open1=t5.open[i]
			close1=open2

		if (TimeGe>T1) and  (TimeGe<=T2):
			vol2=vol2+t5.volume[i]
			open2=t5.open[i]
			close2=open3

		if (TimeGe>T2) and (TimeGe<=T3):
			vol3=vol3+t5.volume[i]
			close3=t5.close[0]
                	open3=t5.open[i]


	#print open1,close1,vol1
	#print open2,close2,vol2
	#print open3,close3,vol3
	#print CodeNo

	if art_hao(open1,open2,open3,close1,close2,close3,vol1,vol2,vol3) ==1 :
		print "--------------------------",CodeNo
#	if vol1<vol2 and vol2<vol3:
#		print "-------------------------vol ok!"
#	if close1<close2  and close2<close3:
#		print CodeNo,"________________close OK!"

	return


ThreadCode=group_list(code,GroupNum)


def Do_Th(CodeNo):
	threads=[]
	th_num=range(len(CodeNo))

	for item in CodeNo:
		t=threading.Thread(target=get_D_5min,args=(item,))
        	threads.append(t) 


	for i in th_num:
		threads[i].start()	  
	for i in th_num:
		threads[i].join()

  	#sleep(5)  

for i  in range(len(ThreadCode)):
	Do_Th(ThreadCode[i]) 
	print "____________________________________________",i,'end:%s'%ctime()



#Do_Th(ThreadCode[0])
#Do_Th(ThreadCode[2]) 


#for t in threads:
	#t.setDaemon(True)
	#t.start()


#	for i in item
#		#get_D_5min(item)
#		print item
#		print "++++++++++++++++"

