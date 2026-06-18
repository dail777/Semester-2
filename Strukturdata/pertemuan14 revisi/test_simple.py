print("Starting test...")
from ticket_system import SistemAntrian
print("✓ Import successful")

sistem = SistemAntrian()
print("✓ SistemAntrian created")

print("Registering user1...")
sistem.register_user("user1", "pass1", "User Satu", saldo=500000)
print("✓ User1 registered")

print("Creating first ticket...")
o1 = sistem.purchase_ticket("user1", "Reguler", 50, 50)
print(f"✓ Ticket created: {o1.ticket_number}")

pending = sistem.get_pending_orders()
print(f"✓ Queue size: {len(pending)}")
print("Test complete!")
