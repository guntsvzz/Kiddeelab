for row in range(number_row):
        for column in range(number_column):
            x = column * TILE_SIZE 
            y = row * TILE_SIZE
            screen.blit('path', (x,y))
            material = maze[row][column]
            tile = tiles[material]
            if tile != 'path':
                screen.blit(tile, (x,y))