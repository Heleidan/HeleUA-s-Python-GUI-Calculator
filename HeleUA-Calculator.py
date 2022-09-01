from socket import SOMAXCONN
import tkinter as tk
tiny_font_style = ("Arial, 16")
smothy_gray = "#F5F5F5"
labeled_white = "#25265E"
class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x467")
        self.window.resizable(0, 0)
        self.window.title("HeleUA Calculator")
        #Display Label
        self.total_expression = "0"
        self.current_expression = "0"
        #buttoms
        self.display_frame = self.create_display_frame()
        self.buttoms_frame = self.create_buttoms_frame()
    #definition of display label function
    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, 
        bg=smothy_gray, fg=labeled_white, padx=24, font= tiny_font_style)
        total_label.pack(expand = True, fill = "both")
    #definitions of buttoms
    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=smothy_gray)
        frame.pack(expand = True, fill="both")
        return frame

    def create_buttoms_frame(self):
            frame = tk.Frame(self.window)
            frame.pack(expand=True, fill="both")
            return frame

    def run(self):
        self.window.mainloop()
if __name__ == "__main__":
    calc = Calculator()
    calc.run()
    
#Christian bebe lvl 1