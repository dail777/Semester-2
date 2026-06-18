"""Sistem Antrian Tiket yang mengintegrasikan Queue dan JSON database.
Graph telah dihapus — antrian hanya menggunakan struktur Queue.
"""

import os
import threading
from datetime import datetime
from typing import Any, Dict, List, Optional
from queue_ticket import Queue
from db_manager import DatabaseManager


class TiketOrder:
    """Representasi pesanan tiket"""
    
    def __init__(
        self,
        ticket_number: int,
        username: str,
        name: str,
        category: str,
        price: int,
        lokasi_x: int,
        lokasi_y: int,
        purchase_time: str,
        status: str = "Menunggu",
        served_by: str = "",
        served_time: str = ""
    ):
        self.ticket_number = ticket_number
        self.username = username
        self.name = name
        self.category = category
        self.price = price
        self.lokasi_x = lokasi_x
        self.lokasi_y = lokasi_y
        self.purchase_time = purchase_time
        self.status = status
        self.served_by = served_by
        self.served_time = served_time
    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            ticket_number=data.get("ticket_number"),
            username=data.get("username", ""),
            name=data.get("name", ""),
            category=data.get("category", "Reguler"),
            price=data.get("price", 0),
            lokasi_x=data.get("lokasi_x", 50),
            lokasi_y=data.get("lokasi_y", 50),
            purchase_time=data.get("purchase_time", datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
            status=data.get("status", "Menunggu"),
            served_by=data.get("served_by", ""),
            served_time=data.get("served_time", "")
        )
    
    def to_dict(self) -> dict:
        return {
            "ticket_number": self.ticket_number,
            "username": self.username,
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "lokasi_x": self.lokasi_x,
            "lokasi_y": self.lokasi_y,
            "purchase_time": self.purchase_time,
            "status": self.status,
            "served_by": self.served_by,
            "served_time": self.served_time
        }
    
    def __repr__(self):
        return f"TiketOrder({self.ticket_number}, {self.username}, {self.category}, {self.status})"


class SistemAntrian:
    """Sistem Antrian Tiket menggunakan Queue dan Database.

    Kebijakan baru:
    - Jika antrian > 2, antrian depan otomatis diterima (dilayani) sekali.
    - Antrian belakang (posisi > 2) otomatis ditolak dalam 30 detik jika masih menunggu.
    """

    def __init__(self, pusat_x=50, pusat_y=50):
        self.db = DatabaseManager()
        self.antrian = Queue()
        self.timers: Dict[int, threading.Timer] = {}
        self.lock = threading.RLock()  # RLock untuk support nested locking
        self._load_pending_orders()
    
    def _get_next_ticket_number(self) -> int:
        orders = self.db.get_all_orders()
        if not orders:
            return 1000
        return max(order["ticket_number"] for order in orders) + 1
    
    def _normalize_username(self, username: str) -> str:
        return username.strip() if isinstance(username, str) else username
    
    def _load_pending_orders(self):
        pending_orders = self.db.get_orders(status="Menunggu")
        for order_data in pending_orders:
            order = TiketOrder.from_dict(order_data)
            self.antrian.enqueue(order)

        self._apply_rejects_for_queue()

    def _cancel_all_timers(self):
        for ticket_number in list(self.timers.keys()):
            self._cancel_timer(ticket_number)

    def reload_data(self):
        self._cancel_all_timers()
        self.db = DatabaseManager()
        self.antrian = Queue()
        self.timers = {}
        self._load_pending_orders()
    
    def authenticate(self, username: str, password: str) -> Optional[str]:
        return self.db.authenticate(username, password)
    
    def register_user(self, username: str, password: str, name: str, saldo: int = 0) -> bool:
        return self.db.register_user(username, password, name, saldo)
    
    def get_user_info(self, username: str) -> Optional[dict]:
        self.reload_data()
        username = self._normalize_username(username)
        return self.db.get_user(username)

    def get_user_chat(self, username: str) -> Optional[Dict[str, Any]]:
        username = self._normalize_username(username)
        chats = self.db.get_chats(username=username)
        return chats[-1] if chats else None

    def send_user_message(self, username: str, text: str) -> Optional[Dict[str, Any]]:
        username = self._normalize_username(username)
        user = self.db.get_user(username)
        if not user or not text.strip():
            return None
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        existing_chat = self.get_user_chat(username)
        message = {"sender": username, "text": text.strip(), "timestamp": now}
        if existing_chat:
            self.db.add_chat_message(existing_chat["chat_id"], message)
            self.db.update_chat(existing_chat["chat_id"], status="Menunggu", updated_at=now)
            chat = existing_chat
        else:
            chat_id = self._get_next_chat_id()
            chat = {
                "chat_id": chat_id,
                "username": username,
                "created_at": now,
                "updated_at": now,
                "status": "Menunggu",
                "messages": [message]
            }
            self.db.add_chat(chat)
        self.db.save()
        return chat

    def send_admin_message(self, chat_id: int, text: str) -> Optional[Dict[str, Any]]:
        if not text.strip():
            return None
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = {"sender": "admin", "text": text.strip(), "timestamp": now}
        if self.db.add_chat_message(chat_id, message):
            self.db.update_chat(chat_id, status="Ditanggapi", updated_at=now)
            return self.db.get_chat(chat_id)
        return None

    def _get_next_chat_id(self) -> int:
        chats = self.db.get_all_chats()
        if not chats:
            return 1
        return max(chat["chat_id"] for chat in chats) + 1

    def get_chat_queue_position(self, chat_id: int) -> Optional[int]:
        pending = self.db.get_chats(status="Menunggu")
        for idx, chat in enumerate(pending, 1):
            if chat["chat_id"] == chat_id:
                return idx
        return None

    def get_admin_chats(self) -> List[Dict[str, Any]]:
        return self.db.get_all_chats()

    def get_chat_by_id(self, chat_id: int) -> Optional[Dict[str, Any]]:
        return self.db.get_chat(chat_id)

    def get_pending_chat_count(self) -> int:
        return len(self.db.get_chats(status="Menunggu"))

    def update_user_name(self, username: str, new_name: str) -> bool:
        username = self._normalize_username(username)
        result = self.db.update_user(username, name=new_name)
        if result:
            for order in self.db.get_orders(username=username):
                order["name"] = new_name
            self.db.save()
        return result
    
    def delete_user(self, username: str) -> bool:
        username = self._normalize_username(username)
        return self.db.delete_user(username)
    
    def top_up_balance(self, username: str, amount: int) -> bool:
        username = self._normalize_username(username)
        user = self.db.get_user(username)
        if not user or amount <= 0:
            return False
        user["saldo"] += amount
        self.db.save()
        return True
    
    def set_user_location(self, username: str, lokasi_x: int, lokasi_y: int) -> bool:
        username = self._normalize_username(username)
        return self.db.update_user(username, location_x=lokasi_x, location_y=lokasi_y)
    
    def get_categories(self) -> List[Dict[str, Any]]:
        self.reload_data()
        return self.db.get_categories()
    
    def add_category(self, name: str, price: int) -> bool:
        return self.db.add_category(name, price)
    
    def update_category_price(self, name: str, price: int) -> bool:
        return self.db.update_category(name, price)
    
    def purchase_ticket(self, username: str, category_name: str, lokasi_x: int = 0, lokasi_y: int = 0) -> Optional[TiketOrder]:
        username = self._normalize_username(username)
        user = self.db.get_user(username)
        if not user:
            return None
        category = next((cat for cat in self.db.get_categories() if cat["name"] == category_name), None)
        if not category:
            return None
        if user["saldo"] < category["price"]:
            return None
        ticket_number = self._get_next_ticket_number()
        purchase_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        order = TiketOrder(
            ticket_number=ticket_number,
            username=username,
            name=user["name"],
            category=category_name,
            price=category["price"],
            lokasi_x=lokasi_x,
            lokasi_y=lokasi_y,
            purchase_time=purchase_time,
            status="Menunggu"
        )
        user["saldo"] -= category["price"]
        self.db.add_order(order.to_dict())
        self.db.save()
        self.antrian.enqueue(order)

        self._apply_rejects_for_queue()

        return order
    
    def get_pending_orders(self) -> List[TiketOrder]:
        self.reload_data()
        return self.antrian.get_all_queue()
    
    def get_next_order(self) -> Optional[TiketOrder]:
        self.reload_data()
        return self.antrian.peek()
    
    def serve_next_order(self, admin_username: str) -> Optional[TiketOrder]:
        with self.lock:
            order = self.antrian.dequeue()
            if not order:
                return None
            # cancel any timer
            self._cancel_timer(order.ticket_number)
            order.status = "Selesai"
            order.served_by = admin_username
            order.served_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.db.update_order(order.ticket_number, status="Selesai", served_by=admin_username, served_time=order.served_time)

            # after serving, ensure back items have timers if needed
            self._apply_rejects_for_queue()
            return order

    def reject_order(self, ticket_number: int, admin_username: str = "admin") -> Optional[TiketOrder]:
        with self.lock:
            order = self.db.get_order(ticket_number)
            if not order or order.get("status") != "Menunggu":
                return None
            # remove from queue if present
            removed = self.antrian.remove_by_ticket(ticket_number)
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.db.update_order(ticket_number, status="Dibatalkan", cancelled_by=admin_username, cancelled_time=now)
            self._cancel_timer(ticket_number)
            # re-evaluate queue timers
            self._apply_rejects_for_queue()
            return self.db.get_order(ticket_number)

    def get_order_history(self, username: Optional[str] = None) -> List[Dict[str, Any]]:
        self.reload_data()
        username = self._normalize_username(username) if username is not None else None
        return self.db.get_orders(username=username)
    
    def get_admin_purchase_history(self) -> List[Dict[str, Any]]:
        self.reload_data()
        return [self._annotate_order(order) for order in self.db.get_all_orders()]
    
    def get_purchase_statistics_by_date(self) -> List[Dict[str, Any]]:
        self.reload_data()
        stats = self.db.get_purchase_stats_by_date()
        return [
            {
                "date": item["date"],
                "count": item["count"],
                "cancelled": item.get("cancelled", 0),
                "completed": item.get("completed", 0),
                "waiting": item.get("waiting", 0),
            }
            for item in stats
        ]

    def get_user_purchase_history(self, username: str) -> List[Dict[str, Any]]:
        self.reload_data()
        username = self._normalize_username(username)
        return [self._annotate_order(order) for order in self.db.get_orders(username=username)]
    
    def get_user_balance(self, username: str) -> int:
        username = self._normalize_username(username)
        user = self.db.get_user(username)
        return user["saldo"] if user else 0
    
    def get_user_location(self, username: str) -> Optional[tuple]:
        username = self._normalize_username(username)
        user = self.db.get_user(username)
        if not user:
            return None
        return (user["location_x"], user["location_y"])
    
    def get_queue_position(self, ticket_number: int) -> Optional[int]:
        pending = self.antrian.get_all_queue()
        for idx, order in enumerate(pending, 1):
            if order.ticket_number == ticket_number:
                return idx
        return None

    def _annotate_order(self, order_data: Dict[str, Any]) -> Dict[str, Any]:
        annotated = dict(order_data)
        if annotated["status"] == "Menunggu":
            position = self.get_queue_position(annotated["ticket_number"])
            annotated["queue_position"] = position
            annotated["status_label"] = "Diproses" if position == 1 else "Menunggu"
        else:
            annotated["queue_position"] = None
            annotated["status_label"] = annotated["status"]
        return annotated
    
    def get_prioritas_berdasarkan_lokasi(self) -> List[Dict[str, Any]]:
        # Graph functionality removed — return empty list
        return []
    
    def get_pembeli_terdekat(self, top_n: int = 5) -> List[Dict[str, Any]]:
        return []
    
    def get_statistik(self) -> dict:
        total_orders = len(self.db.get_all_orders())
        waiting = len(self.db.get_orders(status="Menunggu"))
        completed = len(self.db.get_orders(status="Selesai"))
        cancelled = len(self.db.get_orders(status="Dibatalkan"))
        total_revenue = sum(order["price"] for order in self.db.get_all_orders() if order["status"] != "Dibatalkan")
        percentage_completed = (completed / total_orders * 100) if total_orders else 0
        return {
            "total_orders": total_orders,
            "total_pembeli": total_orders,
            "menunggu": waiting,
            "selesai": completed,
            "cancelled": cancelled,
            "pending": waiting,
            "completed": completed,
            "revenue": total_revenue,
            "completion_rate": percentage_completed,
            "persentase_selesai": percentage_completed
        }
    
    def reset(self):
        self._cancel_all_timers()
        self.db = DatabaseManager()
        self.antrian = Queue()
        self.timers = {}
        self._load_pending_orders()

    # ------- Queue policy helpers -------
    def _schedule_reject(self, ticket_number: int, delay: int = 30):
        if ticket_number in self.timers:
            return

        timer = threading.Timer(delay, self._auto_reject, args=(ticket_number,))
        self.timers[ticket_number] = timer
        timer.daemon = True
        timer.start()

    def _cancel_timer(self, ticket_number: int):
        t = self.timers.pop(ticket_number, None)
        if t:
            try:
                t.cancel()
            except Exception:
                pass

    def _auto_reject(self, ticket_number: int):
        with self.lock:
            order = self.db.get_order(ticket_number)
            if not order or order.get("status") != "Menunggu":
                self._cancel_timer(ticket_number)
                return
            # ensure the order is still at position > 2
            pos = self.antrian.get_position_by_ticket(ticket_number)
            if pos is None or pos <= 2:
                self._cancel_timer(ticket_number)
                return
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.db.update_order(ticket_number, status="Dibatalkan", cancelled_by="system", cancelled_time=now)
            self.antrian.remove_by_ticket(ticket_number)
            self._cancel_timer(ticket_number)
            # after rejecting, re-apply timers for remaining back items
            self._apply_rejects_for_queue()

    def _apply_rejects_for_queue(self):
        # ensure items at positions >2 have timers; cancel timers for items at positions <=2
        all_q = self.antrian.get_all_queue()
        for idx, o in enumerate(all_q, 1):
            if idx > 2:
                if o.ticket_number not in self.timers:
                    self._schedule_reject(o.ticket_number)
            else:
                # cancel timers for front two
                if o.ticket_number in self.timers:
                    self._cancel_timer(o.ticket_number)

    def _on_enqueue(self):
        # Called after enqueueing a new order. Schedule rejects for items at position > 2
        with self.lock:
            # Just apply queue policy - don't auto-serve, let items stay in queue
            self._apply_rejects_for_queue()

    def reset_history(self) -> bool:
        self.db.reset_orders()
        self.reload_data()
        return True

    def reset_chats(self) -> bool:
        self.db.reset_chats()
        self.reload_data()
        return True
