_world_ = {}
starting_position = (0, 0)

def load_tiles():
    """Parses a file that describes the world space into the _world object"""
    with open('resources/map.txt', 'r') as f:
        rows = f.readlines()
    # assuming all rows have the same number of tabs
    # FIXME: bad assumtion, esp with atom!
    x_max = len( rows[0].split('\t') )
    for y in range( len( rows ) ):
        cols = rows[y].split('\t')
        for x in range( x_max ):
            # Windows users may need to replace '\r\n'
            # This replaces the last return line
            # to conform to what the other empty entries are.
            tile_name = cols[x].replace('\n', '')
            if tile_name == 'StartingRoom':
                global starting_position
                starting_position = ( x, y )
            _world[ ( x, y ) ] = None if tile_name == '' else getattr(__import__('tiles'), tile_name)(x, y)

def tile_exists(x, y):
    return _world.get( ( x, y ) )
