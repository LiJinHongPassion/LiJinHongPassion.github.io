import tkinter as tk
from tkinter import messagebox
import json
import os

source_file = os.path.abspath(__file__)
source_dir = os.path.dirname(source_file)

all_users = []
relations = []

with open(source_dir + '/data.json', 'r', encoding='utf8') as file:
    temp =  json.load(file)
    all_users = temp['users']
    relations = temp['relations']
    
def save_all():
    with open(source_dir + '/data.json', 'w', encoding='utf8') as file:
        all = {
            "users": all_users,
            "relations": relations
        }
        json.dump(all, file)

def update_listbox():
    # 清空用户列表框
    user_listbox.delete(0, tk.END)

    # 重新加载用户信息
    with open(source_dir + '/data.json', 'r', encoding='utf8') as file:
        temp =  json.load(file)
        all_users = temp['users']

    # 显示用户列表
    user_listbox.insert(tk.END, all_users)

def save_user_info():
    # 获取用户输入的信息
    user_info = {
        'id': entry_name.get(),
        'label': entry_name.get(),
        'name': entry_name.get(),
        'gender': entry_gender.get(),
        'field': entry_field.get(),
        'profession': entry_profession.get(),
        'birthday': entry_birthday.get(),
        'description': entry_description.get('1.0', tk.END).strip()
    }
    
    # 检查用户输入的信息是否完整
    if '' in user_info.values():
        messagebox.showwarning('警告', '请填写完整用户信息')
        return
    
    # 添加用户信息
    all_users.append(user_info)
    
    # 将用户信息保存为JSON格式
    save_all()
    # 刷新用户列表
    update_listbox()
    
    # 清空输入框
    entry_name.delete(0, tk.END)
    entry_gender.delete(0, tk.END)
    entry_field.delete(0, tk.END)
    entry_profession.delete(0, tk.END)
    entry_birthday.delete(0, tk.END)
    entry_description.delete('1.0', tk.END)
    messagebox.showinfo('提示', '用户信息保存成功')

def update_user_info():
    # 获取用户输入的姓名
    name = entry_name.get()
    
    # 查找需要更新的用户信息
    updated = False
    for user in all_users:
        if user['name'] == name:
            user['gender'] = entry_gender.get()
            user['field'] = entry_field.get()
            user['profession'] = entry_profession.get()
            user['birthday'] = entry_birthday.get()
            user['description'] = entry_description.get('1.0', tk.END).strip()
            updated = True
            break
    
    if not updated:
        messagebox.showwarning('警告', '该用户不存在')
        return
    
    # 将用户信息保存为JSON格式
    save_all()
    # 刷新用户列表
    update_listbox()
    
    # 清空输入框
    entry_name.delete(0, tk.END)
    entry_gender.delete(0, tk.END)
    entry_field.delete(0, tk.END)
    entry_profession.delete(0, tk.END)
    entry_birthday.delete(0, tk.END)
    entry_description.delete('1.0', tk.END)
    messagebox.showinfo('提示', '用户信息更新成功')

def delete_user_info():
    # 获取用户输入的姓名
    name = entry_name.get()
    
    # 删除指定姓名的用户信息
    deleted = False
    for user in all_users:
        if user['name'] == name:
            all_users.remove(user)
            deleted = True
            break
    
    if not deleted:
        messagebox.showwarning('警告', '该用户不存在')
        return
    
    # 将用户信息保存为JSON格式
    save_all()
    # 刷新用户列表
    update_listbox()
    
    # 清空输入框
    entry_name.delete(0, tk.END)
    entry_gender.delete(0, tk.END)
    entry_field.delete(0, tk.END)
    entry_profession.delete(0, tk.END)
    entry_birthday.delete(0, tk.END)
    entry_description.delete('1.0', tk.END)
    messagebox.showinfo('提示', '用户信息删除成功')

def search_user_details():
    # 获取用户输入的姓名
    name = entry_name.get()
    
    # 查找指定姓名的用户信息
    found = False
    for user in all_users:
        if user['name'] == name:
            messagebox.showinfo('用户详情', 
                f'姓名：{user["name"]}\n'
                f'性别：{user["gender"]}\n'
                f'领域：{user["field"]}\n'
                f'职业：{user["profession"]}\n'
                f'生日：{user["birthday"]}\n'
                f'描述：{user["description"]}')
            found = True
            break
    
    if not found:
        messagebox.showwarning('警告', '该用户不存在')

# 创建主窗口
window = tk.Tk()
window.title('用户信息管理系统')

# 添加姓名标签和输入框
label_name = tk.Label(window, text='姓名：')
label_name.grid(row=0, column=0, padx=10, pady=10)
entry_name = tk.Entry(window)
entry_name.grid(row=0, column=1)

# 添加性别标签和输入框
label_gender = tk.Label(window, text='性别：')
label_gender.grid(row=1, column=0, padx=10, pady=10)
entry_gender = tk.Entry(window)
entry_gender.grid(row=1, column=1)

# 添加领域标签和输入框
label_field = tk.Label(window, text='领域：')
label_field.grid(row=2, column=0, padx=10, pady=10)
entry_field = tk.Entry(window)
entry_field.grid(row=2, column=1)

# 添加职业标签和输入框
label_profession = tk.Label(window, text='职业：')
label_profession.grid(row=3, column=0, padx=10, pady=10)
entry_profession = tk.Entry(window)
entry_profession.grid(row=3, column=1)

# 添加生日标签和输入框
label_birthday = tk.Label(window, text='生日：')
label_birthday.grid(row=4, column=0, padx=10, pady=10)
entry_birthday = tk.Entry(window)
entry_birthday.grid(row=4, column=1)

# 添加描述标签和文本框
label_description = tk.Label(window, text='描述：')
label_description.grid(row=5, column=0, padx=10, pady=10)
entry_description = tk.Text(window, height=5, width=30)
entry_description.grid(row=5, column=1)

# 添加保存按钮
button_save = tk.Button(window, text='保存', command=save_user_info)
button_save.grid(row=6, column=0, padx=10, pady=20)

# 添加更新按钮
button_update = tk.Button(window, text='更新', command=update_user_info)
button_update.grid(row=6, column=1)

# 添加删除按钮
button_delete = tk.Button(window, text='删除', command=delete_user_info)
button_delete.grid(row=7, column=0)

# 添加查询详情按钮
button_search_details = tk.Button(window, text='查询详情', command=search_user_details)
button_search_details.grid(row=7, column=1)

# 创建用户列表框
frame_list = tk.Frame(window)
frame_list.grid(row=0, column=2, rowspan=8, padx=20)

# 创建滚动条
scrollbar = tk.Scrollbar(frame_list)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# 创建用户列表框
user_listbox = tk.Listbox(frame_list, yscrollcommand=scrollbar.set)
user_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.config(command=user_listbox.yview)

# 显示用户列表
for user in all_users:
    user_listbox.insert(tk.END, user)

# 当用户列表框选中项发生变化时，显示所选用户的信息
def on_select(event):
    selected_index = user_listbox.curselection()
    if selected_index:
        selected_user = all_users[selected_index[0]]
        entry_name.delete(0, tk.END)
        entry_name.insert(tk.END, selected_user['name'])
        entry_gender.delete(0, tk.END)
        entry_gender.insert(tk.END, selected_user['gender'])
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, selected_user['field'])
        entry_profession.delete(0, tk.END)
        entry_profession.insert(tk.END, selected_user['profession'])
        entry_birthday.delete(0, tk.END)
        entry_birthday.insert(tk.END, selected_user['birthday'])
        entry_description.delete('1.0', tk.END)
        entry_description.insert(tk.END, selected_user['description'])

user_listbox.bind('<<ListboxSelect>>', on_select)

# 启动主循环
window.mainloop()
