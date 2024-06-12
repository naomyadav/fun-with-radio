basic.showString("" + ("" + music.stringPlayable("C5 B A G F E D C ", 120)))
basic.forever(function on_forever() {
    music.play(music.stringPlayable("C5 B A G F E D C ", 120), music.PlaybackMode.InBackground)
})
