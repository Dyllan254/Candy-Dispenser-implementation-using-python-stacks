from tkinter import Button, Canvas, LEFT, Label, RAISED, RIGHT, Tk
from tkinter.messagebox import showerror, showinfo


class Dispenser:

    def __init__(self, window: Tk):
        self.window = window
        self.color_primary = "Red"

        self.candy_stack = []
        self.max_size = 9

        # The Spring
        self.spring_left = 73 # The x-coordinate of the leftmost point of the spring.
        self.spring_right = 287 # The x-coordinate of the rightmost point of the spring.
        self.spring_top = 120 # The y-coordinate of the uppermost point of the spring.
        self.spring_bottom = 600 # The y-coordinate of the lowermost point of the spring.
        self.spring_offset = 35 # The offset between the individual spring segments.
        self.spring_thickness = 7

        # The y-coordinates of the spring used to define the positions of the individual spring segments.
        self.a_y = 120
        self.b_y = 220
        self.c_y = 330
        self.d_y = 430
        self.e_y = 530

        # The candy bar
        self.candy_bar_bottom = self.spring_top + 35
        self.candy_bar_cx = (self.spring_left + self.spring_right) / 2
        self.candy_bar_cy = (self.spring_top + self.candy_bar_bottom) / 2

        # Split The canvas into two equal parts
        self.spring_canvas = Canvas(self.window, width=(window_width / 2), height=window_height, background="floral "
                                                                                                            "white")
        self.spring_canvas.pack(side=LEFT)

        self.control_panel = Canvas(self.window, width=(window_width / 2), height=window_height)
        self.control_panel.pack(side=RIGHT)

        # Left panel heading
        self.heading_name = Label(self.spring_canvas, text="Candy Dispenser", bg="white", fg="black",
                                  font=("Arial", 20, "bold"))
        self.heading_name.place(x=80, y=20)

        # Right panel heading
        self.heading_name = Label(self.control_panel, text="Press Below ↓", bg="white", fg="black",
                                  font=("Arial", 20, "bold"))
        self.heading_name.place(x=90, y=20)

        # Draw the Spring
        self.a = self.spring_canvas.create_line(self.spring_left, self.a_y, self.spring_right, self.a_y,
                                             width=self.spring_thickness, smooth=True)

        self.a_b1 = self.spring_canvas.create_line(self.spring_left, self.a_y, self.spring_right, self.b_y,
                                                width=self.spring_thickness, smooth=True)

        self.a_b2 = self.spring_canvas.create_line(self.spring_left, self.b_y, self.spring_right, self.a_y,
                                                width=self.spring_thickness, smooth=True)

        self.b = self.spring_canvas.create_line(self.spring_left, self.b_y, self.spring_right, self.b_y,
                                             width=self.spring_thickness, smooth=True)

        self.b_c1 = self.spring_canvas.create_line(self.spring_left, self.c_y, self.spring_right, self.b_y,
                                                width=self.spring_thickness, smooth=True)

        self.b_c2 = self.spring_canvas.create_line(self.spring_right, self.c_y, self.spring_left, self.b_y,
                                                width=self.spring_thickness, smooth=True)

        self.c = self.spring_canvas.create_line(self.spring_left, self.c_y, self.spring_right, self.c_y,
                                             width=self.spring_thickness, smooth=True)

        self.c_d1 = self.spring_canvas.create_line(self.spring_left, self.c_y, self.spring_right, self.d_y,
                                                width=self.spring_thickness, smooth=True)

        self.c_d2 = self.spring_canvas.create_line(self.spring_right, self.c_y, self.spring_left, self.d_y,
                                                width=self.spring_thickness, smooth=True)

        self.d = self.spring_canvas.create_line(self.spring_left, self.d_y, self.spring_right, self.d_y,
                                             width=self.spring_thickness, smooth=True)

        self.d_e1 = self.spring_canvas.create_line(self.spring_left, self.d_y, self.spring_right, self.e_y,
                                                width=self.spring_thickness, smooth=True)

        self.d_e2 = self.spring_canvas.create_line(self.spring_right, self.d_y, self.spring_left, self.e_y,
                                                width=self.spring_thickness, smooth=True)

        self.spring_canvas.create_line(self.spring_left, self.e_y, self.spring_right, self.e_y,
                                    width=self.spring_thickness, smooth=True)

        # Create Spring Outline
        self.spring_canvas.create_line(70, 70, 70, 540, width=3)
        self.spring_canvas.create_line(290, 70, 290, 540, width=3)
        self.spring_canvas.create_line(290, 540, 70, 540, width=3)
        self.spring_canvas.create_line(60, 70, 60, 545, width=3)
        self.spring_canvas.create_line(300, 70, 300, 545, width=3)
        self.spring_canvas.create_line(290, 540, 70, 540, width=3)
        self.spring_canvas.create_line(300, 545, 60, 545, width=3)

        # Draw the buttons for the right panel
        Button(self.control_panel, text="Push", bg="white", font=("Arial", 15, "bold"),
                 relief=RAISED, command=self.push).place(x=80, y=100)

        Button(self.control_panel, text="Top", fg="black", bg="white", font=("Arial", 15, "bold"),
               relief=RAISED,  command=self.top).place(x=220, y=100)

        Button(self.control_panel, text="Pop", fg="black", bg="white", font=("Arial", 15, "bold"),
               relief=RAISED, command=self.pop).place(x=80, y=180)

        Button(self.control_panel, text="Size", fg="black", bg="white", font=("Arial", 14, "bold"),
               relief=RAISED, command=self.report_size).place(x=220, y=180)

        Button(self.control_panel, text="Is Empty?", fg="black", bg="white", font=("Arial", 14, "bold"),
               relief=RAISED, command=self.report_empty_stat).place(x=80, y=251)

        # Outline for the Buttons
        self.control_panel.create_line(290, 70, 70, 70, width=3)
        self.control_panel.create_line(70, 70, 70, 300, width=3)
        self.control_panel.create_line(290, 70, 290, 300, width=3)
        self.control_panel.create_line(290, 300, 70, 300, width=3)

    def pop(self):
        if self.size() > 0:

            candy = self.candy_stack.pop()
            self.spring_canvas.delete(candy['bar'])
            self.spring_canvas.delete(candy['label'])

            self.update_dispenser('pop')
            showinfo("Popped Candy", f"Popped Candy is {candy['tag']}")
        else:
            showerror("Error!", "The Dispenser is empty.")

    def push(self):
        if self.size() < self.max_size:
            self.candy_stack.append(self.draw_candy())  # Add candy to stack.
            self.update_dispenser('push')
        else:
            showerror(" ", "The Dispenser is full.")

    def draw_candy(self):
        bar = self.spring_canvas.create_rectangle(self.spring_left, self.spring_top, self.spring_right,
                                          self.candy_bar_bottom, fill="Red", outline="Blue")
        tag = f'Gumball {self.size() + 1}'
        label = self.spring_canvas.create_text(self.candy_bar_cx, self.candy_bar_cy, text=tag, fill='white')
        return {'bar': bar, 'label': label, 'tag': tag}

    def update_dispenser(self, mode):
        # Update position of all candies excluding the topmost in the stack.
        if mode == 'push':
            for i in range(self.size()):
                self.update_candy_pos(self.candy_stack[i], (self.size() - 1) - i)

            # Update spring's pitch.
            self.a_y += self.spring_offset
            self.b_y += self.spring_offset / 1.5
            self.c_y += self.spring_offset / 2
            self.d_y += self.spring_offset / 3

        elif mode == 'pop':
            stack_size = self.size()
            for i in range(stack_size):
                self.update_candy_pos(self.candy_stack[i], stack_size - (i + 1))

            # Update spring's pitch.
            self.a_y -= self.spring_offset
            self.b_y -= self.spring_offset / 1.5
            self.c_y -= self.spring_offset / 2
            self.d_y -= self.spring_offset / 3
        else:
            raise Exception

        # Update the spring.
        self.spring_canvas.coords(self.a, self.spring_left, self.a_y, self.spring_right, self.a_y)
        self.spring_canvas.coords(self.a_b1, self.spring_left, self.a_y, self.spring_right, self.b_y)
        self.spring_canvas.coords(self.a_b2, self.spring_left, self.b_y, self.spring_right, self.a_y)
        self.spring_canvas.coords(self.b, self.spring_left, self.b_y, self.spring_right, self.b_y)
        self.spring_canvas.coords(self.b_c1, self.spring_left, self.c_y, self.spring_right, self.b_y)
        self.spring_canvas.coords(self.b_c2, self.spring_right, self.c_y, self.spring_left, self.b_y)
        self.spring_canvas.coords(self.c, self.spring_left, self.c_y, self.spring_right, self.c_y)
        self.spring_canvas.coords(self.c_d1, self.spring_left, self.c_y, self.spring_right, self.d_y)
        self.spring_canvas.coords(self.c_d2, self.spring_right, self.c_y, self.spring_left, self.d_y)
        self.spring_canvas.coords(self.d, self.spring_left, self.d_y, self.spring_right, self.d_y)
        self.spring_canvas.coords(self.d_e1, self.spring_left, self.d_y, self.spring_right, self.e_y)
        self.spring_canvas.coords(self.d_e2, self.spring_right, self.d_y, self.spring_left, self.e_y)

        # Redraw the  components
        self.spring_canvas.update()

        # Update the candy's position
    def update_candy_pos(self, candy, y):
        updated_bar_top = self.spring_top + (self.spring_offset * y)
        updated_bar_bottom = self.candy_bar_bottom + (self.spring_offset * y)

        self.spring_canvas.coords(
            candy['bar'], self.spring_left, updated_bar_top, self.spring_right, updated_bar_bottom
        )
        self.spring_canvas.coords(
            candy['label'], self.candy_bar_cx, (updated_bar_top + updated_bar_bottom) / 2
        )

    def size(self):
        return len(self.candy_stack)

    def report_size(self):
        showinfo('Size', f'The size of the Dispenser is {self.size()}')

    def top(self):
        if self.is_empty():
            showerror('Error!', 'The Dispenser is empty')
        else:
            showinfo('Top', f'The Top candy is "{self.candy_stack[-1]["tag"]}"')

    def is_empty(self):
        if self.size() == 0:
            return True
        return False

    def report_empty_stat(self):
        msg = 'False'
        if self.is_empty():
            msg = 'True'
        showinfo('Is Empty?', msg)


if __name__ == '__main__':
    window_height = 550
    window_width = 850

    root = Tk()
    root.title('Dyllan Macharia')
    root.maxsize(window_width, window_height)
    root.minsize(window_width, window_height)
    Dispenser(root)
    root.mainloop()
