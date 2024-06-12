basic.show_string("" + str((music.string_playable("C5 B A G F E D C ", 120))))

def on_forever():
    music.play(music.string_playable("C5 B A G F E D C ", 120),
        music.PlaybackMode.IN_BACKGROUND)
basic.forever(on_forever)
