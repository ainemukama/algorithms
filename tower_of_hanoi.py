def move_tower(height, from_pole=1, to_pole=2, intermediate_pole=3):
    if height >= 1:
        move_tower(height-1, from_pole, intermediate_pole, to_pole)
        print 'height: %d \tmoving disk from pole %d to pole %d' % (height, from_pole, to_pole)
        move_tower(height-1, intermediate_pole, to_pole, from_pole)

for height in range(1, 6):
    print 'height', height
    move_tower(height)
