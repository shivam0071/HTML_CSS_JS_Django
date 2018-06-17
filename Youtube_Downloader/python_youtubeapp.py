from pytube import YouTube
yt = YouTube("https://www.youtube.com/watch?v=YcKACsvp6Ck")
yt.title
yt.streams.all() #Choose a stream
stream = yt.streams.first() #lets take 1st for example
#stream.download() #You can give a path here
for reso in yt.streams.all():
    print(reso.resolution)

user_input = '144p'

for reso in yt.streams.all():
    print(reso.resolution)
    if reso.resolution == user_input:
        print ('Found it')
        print ('Downloading')
        print ('Stream is',reso)
        print(type(reso))
        reso.download()
        break
