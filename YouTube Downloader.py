from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("ERROR!")
    print("Your video has been downloaded successfully.")

link = input("Enter the YouTube video URL: ")
Download(link)