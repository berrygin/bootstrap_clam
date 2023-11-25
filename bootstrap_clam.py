import tkinter as tk
import tkinter.ttk as ttk


class Bootstrap_clam(tk.Frame):
    ''' Bootstrap Superhero & clam Theme '''
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        style = ttk.Style()
        style.theme_use('clam')

        cyborg_colors = {
            'primary': '#0da3de',
            'secondary': '#5e5e5e',
            'success': '#68be0d',
            'info': '#ad0dd4',
            'warning': '#ff890d',
            'danger': '#df0d0d',
            'foreground': '#ffffff',
            'light': '#2d2d2d',
            'dark': '#b1b3b2',
            'background': '#060606'
        }

        darkly_colors = {
            'primary': '#315883',
            'secondary': '#444444',
            'success': '#00c38c',
            'info': '#0095e2',
            'warning': '#fe9b00',
            'danger': '#f8371f',
            'foreground': '#ffffff',
            'light': '#acb5be',
            'dark': '#303030',
            'background': '#222'
        }

        superhero_colors = {
            'primary': '#df6919',
            'secondary': '#4e5d6c',
            'success': '#5cb85c',
            'info': '#5bc0de',
            'warning': '#ffc107',
            'danger': '#d9534f',
            'foreground': '#ebebeb',
            'light': '#abb6c2',
            'dark': '#20374c',
            'background': '#0f2537'
        }

        colors = cyborg_colors

        bg = colors['background']
        fg = colors['foreground']
        h1 = 'Arial', 32
        h2 = 'Arial', 24
        h3 = 'Arial', 16
        body = 'Arial', 8

        style.configure('c.TFrame', background=bg)
        style.configure('c.TLabel', background=bg, foreground=fg, font=h1)
        style.configure('primary.TLabel', background=colors['primary'], foreground=fg, font=h3)
        style.configure('secondary.TLabel', background=colors['secondary'], foreground=fg, font=h3)
        style.configure('success.TLabel', background=colors['success'], foreground=fg, font=h3)
        style.configure('info.TLabel', background=colors['info'], foreground=fg, font=h3)
        style.configure('warning.TLabel', background=colors['warning'], foreground=fg, font=h3)
        style.configure('danger.TLabel', background=colors['danger'], foreground=fg, font=h3)
        style.configure('light.TLabel', background=colors['light'], foreground=fg, font=h3)
        style.configure('dark.TLabel', background=colors['dark'], foreground=fg, font=h3)

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.master.geometry('512x512+64+64')
        self.master.title('Bootstrap theme')

        frame = ttk.Frame(self.master, style='c.TFrame')
        frame.pack(expand=True, fill=tk.BOTH)

        theme = 'Cyborg'
        label = ttk.Label(frame, text=theme, style='c.TLabel')
        label.pack(pady=8)
        label = ttk.Label(frame, text=' primary', anchor=tk.W, style='primary.TLabel')
        label.pack(expand=True, fill=tk.BOTH, padx=32, pady=8)
        label = ttk.Label(frame, text=' secondary', anchor=tk.W, style='secondary.TLabel')
        label.pack(expand=True, fill=tk.BOTH, padx=32, pady=8)
        label = ttk.Label(frame, text=' success', anchor=tk.W, style='success.TLabel')
        label.pack(expand=True, fill=tk.BOTH, padx=32, pady=8)
        label = ttk.Label(frame, text=' info', anchor=tk.W, style='info.TLabel')
        label.pack(expand=True, fill=tk.BOTH, padx=32, pady=8)
        label = ttk.Label(frame, text=' warning', anchor=tk.W, style='warning.TLabel')
        label.pack(expand=True, fill=tk.BOTH, padx=32, pady=8)
        label = ttk.Label(frame, text=' danger', anchor=tk.W, style='danger.TLabel')
        label.pack(expand=True, fill=tk.BOTH, padx=32, pady=8)
        label = ttk.Label(frame, text=' light', anchor=tk.W, style='light.TLabel')
        label.pack(expand=True, fill=tk.BOTH, padx=32, pady=8)
        label = ttk.Label(frame, text=' dark', anchor=tk.W, style='dark.TLabel')
        label.pack(expand=True, fill=tk.BOTH, padx=32, pady=8)
        
        ttk.Frame(frame, style='c.TFrame').pack(pady=8)

if __name__ == '__main__':
    root = tk.Tk()
    _ = Bootstrap_clam(root)
    app = App(master=root)
    app.mainloop()
