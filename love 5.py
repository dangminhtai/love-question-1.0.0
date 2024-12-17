import tkinter as tk
from PIL import Image, ImageTk
import random

root = tk.Tk()
root.title("Love Question")
root.geometry("800x600")

# Load images
love_q_img = Image.open("love_question.png")
yes_img = Image.open("yes.png")
yes_hover = Image.open("yes_hover.png")
no_img = Image.open("no.png")
no_hover = Image.open("no_hover.png")

def resize_img(x, scale):
    width, height = x.size
    new_width = int(width * scale)
    new_height = int(height * scale)
    return x.resize((new_width, new_height))

# Random movement for "No" button
def move_button(event=None):
    target_x = random.randint(0, 700)
    target_y = random.randint(0, 500)
    current_x, current_y = canvas.coords(button_no)
    delta_x = target_x - current_x
    delta_y = target_y - current_y
    steps = 40
    step_x = delta_x / steps
    step_y = delta_y / steps

    def update_position(step):
        canvas.coords(button_no, current_x + step_x * step, current_y + step_y * step)
        if step < steps:
            root.after(1, lambda: update_position(step + 1))
    update_position(0)

# Images with resizing
love_photo = ImageTk.PhotoImage(love_q_img)
yes_photo = ImageTk.PhotoImage(resize_img(yes_img, 0.3))
yes_hover_photo = ImageTk.PhotoImage(resize_img(yes_hover, 0.3))
no_photo = ImageTk.PhotoImage(resize_img(no_img, 0.3))
no_hover_photo = ImageTk.PhotoImage(resize_img(no_hover, 0.3))

# Canvas setup
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

# Background image
label_loveq = canvas.create_image(0, 0, anchor=tk.NW, image=love_photo)

# "Yes" button on canvas
button_yes = canvas.create_image(70, 300, anchor=tk.NW, image=yes_photo, tags="yes")

# "No" button on canvas
button_no = canvas.create_image(500, 300, anchor=tk.NW, image=no_photo, tags="no")

# Event handlers for Yes button
def on_enter_yes(event):
    canvas.itemconfig(button_yes, image=yes_hover_photo)

def on_leave_yes(event):
    canvas.itemconfig(button_yes, image=yes_photo)

def on_click_yes(event):
    # Resize the 'Yes' button image and convert it to PhotoImage
    resized_yes_img = resize_img(yes_img, 0.295)  # Tạo hiệu ứng lún xuống
    yes_click_photo = ImageTk.PhotoImage(resized_yes_img)  # Chuyển đổi sang PhotoImage
    canvas.itemconfig(button_yes, image=yes_click_photo)  # Cập nhật hình ảnh
    print("I love you")  # In ra màn hình dòng chữ

    # Ghi lại hình ảnh mới để tránh mất ảnh khi gọi lại
    canvas.image = yes_click_photo

def on_release_yes(event):
    canvas.itemconfig(button_yes, image=yes_photo)  # Trở lại trạng thái ban đầu

# Event handlers for No button
def on_enter_no(event):
    move_button(event)
    canvas.itemconfig(button_no, image=no_hover_photo)

def on_leave_no(event):
    canvas.itemconfig(button_no, image=no_photo)

# Bind events for buttons on canvas
canvas.tag_bind("yes", "<Enter>", on_enter_yes)
canvas.tag_bind("yes", "<Leave>", on_leave_yes)
canvas.tag_bind("yes", "<Button-1>", on_click_yes)  # Sự kiện click chuột
canvas.tag_bind("yes", "<ButtonRelease-1>", on_release_yes)  # Khi thả chuột thì khôi phục hình ảnh ban đầu
canvas.tag_bind("no", "<Enter>", on_enter_no)
canvas.tag_bind("no", "<Leave>", on_leave_no)

root.mainloop()
