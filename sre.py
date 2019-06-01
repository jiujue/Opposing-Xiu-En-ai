import os
import time
import pygame
import urllib.request
import win32api,win32con,win32gui
import threading
import tkinter


imgURLList=['https://ss1.bdstatic.com/070cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2140782809,1577943474&fm=26&gp=0.jpg',
            'https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=3238864665,3372090867&fm=26&gp=0.jpg',
            'https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=3238864665,3372090867&fm=26&gp=0.jpg',
            'https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=773726867,4012061604&fm=26&gp=0.jpg',
            'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1559325983449&di=d00a8110ab4f8fcaef772db90cab93f4&imgtype=0&src=http%3A%2F%2Fimage.biaobaiju.com%2Fuploads%2F20181220%2F23%2F1545318794-mZTIxivtJU.jpg',
            'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1559325979759&di=3ac645fb70c115ad87f3a34ac179519e&imgtype=0&src=http%3A%2F%2Fimg.besoo.com%2Ffile%2F201809%2F11%2F1ppsda4iyb0.jpg',
            'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1559325970909&di=4c2e193cecd5b7a3bf0a1bd761ac31b6&imgtype=0&src=http%3A%2F%2Fimage.biaobaiju.com%2Fuploads%2F20180801%2F00%2F1533055147-IYumHAzWiB.jpg',
            'https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=1995988220,278297006&fm=26&gp=0.jpg',
            'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1559325961458&di=4b7e9c1832174bd233130f6459241eb3&imgtype=0&src=http%3A%2F%2Fwww.feizl.com%2Fupload2007%2F2017_04%2F17042800206967.jpg',
            'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1559325956068&di=acc5c10ca782b7b5971c977a18cd4725&imgtype=0&src=http%3A%2F%2Fimage.biaobaiju.com%2Fuploads%2F20181220%2F23%2F1545319058-XMZJbxolWL.jpg',
            'https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=1883047906,2493026963&fm=26&gp=0.jpg',
            ]

fileList = []
IsExit=False
def downLoadimg():
    path = "C:\\tempOfjiujueismmp\\"
    try:
        os.mkdir("C:\\tempOfjiujueismmp\\")
    except:
        pass
    i=0
    for it in imgURLList:
        imgName=str(i)+"jpg"
        with open(path+str(imgName),"wb") as f:
            f.write(urllib.request.urlopen(it).read())
        # print(path+imgName)
        fileList.append(path+imgName)
        i+=1

def changeBGI():
    downLoadimg()
    key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,
                                "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(key, "WallpaperStyle", 0, win32con.REG_SZ, "2")

    while True:
        if IsExit == True:
            exit()
        for it in fileList:
            win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, it, win32con.SPIF_SENDWININICHANGE)
            time.sleep(3)

def playMusic():
    pygame.mixer.init()
    pygame.mixer.music.load('music.mp3')
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)

    while True:
        pass


def msg():
    win32api.MessageBox(0,"你好,下次开机记得不要虐狗哦\n(我已经帮你定时关机,不如点击确定 然后 切换到桌面 听完这首歌)"
                          ,"感情虽好,仍有分离",0)
    os.system("shutdown -s -t 199")


def control():
    win=tkinter.Tk()
    win.title("From jiujuismmp")
    global IsExit
    btn=tkinter.Button(win,width=80,height=5,text="exit",command=msg)
    btn.pack(expand=True,fill=tkinter.BOTH)
    win.protocol("WM_DELETE_WINDOW", msg)
    win.mainloop()
    while True:
        pass


if __name__ == '__main__':
    t=threading.Thread(target=control)
    t1=threading.Thread(target=changeBGI)
    t2=threading.Thread(target=playMusic)

    t.start()
    t1.start()
    t2.start()

    t.join()
    t1.join()
    t2.join()

