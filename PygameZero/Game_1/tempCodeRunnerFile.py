    def movement(speed = 5):
            if keyboard.w or keyboard.up: #full
                self.y = self.y - speed #full
                # moving()
            if keyboard.a or keyboard.left: #short
                self.x -= speed #short
                # moving()
            if keyboard.s or keyboard.down: #short
                self.y += speed #short
                # moving()    
            if keyboard.d or keyboard.right: #short
                self.x += speed #short
                # moving()