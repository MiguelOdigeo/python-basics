class DraggableWindow():
    def drag(self):
        print( " dragging ")


class ResizableWindow():
    def resize(self):
        print(" resizing ")


class MyWindow(DraggableWindow, ResizableWindow):
    def act(self):
        super().drag()
        super().resize()

window = MyWindow()

window.act()