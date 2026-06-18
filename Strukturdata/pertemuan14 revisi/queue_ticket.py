"""
Queue implementation untuk sistem antrian tiket
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    """
    Implementasi Queue menggunakan Linked List
    untuk sistem antrian tiket
    """
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def enqueue(self, data):
        """Tambahkan pembeli ke dalam antrian"""
        new_node = Node(data)
        
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.size += 1

    def enqueue_sorted(self, data, key):
        """Tambahkan pembeli ke dalam antrian berdasarkan prioritas."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return

        insertion_value = key(data)
        current = self.head
        previous = None
        while current is not None and key(current.data) <= insertion_value:
            previous = current
            current = current.next

        if previous is None:
            new_node.next = self.head
            self.head = new_node
        else:
            previous.next = new_node
            new_node.next = current
            if current is None:
                self.tail = new_node
        self.size += 1
    
    def dequeue(self):
        """Keluarkan pembeli dari antrian"""
        if self.head is None:
            return None
        
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        
        if self.head is None:
            self.tail = None
        
        return data
    
    def peek(self):
        """Lihat data pembeli paling depan tanpa mengeluarkannya"""
        if self.head is None:
            return None
        return self.head.data
    
    def is_empty(self):
        """Cek apakah antrian kosong"""
        return self.size == 0
    
    def get_size(self):
        """Dapatkan jumlah pembeli dalam antrian"""
        return self.size
    
    def get_all_queue(self):
        """Dapatkan semua data pembeli dalam antrian"""
        queue_list = []
        current = self.head
        
        while current is not None:
            queue_list.append(current.data)
            current = current.next
        
        return queue_list
    
    def clear(self):
        """Kosongkan antrian"""
        self.head = None
        self.tail = None
        self.size = 0
    
    def __str__(self):
        """String representation dari queue"""
        if self.is_empty():
            return "Queue kosong"
        
        result = "Antrian: "
        current = self.head
        items = []
        
        while current is not None:
            items.append(str(current.data))
            current = current.next
        
        return result + " -> ".join(items)

    def remove_by_ticket(self, ticket_number):
        """Hapus node dari antrian berdasarkan ticket_number. Return data jika ditemukan."""
        current = self.head
        previous = None
        while current is not None:
            data = current.data
            if hasattr(data, 'ticket_number') and data.ticket_number == ticket_number:
                # remove node
                if previous is None:
                    # removing head
                    self.head = current.next
                else:
                    previous.next = current.next

                if current.next is None:
                    # removing tail
                    self.tail = previous

                self.size -= 1
                return data
            previous = current
            current = current.next
        return None

    def get_position_by_ticket(self, ticket_number):
        """Dapatkan posisi (1-based) dari ticket_number di antrian, atau None jika tidak ada."""
        idx = 1
        current = self.head
        while current is not None:
            data = current.data
            if hasattr(data, 'ticket_number') and data.ticket_number == ticket_number:
                return idx
            idx += 1
            current = current.next
        return None
