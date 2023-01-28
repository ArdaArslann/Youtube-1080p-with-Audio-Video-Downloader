
import os
from moviepy.editor import *
from tkinter import * 
from tkinter import ttk,messagebox
from slugify import slugify
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube
from pytube import*
import moviepy
import moviepy.editor as mymovie

Foldername =""
videofolder=""
audiofolder="" 
def openloc():
    global Foldername
    Foldername=filedialog.askdirectory()
    
    if(len(Foldername)>1):
        locationnerror.config(text=Foldername,fg="green")
    
    
  
    else:
        locationnerror.config(text="Choose Directory",fg="red")
    
    
def audioandvideocombine():
    url=ytdentry.get()
    yt = YouTube(url)
    
   
  
  
def Download_vid():
    choice = ytdchoices.get()
    url=ytdentry.get()

    

    if(len(url)>1):
        ytderror.config(text="")
        yt = YouTube(url)
        
        
    
  
    if(choice == choices[0]):
        filenamee=slugify(YouTube(url).title)
        video=yt.streams.filter(adaptive=True).first()
        size = yt.streams.filter(adaptive=True).first().filesize
        
        try:
            get=messagebox.askyesno("Do You Want To Download",f"File Size: {round(size* 0.000001, 2)} MB")
            
            if get==True:
                video.download(Foldername,filenamee+".mp4")    
                
                 
        except Exception as e:
             messagebox.showerror("Check Your Internet Connection!")
        
        
    
    
    elif(choice==choices[1]):
       filenamee=slugify(YouTube(url).title)
       audio = yt.streams.filter(only_audio=True).last().download(Foldername,filenamee+".webm")
       
       clip = moviepy.editor.AudioFileClip(Foldername+"/"+filenamee+".webm")
       
       clip.write_audiofile(Foldername+"/"+filenamee+".mp3")
       clip.close()
       os.remove(audio)
       
        
        
        
    elif(choice==choices[2]):
        
            filenamee=slugify(YouTube(url).title)
            videofolder=(Foldername+ "/" + filenamee+".mp4")
            audiofolder=(Foldername+ "/" + filenamee+".mp3")
        
            
            inputvideo=videofolder
            inputaudio=audiofolder
            outputvideo=(Foldername+"/"+ filenamee+"last"+".mp4")
        
            videoclip=mymovie.VideoFileClip(inputvideo)
            audioclip=mymovie.AudioFileClip(inputaudio)
            finalclip=videoclip.set_audio(audioclip)
            finalclip.write_videofile(outputvideo,fps=60)
            
            os.remove(videofolder)
            os.remove(audiofolder)
            
        
  
        
        
    else:
        ytderror.config(text="Paste the link again",fg="red")
    
    
    
 

    ytderror.config(text="Download Completed",fg="green")



root = Tk()
root.title("Youtube Video and Sound Converter")

root.geometry("350x400")
root.columnconfigure(0,weight=1)



ytdlabel= Label(root,text="Enter URL:",font=("bahnschrift semilight",15))
ytdlabel.grid()

ytdentryvar=StringVar()
ytdentry=Entry(root,width=50,textvariable=ytdentryvar)
ytdentry.grid()

ytderror=Label(root,text="Error",fg="red",font=("bahnschrift semilight",13))
ytderror.grid()

savelabel=Label(root,text="Save the Video",font=("bahnschrift semilight",15))
savelabel.grid()

saveEntry=Button(root,width=13,bg="red",fg="white",text="Choose Directory:",command=openloc)
saveEntry.grid()

locationnerror=Label(root,text="Directory causes Error",fg="red",font=("bahnschrift semilight",13))
locationnerror.grid()





choices = ["1080p","Audio","Combine"]
ytdchoices = ttk.Combobox(root,values=choices)
ytdchoices.grid()

    

downloadbtn=Button(root,width=10,text="Apply",bg ="green",fg="lightyellow",font=("bahnschrift semilight",15),command=Download_vid)

downloadbtn.grid()

root.mainloop()

#01000001 01110010 01100100 01100001 00100000 01000001 01110010 01110011 01101100 01100001 01101110

