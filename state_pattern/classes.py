from __future__ import annotations
from abc import ABCMeta, abstractmethod


class DoorState(metaclass=ABCMeta):
    @abstractmethod
    def open_door(self):
        pass

    @abstractmethod
    def close_door(self):
        pass

    @abstractmethod
    def lock_door(self, key: int):
        pass

    @abstractmethod
    def unlock_door(self, key: int):
        pass


class DoorOpened(DoorState):

    def __init__(self, door: Door):
        self._door = door

    def open_door(self):
        print("You can't open door 2 times")

    def close_door(self):
        print('Closing door')
        self._door.set_door_state(self._door.get_closed_door_state())

    def lock_door(self, key: int):
        print("You can't lock door that's is opened")

    def unlock_door(self, key: int):
        print("You cant' unlock opened door")


class DoorClosed(DoorState):
    def __init__(self, door: Door):
        self._door = door

    def open_door(self):
        print('Door is opening')
        self._door.set_door_state(self._door.get_opened_door_state())

    def close_door(self):
        print("You can't close door 2 times")

    def lock_door(self, key: int):
        if key == 10:
            print("Correct key, locking the door")
            self._door.correct_key_entered = True
            self._door.set_door_state(self._door.get_locked_door_state())
        else:
            self._door.correct_key_entered = False
            print("Wrong key was entered (hint : 10)")

    def unlock_door(self, key: int):
        print('Door is already unlocked')


class DoorLocked(DoorState):
    def __init__(self, door: Door):
        self._door = door

    def open_door(self):
        print('Unlock door first')

    def close_door(self):
        print('Door is already closed')

    def lock_door(self, key: int):
        print('Door is already locked')

    def unlock_door(self, key: int):
        if key == 10:
            print("Correct key, unlocking the door")
            self._door.correct_key_entered = True
            self._door.set_door_state(self._door.get_unlocked_door_state())
        else:
            self._door.correct_key_entered = False
            print("Wrong key was entered (hint : 10)")
        print('Unlocking  the door')


class DoorUnlocked(DoorState):
    def __init__(self, door: Door):
        self._door = door

    def open_door(self):
        print('Opening the door')
        self._door.set_door_state(self._door.get_opened_door_state())

    def close_door(self):
        print('Door is closed now')

    def lock_door(self, key: int):
        if key == 10:
            print("Correct key, locking the door")
            self._door.correct_key_entered = True
            self._door.set_door_state(self._door.get_locked_door_state())
        else:
            self._door.correct_key_entered = False
            print("Wrong key was entered (hint : 10)")

    def unlock_door(self, key: int):
        print('door is already unlocked')


class Door:
    correct_key_entered = False

    def __init__(self):
        self._door_opened = DoorOpened(self)
        self._door_closed = DoorClosed(self)
        self._door_locked = DoorLocked(self)
        self._door_unlocked = DoorUnlocked(self)
        self._door_state = self._door_opened

    def set_door_state(self, new_state: DoorState):
        self._door_state = new_state

    def open_door(self):
        self._door_state.open_door()

    def close_door(self):
        self._door_state.close_door()

    def lock_door(self, key: int):
        self._door_state.lock_door(key)

    def unlock_door(self, key: int):
        self._door_state.unlock_door(key)

    def get_opened_door_state(self):
        return self._door_opened

    def get_closed_door_state(self):
        return self._door_closed

    def get_locked_door_state(self):
        return self._door_locked

    def get_unlocked_door_state(self):
        return self._door_unlocked
