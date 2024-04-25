import tkinter as tk
from tkinter import ttk

from main import WordLadder


class WordLadderApp(tk.Tk, WordLadder):
    def __init__(self):
        tk.Tk.__init__(self)
        WordLadder.__init__(self)
        self.title('Word Ladder Game')
        self.geometry('800x600')

        self.rowconfigure(tuple(range(0, 5)), weight=2)
        self.columnconfigure(tuple(range(0, 5)), weight=2)
        self.columnconfigure(2, weight=1)

        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        label_font = ('Arial', 36)
        button_font = ('Arial', 24)

        self.src_label = tk.Label(self, text="Source word:", font=label_font)
        self.src_entry_var = tk.StringVar() 
        self.src_entry = ttk.Combobox(self, 
                                      textvariable=self.src_entry_var, 
                                      values=[],
                                      width=10,
                                      state='normal')
        self.src_entry.bind("<KeyRelease>", self.detect_src_input)

        self.dst_label = tk.Label(self, text="Destination word:", font=label_font)
        self.dst_entry_var = tk.StringVar() 
        self.dst_entry = ttk.Combobox(self,
                                      textvariable=self.dst_entry_var, 
                                      values=[],
                                      width=10)
        self.dst_entry.bind("<KeyRelease>", self.detect_dst_input)

        self.output_label = tk.Label(self, text="Shortest path:", font=button_font)

        self.find_button = tk.Button(self, text="Find", command=self.button_pressed, font=button_font)
        self.find_button.config(width=10, height=2)

    def create_layout(self):
        self.src_label.grid(row=1, column=1, sticky='s')
        self.src_entry.grid(row=2, column=1, sticky='n')
        self.dst_label.grid(row=1, column=3, sticky='s')
        self.dst_entry.grid(row=2, column=3, sticky='n')
        self.find_button.grid(row=3, column=2)
        self.output_label.grid(row=2, column=1, sticky='ws', columnspan=4)

    def button_pressed(self):
        src = self.src_entry_var.get()
        dst = self.dst_entry_var.get()

        self.src_entry_var.set('')
        self.dst_entry_var.set('')

        path = self.find_shortest_path(src, dst)
        if path:
            self.output_label.config(text=' -> '.join(path))
        else:
            self.output_label.config(text='No possible paths')

    def detect_src_input(self, event):
        word = self.src_entry_var.get()
        res = self.word_dictionary.complete(word)
        
        self.src_entry.config(values=res[:5])

        if event.keysym in ["Command", "Meta_L", "Meta_R"]:
            self.src_entry.event_generate("<Down>")

    def detect_dst_input(self, event):
        word = self.dst_entry_var.get()
        res = self.word_dictionary.complete(word)
        
        self.dst_entry.config(values=res[:5])

        if event.keysym in ["Command", "Meta_L", "Meta_R"]:
            self.dst_entry.event_generate("<Down>")


if __name__ == '__main__':
    app = WordLadderApp()
    app.mainloop()
