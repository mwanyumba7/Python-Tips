from newspaper import Article

news = Article("https://indianexpress.com/article/"

"technology/gadgets/"
"apple-discontinues-its-last-ipod-model-7910720/")
news.download()
news.parse()
print(news.title)

#Output
End of an Era: Apple discontinues its last iPod model