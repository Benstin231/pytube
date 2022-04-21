from pytube import YouTube

link = input("請輸入Youtube影片網址：\n")

yt = YouTube(link)

# 印出標題
print(f"\n標題： {yt.title}")

# 印出觀看數
print(f"\n觀看次數： {yt.views}")

# 印出影片長度
print(f"\n影片長度： {yt.length}")

video = yt.streams.get_highest_resolution()

print("\n下載中...")

video.download("下載檔案")

print("下載成功！\n")