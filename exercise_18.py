# Identify the last token in a URL

link = "https://www.udemy.com/course/just-enough-python/learn/quiz/4990972#overview"

list_a = link.split("/")

def last_token(url):
  list_all = url.split("/")
  
  return list_all[-1]
  
print(last_token(link))
