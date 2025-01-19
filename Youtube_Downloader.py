import pytube
import os
import subprocess
import speedtest
import time


def full_program(video, downloads):
  
  # input video preferences

  # Extension
  ext = input("Enter the format: ").lower()
  form = ["mp4", "mp3", "avi", "mov"]
  while ext not in form and ext != "":
    print(f"Please choose one the availabe format \n{', '.join(form)}")
    ext = input("Format: ")
  if ext == "":
    ext = "mp4"
  
  # List all available resolution of the video
  S = set()
  for stream in pytube.YouTube(video).streams.order_by("resolution"):
    S.add(int(stream.resolution[:-1]))
  Reso = list(map(lambda x: f"{str(x)}p", sorted(list(S))))

  # Resolution
  if ext in ["mp4", "avi", "mov"]:
    reso = input("Enter the resolution: ").lower()
    while reso not in Reso and reso != "":
      print(f"Please choose one the availabe resolution \n{Reso}")
      reso = input("Resolution: ")
    if reso == "":
      reso = Reso[-1]
      print(Reso[-1])

  # Location
  direc = input("Enter the path: ")
  if not os.path.exists(direc) and direc != "Downloads" and direc != "":
    direc = input("Please enter a valid path: ")
  if direc == "Downloads" or os.path.isdir(direc) == False or direc == "":
    direc = downloads

  # Name
  def Valid(ch):
    symb = '<>:"/\|?*'
    i = 0
    ok = True
    while (ok) and (i < len(ch)): 
      ok = symb.find(ch[i]) != -1 or ch[i].isalnum()
      i += 1 
    return ok

  name = input("Enter the file name: ")
  if name == "":
    print("The title of the video will be the name of the file")
    name = f"{pytube.YouTube(video).title}.{ext}"
    while not Valid(name): 
      print("The title of the video is an invalid name")
      ch1 = input("(E)nter new file name or (R)emove characters: ").lower()
      rm = ["r", "remove", "remove characters"]
      ent = ["e", "enter", "enter new file name"]
      if ch1 in ent: 
        name = input("File name: ")
        while not Valid(name): 
          name = input("File name: ")
      elif ch1 in rm:
        name = "".join(list(filter(Valid, name)))
      else:
        while ch1 not in rm + ent:
          ch1 = input("(E)nter new file name or (R)emove characters: ").lower()
  else: 
    while not Valid(name): 
      name = input("Enter the file name: ")
  name = Path(direc, name)


  # Download
  if ext == "mp3":
    yt = pytube.YouTube(video).streams.filter(only_audio=True).first()
    remain(yt)
    yt.download(output_path=direc, filename=name)
    print("Audio Downloaded Successfully!")
  else: # Video
    yt = pytube.YouTube(video).streams.filter(res=reso).first()
    # if save.is_progressive:
    if True:
      remain(yt)
      yt.download(output_path=direc, filename=name)
      print("Video Downloaded Successfully!")
    else: # Working
      print("Program stopped!")
      # exit()
      def ffm():
        aud = f"{name[::-1][name[::-1].find('.'):][::-1]}.mp3"
        vid = f"{name[::-1][name[::-1].find('.'):][::-1]}.mp4"
        ad = pytube.YouTube(video).streams.filter(only_audio=True).first()
        vd = pytube.YouTube(video).streams.filter(res=reso).first()

        ad.download(output_path=direc, filename=aud)
        vd.download(output_path=direc, filename=vid)
        os.chdir("/home/ghoudiy/Downloads/")
        subprocess.run(f"ffmpeg -loglevel panic -i '{vid}' -i '{aud}' -c:v copy -c:a aac '{name}'", shell=True)
        os.remove(aud)
        os.remove(vid)
        print("Video Downloaded Successfully!")
      # Not completed
      print("New condition", Reso.index(reso))
      i = Reso.index(reso)
      while i > 0: 
        try:
          save = pytube.YouTube(video).streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()
          remain(save)
          start = time.time()
          save.download(output_path=direc, filename=name)
          print("Real time: ", (time.time() - start) / 60, "minutes", (time.time() - start) % 60, "seconds")
          break
        except:
          i -= 1
      
def demo_program(video,direc):
  yt = pytube.YouTube(video).streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()	
  name = f"{pytube.YouTube(video).title}.mp4"
  name = Path(direc, name)
  # remain(yt)
  yt.download(output_path=direc, filename=name)
  print("Video Downloaded Successfully!")


# Some function needed in program globally
def remain(*yot):
  speed = speedtest.Speedtest(secure=True).upload() * (10**-6)
  print(f'Your internet upload is {"%.3f" % speed} Mb/s')
  size = 0
  for i in range(len(yot)):
    size += yot[i].filesize * (10 ** -5)
  dur = f"{int(size // speed // 60)} minute(s) and {int(size // speed % 60)} second(s) remaining"
  if int(size // speed // 60) > 3:
    if size >= 1000:  
      print("The size of the video=","%.3f" % (size / 1000))
    else: 
      print("The size of the video=", "%.3f" % size)
  print(dur, "(Approx value)")

def Path(direc,name):
  if os.path.exists(f"{direc}/{name}"):
    print("Look like you have the same name in your dir.")
    ch = input("Replace with the new video? [Y/n]: ").lower()
    if ch == "": 
      ch = "n"
    while ch not in ["y","n"] and ch != "":
      ch = input("[Y/n]: ").lower()
    if ch == "y": 
      os.remove(f"{direc}\{name}")
    else: 
      exec(open("/home/ghoudiy/Documents/Programming/Python/Programs/Uncompleted_Programs/03_Rename.py").read(), globals())
      name = mv(name,direc)
  return name

video = input("Enter The Video URL: ")

downloads = os.path.expanduser("~") + "/Downloads"

ch = input("(D)emo or (F)ull program: ").lower()
if ch == "d":
  demo_program(video, downloads)
else:
  full_program(video, downloads)

