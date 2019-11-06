# tkinterを用いたGUI

import tkinter as tk
import sekigae


# ルート画面のインスタンス生成
root = tk.Tk()

# タイトルの設定
root.title("Hello World")
# 画面サイズの設定
root.geometry("400x400")
# ラベルの作成
left_table = tk.Label(root, text=sekigae.member_list[:4], borderwidth=2, relief="solid")
left_table.pack(side='left')
right_table = tk.Label(root, text=sekigae.member_list[4:8], borderwidth=2, relief="solid")
right_table.pack(side='right')
bottom_table = tk.Label(root, text=sekigae.member_list[8:], borderwidth=2, relief="solid")
bottom_table.pack(side= "bottom")

print(sekigae.member_list[8:])
# メインループの開始：ウィンドウが動き出す
root.mainloop()

root.title("Hello World")

root.mainloop()
