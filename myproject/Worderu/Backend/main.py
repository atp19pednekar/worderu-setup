from sound import sound_record
from transcribe import transcription
from export import export
from analysis import summary,sentiment,positive

def character_mapping(sentiment):

    if (sentiment>0.5 and sentiment <1.0):
        message="You can be Avatar Aang or Uncle Iroh, your words are gentle and positive!"
    elif(sentiment>0.0 and sentiment<=0.5):
        message="You can be katara or Sokka, your words are firm but still positive!"
    elif(sentiment==0.0):
        message="You can be Zuko or Toph, wow look at somebody who is truly neutral verbally!"
    elif(sentiment>=-0.5 and sentiment<0.0):
        message="You are slightly to moderately negetive, Mai from Team Azula fits you the best!"
    else:
        message="You can easily become Firelord Ozai or Azula, talk about some negetive speech!"
    
    return message

def main():

    sound_record() #Should get triggered on Click of Record Sound button on Index.html

    data = transcription() #Transcribe the Audio to Text using Open AI Whisper Small model

    paragraph=summary(data) #Summarise the Text using Tansfromers

    emotion=sentiment(data) #Guage top emotions detected in text

    scale=positive(data) #Rank the sentiment Score detected in text

    # Except Export() all functions get called on Get started button

    message=character_mapping(scale)

    print(data,"\n")

    print(paragraph,"\n")

    print(emotion,"\n")

    print(scale,"\n")
    
    print(message)

    export(data) #Export the data to PDF 
    #gets called on clicking export button


if __name__ == '__main__':
    main()