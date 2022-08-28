try:
	import os,sys,time,requests,bs4,json,pytube
	from pytube import YouTube
	from colorama import Fore,init,Back
	from bs4 import BeautifulSoup
except KeyboardInterrupt:
	sys.exeit("Module Belum Terisntall !!!")

BT = Fore.BLUE # Biru Tua
WH = Fore.WHITE # Putih Mati
R = Fore.RED # Merah
GR = Fore.GREEN # Hijau
BL = Fore.BLACK # Hitam
YE = Fore.YELLOW # Kuning

H="\033[1;92m" # Hijau
W="\033[1;97m" # Putih
Ab="\033[1;90m" # Abu Abu
Y="\033[1;93m" # Kuning
U="\033[1;95m" # Ungu
gktau="33[37;1m" # Entah
B="\033[1;96m" # Biru
#Tulisan Background Merah
bg="\033[1;0m\033[1;41mText\033[1;0m"

#def sf():
#	baca3 = requests.get("link sfile mobile lu",headers={"User-Agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36"}).text
#	baca2 = bs4.BeautifulSoup(baca3,"html.parser").find_all("div",{"class":"list"})[3].text
#	print (baca2.split("- Downloads:")[1])

def tanya():
	a=input(f"{W}re{Y}-{W}download {R}({U}Y{W}/{U}N{R}):{H} ")
	if a == "Y" or a == "y":
		os.system("python run.py")
	elif a == "N" or a == "n":
		sys.exit(f" {Y}[{H}^∆^{Y}]{W} Result --{B}»{R}⟩{H} Thx For Using My Tools")
	else:
		print (f" {W}[{Y}!{W}] Input Not Valid {R}!!!")
		time.sleep(3)
		tanya()

def mp3():
	try:
	        yt = YouTube(str(input(f" {Y}[{R}+{Y}]{W} Link ({U}Mp3{W}) --{B}»{R}⟩{H} ")))
	        video = yt.streams.filter(only_audio=True).first()
	        out_file = video.download(output_path="")
	        base, ext = os.path.splitext(out_file)
	        new_file = base + '.mp3'
	        os.rename(out_file, new_file)
	        print (f"{R} • {W}Judul {R}: {H}",yt.title)
	        print (f"{R} • {W}views {R}: {H}",yt.views)
	        print (f"{R} • {W}Publish On {R}: {H}",yt.publish_date)
	        print (f" {Y}[{H}✓{Y}]{W} Result --{B}»{R}⟩{H} Download Saved /sdcard/ytdl/mp3/"+yt.title)
	        os.system(f"cp '{base}.mp3' /sdcard/ytdl/mp3")
	        tanya()
	except pytube.exceptions.RegexMatchError:
		sys.exit(f" {Y}[{R}x{Y}]{W} Result --{B}»{R}⟩{H} Link Not Valid !!!")

def mp4():
	try:
		link = input(f" {Y}[{R}+{Y}]{W} Link ({U}Mp4{W}) --{B}»{R}⟩{H} ")
		yt = YouTube( link )
		print (f"{R} •{W} Judul{R}: {H}",yt.title)
		print (f"{R} •{W} Views{R}: {H}", yt.views)
		print (f"{R} •{W} Publish on{R}: {H}", yt.publish_date)
		stream = yt.streams.get_highest_resolution()
		ha=stream.download()
		print (f" {Y}[{H}✓{Y}]{W} Result --{B}»{R}⟩{H} Download Saved /sdcard/ytdl/mp4/"+yt.title+".mp4")
		os.system(f"cp '{ha}' /sdcard/ytdl/mp4")
		tanya()
	except pytube.exceptions.RegexMatchError:
		sys.exit(f" {Y}[{R}x{Y}]{W} Result --{B}»{R}⟩{H} Link Not Valid !!!")

def banner():
	baca3 = requests.get("https://sfile.mobi/10OeFaENP0Y7",headers={"User-Agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36"}).text
	baca2 = bs4.BeautifulSoup(baca3,"html.parser").find_all("div",{"class":"list"})[3].text 
	ha=baca2.split("- Downloads:")[1]
	os.system("mkdir /sdcard/ytdl && mkdir /sdcard/ytdl/mp4 && mkdir /sdcard/ytdl/mp3")
	os.system("clear")
	print (f"""
{W}┌────────────────────────────────────────────────────────────────────────────────────┐
{W}│{B}	   _________  ______   _						     {W}│
{W}│{B} |\     /|\__   __/ (  __  \ ( ) {R}•{W} Creator {R}:{W} AmmarrBN			             │
{W}│{B} ( \   / )   ) (    | (  \  )| ( {R}•{W} Youtube {R}:{W} Ammar Executed			     │
{W}│{B}  \ (_) /    | |    | |   ) || | {R}•{W} Github  {R}:{H} https://github.com/AmmarrBN{W}	     │
{W}│{B}   \   /     | |    | |   | || | {R}•{W} Insagrm {R}:{H} https://instagram.com/ammarexecuted{W}    │
{W}│{B}    ) (      | |    | |   ) || | {R}•{W} User    {R}:{Y} {ha} {W}People				     │
{W}│{B}    | |      | |    | (__/  )| (____/){W}						     │
{W}│{B}    \_/      )_(    (______/ (_______/{W}						     │
{W}│					{W}					     │
{W}└────────────────────────────────────────────────────────────────────────────────────┘""")
def menu():
	print (f"""{W}┌────────────────────────────────────────────────────────────────────────────────────┐
{W}│  		  Youtube Downloader {Y}Mp4 {H}&{Y} Mp3 {R}({U}Support Yt Short{R}){W}		     │
{W}│{R}  » {W}1{R}.{U}Convert {R}Youtube {W}Video To {Y}Mp4    {R}({H} Online {R}){W}			             │
{W}│{R}  » {W}2{R}.{U}Convert {R}Youtube {W}Video To {Y}Mp3    {R}({H} Online {R}){W}				     │
{W}│{R}  » {W}3{R}.{W}Support Admin   		      {R}({Y} YouTubee{R} ){W}				     │
{W}│{R}  » {W}4{R}.{W}Exit Tools		     {R}({Y} Exit Tools{R} ){W}			     	     │
{W}└────────────────────────────────────────────────────────────────────────────────────┘""")

def pilih():
	alok=input(f" {Y}[{R}+{Y}]{W} Input Menu --{B}»{R}⟩{H} ")
	if alok == "1" or alok == "01":
		banner()
		mp4()
	elif alok == "2" or alok == "02":
		banner()
		mp3()
	elif alok == "3" or alok == "03":
		os.system("xdg-open https://youtube.com/channel/UCyyIDnXYJlRI_-2pAQqKr0g")
	elif alok == "4" or alok == "04":
		sys.exit(f" {Y}[{R}+{Y}]{W} Result --{B}»{R}⟩{H} Exit Tools !!!!")
	else:
		sys.exit(f" {Y}[{R}-{Y}]{W} Result --{B}»{R}⟩{H} Menu Not Valid !!!!")

banner()
menu()
pilih()
