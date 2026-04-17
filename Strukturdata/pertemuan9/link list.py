#membuat single linked list (SLL) dengan python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None

    def tambah_belakang(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        print("node baru ditambahkan sebagai head.")
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        print("node baru ditambahkan di belakang.")

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

    def hapus_depan(self):
        if self.head is None:
            print("Linked list kosong, tidak ada node untuk dihapus.")
            return
        print(f"Node dengan data {self.head.data} dihapus dari depan.")
        self.head = self.head.next

    def hapus_belakang(self, data):
        if self.head is None:
            print("Linked list kosong, tidak ada node untuk dihapus.")
            return
        if self.head.data == data:
            print(f"Node dengan data {data} dihapus dari belakang.")
            self.head = self.head.next
            return
        current_node = self.head
        while current_node.next and current_node.next.data != data:
            current_node = current_node.next
        if current_node.next is None:
            print(f"Node dengan data {data} tidak ditemukan.")
            return
        print(f"Node dengan data {data} dihapus dari belakang.")
        current_node.next = current_node.next.next

# Contoh penggunaan
linked_list = LinkedList()
linked_list.tambah_belakang(10)
linked_list.tambah_belakang(20)
linked_list.tambah_belakang(30)
linked_list.hapus_depan()
linked_list.hapus_belakang(10)
linked_list.display()
