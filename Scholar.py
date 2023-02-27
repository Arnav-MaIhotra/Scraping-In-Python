import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
def search(key):
  url1 = f"https://en.wikipedia.org/wiki/{key.replace(' ', '_')}"
  soup1 = BeautifulSoup(requests.get(url1).content, "html.parser")
  for p in soup1.find_all('p'):
      answer.insert(tk.END, p.text)
  url2 = f"https://www.britannica.com/search?query={key.replace(' ', '%20')}"
  soup2 = BeautifulSoup(requests.get(url2).content, "html.parser")
  for a in soup2.find('ul', class_='list-unstyled results').find_all('a', href=True):
      url3 = f"https://www.britannica.com{a['href']}"
      soup3 = BeautifulSoup(requests.get(url3).content, "html.parser")
      try:
        answer.insert(tk.END, soup3.find('p', class_='topic-paragraph').text)
      except:
        continue
  answer.configure(state='disabled')
def handle_click(event):
    term = searchterm.get()
    search(term)
window = tk.Tk()
window.configure(bg='white')
searchterm = tk.Entry()
button = tk.Button(text = "Search")
button.bind("<Button-1>", handle_click)
answer = ScrolledText(width=80, height=30)
searchterm.pack()
button.pack()
answer.pack()
window.mainloop()