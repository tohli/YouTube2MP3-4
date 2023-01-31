from pytube import YouTube

def Download(link):
  youtubeObject = YouTube(link)
  youtubeObject = youtubeObject.streams.get_highest_resolution()
  try:
      youtubeObject.download()
  except:
    print("Error")
  print("This download has completed.")

link = input("Enter video link:")
Download(link)

