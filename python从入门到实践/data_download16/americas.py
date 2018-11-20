from pygal_maps_world.maps import World

world = World()
world.title = 'North, Center and South America'

world.add('North America', ['ca', 'mx', 'us'])
world.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
world.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])

world.render_to_file('americas.svg')
