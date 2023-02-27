import requests, bs4, tkinter as tk; from tkinter.scrolledtext import ScrolledText
def search(key):
    [answer.insert(tk.END, p.text) for url in [f"https://en.wikipedia.org/wiki/{key.replace(' ', '_')}", f"https://www.britannica.com/search?query={key.replace(' ', '%20')}"] for p in bs4.BeautifulSoup(requests.get(url).content, 'html.parser').find_all(['p', 'p', {'class': 'topic-paragraph'}])]
    answer.configure(state='disabled')
window, searchterm, button, answer = tk.Tk(), tk.Entry(), tk.Button(text="Search"), ScrolledText(width=80, height=30)
button.bind("<Button-1>", lambda event: search(searchterm.get()))
searchterm.pack(); button.pack(); answer.pack()
window.mainloop()