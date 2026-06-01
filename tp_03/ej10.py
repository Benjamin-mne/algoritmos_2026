# Consigna: Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone,
# de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje,
# resolver las siguientes actividades:
#   a. escribir una función que elimine de la cola todas las notificaciones de Facebook;
#   b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya
#   la palabra ‘Python’, si perder datos en la cola;
#   c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las
#   11:43 y las 15:57, y determinar cuántas son.

import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

from common.Queue import Queue
from common.Stack import Stack

# =================================================================
class Notification: 
    def __init__(self, hour: str, app: str, msg: str): 
        self.hour = hour
        self.app = app
        self.msg = msg

notificationsData = [
    Notification("13:00", "Facebook", "Tia Paola subió una foto."),
    Notification("14:00", "Twitter", "Manuelito subió tutorial de Python"),
    Notification("21:00", "X", "Elon Musk se casó con una IA")
]

notifications = Queue() 

for i in range(len(notificationsData)):
    notifications.arrive(notificationsData[i])

# =================================================================

def iterateQueue(q: Queue, callback): 
    aux_queue = Queue() 

    for _ in range(q.size()):
        current = q.attention()
        
        # El callback decide si el elemento se queda o se va
        keep_element = callback(current)

        if keep_element:
            aux_queue.arrive(current)

    # Reintegrar elementos a la cola original
    for _ in range(aux_queue.size()):
        q.arrive(aux_queue.attention())


def deleteFacebookNotifications(notification: Notification):
    return notification.app != "Facebook"

def showPythonNotifications(notification: Notification): 

    if ("Python" in notification.msg) and ("Twitter" == notification.app):
        print(notification.msg)
    
    return True


# --- Alternativa a punto C sin usar Pila --- 
# def countNotificationsInInterval(notification: Notification, counter_list: list, a: str = "11:43", b: str = "15:57"):
#    if a <= notification.hour <= b:
#        counter_list[0] += 1
#    return True

# --- PRUEBA PUNTO C ---
# notifications_count = [0] 
# iterateQueue(notifications, lambda n: countNotificationsInInterval(n, notifications_count))
# print(f"\nCantidad de notificaciones entre las 11:43 y las 15:57: {notifications_count[0]}")

def getNotificationsInTimeInterval(q: Queue, a: str = "11:43", b: str = "15:57") -> int:
    pila_temporal = Stack()
    cola_aux = Queue()
    
    for _ in range(q.size()):
        current = q.attention()
        
        if a <= current.hour <= b:
            pila_temporal.push(current)
            
        cola_aux.arrive(current)
        
    cantidad = pila_temporal.size()
    
    for _ in range(cola_aux.size()):
        q.arrive(cola_aux.attention())
        
    return cantidad


# =================================================================

# --- PRUEBA PUNTO C ---
print("\n--- Cantidad de notificaciones en el intervalo (11:43 - 15:57) ---")
print(f"Cantidad: {getNotificationsInTimeInterval(notifications)}")

# --- PRUEBA PUNTO B ---
print("\n--- Notificaciones de Twitter con 'Python' ---")
iterateQueue(notifications, showPythonNotifications)

# --- PRUEBA PUNTO A ---
print("\n--- Eliminando notificaciones de Facebook ---")
iterateQueue(notifications, deleteFacebookNotifications)

