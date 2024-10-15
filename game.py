import os 
import time
# Dictionary
rooms = {
    'Lobby': {'east': 'Pharmacy', 'south': 'Bathroom', 'west': 'Exam Room 1', 'north': 'Kennel', 'item': 'apple'},
    'Exam Room 1': {'east': 'Lobby', 'item': 'stethoscope'},
    'Kennel': {'east': 'Final Boss Room', 'south': 'Lobby', 'item': 'blanket'},
    'Final Boss Room': {},
    'Pharmacy': {'west': 'Lobby', 'north': 'Treatment Area', 'item': 'medicine'},
    'Treatment Area': {'south': 'Pharmacy', 'item': 'dog'},
    'Bathroom': {'north': 'Lobby', 'east': 'Kitchen', 'item': 'cleaning supplies'},
    'Kitchen': {'west': 'Bathroom', 'item': 'Food'}
}

#Sistema de comandos para que el usuario pueda moverse entre salas
#usuario inicia en "lobby"
current_room = 'Lobby'
# Array
user_inventory = []
# El usuario debe poder recorrer todas las salas en una sola ejecución
while True:
    os.system('clear')
    print(f"This is your current inventory {user_inventory}")
    print(f"You're right now in the {current_room}")
    print(rooms[current_room])
    # Si la habitación tiene un objeto permitir obtener el item 
    if "item" in rooms[current_room]:
        print(f"In this room we can find an item, write 'grab' to obtain it")
    next_direction = input('Input the next direction you want to go to: ')
    # Mecanica de movimiento
    if next_direction in rooms[current_room]:
        current_room = rooms[current_room][next_direction]
        # Manejo de excepciones
    try:
        if next_direction == 'grab':
            # El elemento tiene que ser removido de la lista despues de obtenido
            user_inventory.append(rooms[current_room]['item'])
            print(f"You have added an item to your inventory: {user_inventory}")
            del rooms[current_room]['item']
    except:
        print('This room has no items anymore')
        time.sleep(2)
    
    # Se gana la partida al haber obtenido todos los items de las distintas salas
    if current_room == 'Final Boss Room' and 7 == len(user_inventory):   
        print("Win")
        break
    elif current_room == 'Final Boss Room' and 7 != len(user_inventory):
        print("Womp Womp")
        break
        
    if next_direction == 'exit':
        break
    