class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
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
        new_node.prev = last_node
        print("node baru ditambahkan di belakang.")

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" <-> ")
            current_node = current_node.next
        print("None")

    def hapus_depan(self):
        if self.head is None:
            print("Doubly linked list kosong, tidak ada node untuk dihapus.")
            return
        print(f"Node dengan data {self.head.data} dihapus dari depan.")
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    def hapus_belakang(self, data):
        if self.head is None:
            print("Doubly linked list kosong, tidak ada node untuk dihapus.")
            return
        if self.head.data == data:
            print(f"Node dengan data {data} dihapus dari belakang.")
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return
        current_node = self.head
        while current_node.next and current_node.next.data != data:
            current_node = current_node.next
        if current_node.next is None:
            print(f"Node dengan data {data} tidak ditemukan.")
            return
        print(f"Node dengan data {data} dihapus dari belakang.")
        to_delete = current_node.next
        current_node.next = to_delete.next
        if to_delete.next:
            to_delete.next.prev = current_node

# Contoh penggunaan
dll = DoublyLinkedList()
dll.tambah_belakang(10)
dll.tambah_belakang(20)
dll.tambah_belakang(30)
dll.display()
dll.hapus_depan()
dll.display()
dll.hapus_belakang(20)
dll.display()
