from GameFrame import RoomObject
import pygame

class Title(RoomObject):
    """
    The object for displaying the title
    """
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        # set image
        image = self.load_image("Title.png")
        self.set_image(image,800,350)

        # register for key event
        self.handle_key_events = True

    def key_pressed(self, key):
        """
        if the key pressed is pace the game will start
        """

        if key[pygame.K_SPACE]:
            self.room.running = False