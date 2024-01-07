import tkinter as tk
from tkinter import messagebox
import json
import os

source_file = os.path.abspath(__file__)
source_dir = os.path.dirname(source_file)

class UserManagementApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("User Management")
        
        self.users = []
        self.relations = []
        self.selected_relation = None
        
        self.create_widgets()
        self.load_data()
        self.update_user_list()
        self.update_relation_list()
    
    def create_widgets(self):
        self.user_listbox = tk.Listbox(self.root)
        self.user_listbox.pack(side=tk.LEFT, padx=10, pady=10)
        self.user_listbox.bind('<<ListboxSelect>>', self.select_user)
        
        self.relation_name_label = tk.Label(self.root, text="Relation Name:")
        self.relation_name_label.pack(padx=10, pady=10)
        self.relation_name_entry = tk.Entry(self.root)
        self.relation_name_entry.pack(padx=10, pady=10)
        
        self.checkbox_var = tk.BooleanVar()
        self.checkbox = tk.Checkbutton(self.root, text="Selected", variable=self.checkbox_var)
        self.checkbox.pack(padx=10, pady=10)
        
        self.refresh_button = tk.Button(self.root, text="Refresh", command=self.refresh_relations)
        self.refresh_button.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.save_button = tk.Button(self.root, text="Save", command=self.save_data)
        self.save_button.pack(side=tk.LEFT, padx=10, pady=10)
        
    def load_data(self):
        try:
            with open(source_dir + "/data.json", "r", encoding='utf8') as file:
                data = json.load(file)
                self.users = data['users']
                self.relations = data['relations']
        except FileNotFoundError:
            pass
    
    def update_user_list(self):
        self.user_listbox.delete(0, tk.END)
        for user in self.users:
            self.user_listbox.insert(tk.END, user)
    
    def select_user(self, event=None):
        selected_index = self.user_listbox.curselection()
        if selected_index:
            user_name = self.user_listbox.get(selected_index)
            self.selected_user = str(user_name).split()
            
            for relation in self.relations:
                if relation['from'] == self.selected_user[0] and relation['to'] == self.selected_user[2]:   
                    if 'label' in relation:
                        self.relation_name_entry.insert('0', relation['label'])  
                    if 'selected' in relation:
                        self.checkbox_var.set(relation['selected'])
                    break
                else:
                    self.clear_relation_details()
        
    def save_data(self):
        relation_name = self.relation_name_entry.get()
        relation_selected = self.checkbox_var.get()
        if not self.selected_user:
            messagebox.showerror("Error", "Please select a user")
            return
        
        user_name = self.selected_user
        
        
        for relation in self.relations:
            if relation['from'] == user_name[0] and relation['to'] == user_name[2]:
                relation['label'] = relation_name
                relation['selected'] = relation_selected
                break
        
        # new_relation = {
        #     'from': user_name[0],
        #     'to': user_name[1],
        #     'selected': relation_selected,
        #     'name': relation_name
        # }
        
        # self.relations.append(new_relation)
        self.clear_relation_details()
        
        # 将数据写回到JSON文件
        data = {
            'users': self.users,
            'relations': self.relations
        }
        with open(source_dir + "/data.json", "w", encoding='utf8') as file:
            json.dump(data, file)
        
        messagebox.showinfo("User Management", "Relation added successfully.")

    
    def get_user_by_name(self, user_name):
        for user in self.users:
            if user == user_name:
                return user
        return None
    
    def refresh_relations(self):
        self.relations = []
        users_count = len(self.users)
        if users_count >= 2:
            for i in range(users_count-1):
                for j in range(i+1, users_count):
                    user1_name = self.users[i]['name']
                    user2_name = self.users[j]['name']
                    name = f"{user1_name} - {user2_name}"
                    relation_selected = False
                    new_relation = {
                        'from': user1_name,
                        'to': user2_name,
                        'arrows': 'to',
                        'name': name,
                        'selected': relation_selected
                    }
                    self.relations.append(new_relation)
        
        self.update_relation_list()
    
    def update_relation_list(self):
        self.user_listbox.delete(0, tk.END)
        for relation in self.relations:
            self.user_listbox.insert(tk.END, relation['name'])
        
    def clear_relation_details(self):
        self.relation_name_entry.delete(0, tk.END)
        self.checkbox_var.set(False)

app = UserManagementApp()
app.root.mainloop()
