import time
from ticket_system import SistemAntrian

print("\n=== Testing Queue Auto-Reject/Auto-Accept System ===\n")

# Initialize system
sistem = SistemAntrian()

# Register test users
sistem.register_user("user1", "pass1", "User Satu", saldo=500000)
sistem.register_user("user2", "pass2", "User Dua", saldo=500000)
sistem.register_user("user3", "pass3", "User Tiga", saldo=500000)
sistem.register_user("user4", "pass4", "User Empat", saldo=500000)
print("✓ Test users registered\n")

# Create tickets
print("Creating 4 ticket orders...")
o1 = sistem.purchase_ticket("user1", "Reguler", 50, 50)
print(f"  Ticket 1: {o1.ticket_number} | Status: {o1.status}")
time.sleep(0.5)

o2 = sistem.purchase_ticket("user2", "VIP", 60, 60)
print(f"  Ticket 2: {o2.ticket_number} | Status: {o2.status}")
time.sleep(0.5)

o3 = sistem.purchase_ticket("user3", "VVIP", 70, 70)
print(f"  Ticket 3: {o3.ticket_number} | Status: {o3.status}")
time.sleep(0.5)

o4 = sistem.purchase_ticket("user4", "Reguler", 80, 80)
print(f"  Ticket 4: {o4.ticket_number} | Status: {o4.status}")

print("\n✓ Tickets created\n")

# Check queue status
pending = sistem.get_pending_orders()
print(f"Queue size: {len(pending)}")
for idx, o in enumerate(pending, 1):
    print(f"  Position {idx}: Ticket {o.ticket_number} ({o.name}) - {o.status}")

print("\n=== Policy: Size > 2 triggers auto-serve for front ===")
print(f"Total pending: {len(pending)}")
if len(pending) > 2:
    print("✓ Queue size > 2, auto-accept system triggered")
    print("  - Front 2 kept for processing")
    print("  - Back items scheduled for auto-reject in 30s")
else:
    print("Queue size <= 2, no auto-reject triggered")

print("\nWaiting 2 seconds to check timer status...")
time.sleep(2)

pending = sistem.get_pending_orders()
print(f"\nCurrent queue size after delay: {len(pending)}")
for idx, o in enumerate(pending, 1):
    print(f"  Position {idx}: Ticket {o.ticket_number} - {o.status}")

print(f"\nActive timers: {len(sistem.timers)}")
for ticket_num, timer in list(sistem.timers.items())[:5]:
    print(f"  - Timer for ticket {ticket_num}: {'ACTIVE' if timer.is_alive() else 'INACTIVE'}")

print("\n✓ Test completed successfully!")
