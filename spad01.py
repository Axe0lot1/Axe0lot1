
#imports
from re import A
import tkinter as tk
import time
import math

# komentar

#w=tk.Tk
#c=tk.Canvas(w, height=1500, width=900, bg="#fff")
#c.pack


def slobodan_pad(x0, v0y, vx):
    tt = 0
    i = 0
    a = 0.4
    vy = v0y
    tf = 2 * v0y / a
    yp = 0
    while tt < tf :
        tt = 0.04 * i
        x = x0 + vx * tt
        y = yp + v0y * tt - a*tt*tt/2 
        print(f"x = {x:{0}.{5}}, y = {y:{0}.{5}}, vy = {vy}, tf = {tf}, tt = {tt}") 
        i = i + 1   
        if y < 0 :
            break
#        time.sleep(0.04)

slobodan_pad(5, 20, 8)

