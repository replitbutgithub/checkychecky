enum ActionKind {
    Walking,
    Idle,
    Jumping
}
namespace SpriteKind {
    export const startblock = SpriteKind.create()
    export const npc = SpriteKind.create()
    export const visualrep = SpriteKind.create()
    export const ProjectileB = SpriteKind.create()
}
namespace StatusBarKind {
    export const egghealth = StatusBarKind.create()
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`end2`, function (sprite, location) {
    Overlapped = 1
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`beginning`, function (sprite, location) {
    Overlapped = 2
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`beginning2`, function (sprite, location) {
    Overlapped = 2
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`end5`, function (sprite, location) {
    Overlapped = 1
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (swordlearned == 1) {
        animation.runImageAnimation(
        weapon,
        assets.animation`swordanimation`,
        100,
        false
        )
        if (weapon.overlapsWith(deathbug)) {
            statusbar2.value += -1
        } else if (weapon.overlapsWith(eggo_wawfl)) {
            statusbar3.value += -1
        }
    } else {
        game.splash("You don't know how to swing the sword.")
    }
})
controller.player2.onButtonEvent(ControllerButton.A, ControllerButtonEvent.Pressed, function () {
    if (swordlearned == 1) {
        animation.runImageAnimation(
        weaponP2,
        assets.animation`swordanimation`,
        100,
        false
        )
        if (weaponP2.overlapsWith(deathbug)) {
            statusbar2.value += -1
        } else if (weaponP2.overlapsWith(eggo_wawfl)) {
            statusbar3.value += -1
        }
    } else {
        game.splash("You don't know how to swing the sword.")
    }
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`endtilemaze`, function (sprite, location) {
    tiles.placeOnTile(mySprite, tiles.getTileLocation(0, 0))
    tiles.setTilemap(tilemap`finalarena`)
    multilights.toggleLighting(false)
    eggo_wawfl = sprites.create(assets.image`eggo waffle`, SpriteKind.npc)
    tiles.placeOnTile(eggo_wawfl, tiles.getTileLocation(14, 7))
    statusbar3 = statusbars.create(20, 4, StatusBarKind.egghealth)
    statusbar3.value = 3
    statusbar3.attachToSprite(eggo_wawfl)
})
statusbars.onZero(StatusBarKind.EnemyHealth, function (status) {
    deathbug.destroy()
    buggykilled = 1
    deathbugon = 0
    theme = 1
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`end`, function (sprite, location) {
    Overlapped = 1
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`beginning3`, function (sprite, location) {
    Overlapped = 2
})
statusbars.onZero(StatusBarKind.egghealth, function (status) {
    eggo_wawfl.destroy(effects.warmRadial, 500)
    pause(2000)
    animation.runImageAnimation(
    DeathbugBIGGER,
    assets.animation`deathbugfaceleft`,
    100,
    true
    )
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    game.over(false, effects.melt)
})
let anticrash = 0
let mySprite2: Sprite = null
let players2 = 0
let weaponP2: Sprite = null
let statusbar3: StatusBarSprite = null
let statusbar2: StatusBarSprite = null
let deathbug: Sprite = null
let deathbugon = 0
let eggo_wawfl: Sprite = null
let DeathbugBIGGER: Sprite = null
let weapon: Sprite = null
let mySprite: Sprite = null
let Overlapped = 0
let theme = 0
let swordlearned = 0
let buggykilled = 0
let Weapon_Attack_Mode = 0
buggykilled = 0
let statusbar = statusbars.create(20, 4, StatusBarKind.Health)
statusbar.value = 1
statusbar.setColor(0, 0)
game.splash("Arrow keys or joystick to move. Press A or spacebar to attack!")
swordlearned = 0
theme = 1
Overlapped = 0
let tilemap2 = 1
tiles.setTilemap(tilemap`1`)
mySprite = sprites.create(img`
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    `, SpriteKind.Player)
controller.moveSprite(mySprite, 100, 100)
weapon = sprites.create(assets.image`Sword`, SpriteKind.Projectile)
DeathbugBIGGER = sprites.create(img`
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    `, SpriteKind.Enemy)
eggo_wawfl = sprites.create(img`
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    `, SpriteKind.npc)
mySprite.setPosition(20, 120)
deathbugon = 0
scene.cameraFollowSprite(mySprite)
characterAnimations.loopFrames(
mySprite,
assets.animation`Bugmove`,
100,
characterAnimations.rule(Predicate.Moving)
)
characterAnimations.loopFrames(
mySprite,
assets.animation`Bugnotmove`,
100,
characterAnimations.rule(Predicate.NotMoving)
)
statusbar.attachToSprite(mySprite)
forever(function () {
    weapon.x = mySprite.x + 15
    weapon.y = mySprite.y
    if (players2 == 1) {
        weaponP2.x = mySprite2.x + 15
        weaponP2.y = mySprite2.y
    }
})
forever(function () {
    if (theme == 2) {
        music.stopAllSounds()
        music.playMelody(music.convertRTTTLToMelody(""), 120)
    }
})
forever(function () {
    if (tilemap2 == 5) {
        if (controller.down.isPressed()) {
            multilights.flashlightSourceAttachedTo(mySprite).direction = 90
        } else if (controller.left.isPressed()) {
            multilights.flashlightSourceAttachedTo(mySprite).direction = 180
        } else if (controller.up.isPressed()) {
            multilights.flashlightSourceAttachedTo(mySprite).direction = 270
        } else if (controller.right.isPressed()) {
            multilights.flashlightSourceAttachedTo(mySprite).direction = 0
        }
    }
})
forever(function () {
    if (deathbugon == 1 && buggykilled == 0) {
        scene.cameraShake(2, 100)
    }
})
forever(function () {
    if (theme == 1) {
        music.stopAllSounds()
        music.playMelody(music.convertRTTTLToMelody("random son:d=4,o=5,b=80:a2,c,b4,c,p,f2,b4,p,f3,f,p,a2,a4,c,e,p,g2,g#4,b4,d,p,e2,f,e,b4,p,1a2"), 120)
    }
})
forever(function () {
    if (theme == 3) {
        music.stopAllSounds()
        music.playMelody(music.convertRTTTLToMelody("random son:d=4,o=5,b=480:a6,e6,f6,d6,a#6,f6,e6,c#6,g6,a#6,a6,d6,a#,d6,g6,e6,c6,c#6,e6,d6,a,c#6,e6,d6"), 120)
    }
})
forever(function () {
    if (theme == 4) {
        music.stopAllSounds()
        music.playMelody(music.convertRTTTLToMelody("final boss:d=4,o=5,b=100:16g#,16g#,16g#,16p,16e,16e,16e,16p,16c#,16c#,16c#,16p,8p,16g4,16p,16c#,16p,16c#,16p,16d,16c#,16d#,16c#,16e,16c#,16f,16c#,16p,16b4,16p,8p,16c,16p,8p,16c#"), 120)
    }
})
forever(function () {
    if (Overlapped == 1) {
        Overlapped = 0
        if (tilemap2 == 1) {
            tiles.setTilemap(tilemap`2`)
            tiles.placeOnTile(mySprite, tiles.getTileLocation(1, 7))
            if (players2 == 1) {
                tiles.placeOnTile(mySprite2, tiles.getTileLocation(1, 7))
            }
            if (swordlearned == 1 && anticrash == 0 && players2 == 0) {
                mySprite2.destroy()
                anticrash += 1
            }
        } else if (tilemap2 == 2) {
            tiles.setTilemap(tilemap`2`)
            tiles.placeOnTile(mySprite, tiles.getTileLocation(1, 7))
            if (players2 == 1) {
                tiles.placeOnTile(mySprite2, tiles.getTileLocation(1, 7))
            }
        } else if (tilemap2 == 3) {
            if (buggykilled == 0) {
                theme = 2
                controller.moveSprite(mySprite, 0, 0)
                if (players2 == 1) {
                    controller.moveSprite(mySprite2, 0, 0)
                }
                scene.cameraShake(4, 500)
                pause(1000)
                mySprite.setVelocity(-50, 0)
                scene.cameraShake(8, 500)
                pause(1000)
                deathbug = sprites.create(img`
                    .......f.f......f.f......f.f......f.f......f.f......f.f......f.f......f.f...........................
                    ........f.f......f.f......f.f......f.f......f.f......f.f......f.f......f.f..........................
                    ........f.f......f.f......f.f......f.f......f.f......f.f......f.f......f.f..........................
                    ..fff...fff......fff......fff......fff......fff......fff......fff......fff.......fff................
                    .f444f.f444ff...f444ff...f444ff...f444ff...f444ff...f444ff...f444ff...f444ff....f444f...............
                    f4ff4ff455544f.f455544f.f455544f.f455544f.f455544f.f455544f.f455544f.f455554ff..f4ff2f..............
                    .f..f445222544f45222544f45222544f45222544f45222544f45222544f45222544f452225544ff4f..f...............
                    ....f452222254f52222254f52222254f52222254f52222254f52222254f52222254f522222255444f..................
                    ....f452222254f52222254f52222254f52222254f52222254f52222254f52222254f52222225544f...................
                    .f..f445222544f45222544f45222544f45222544f45222544f45222544f45222544f452225544ff....................
                    f4ff4ff455544f.f455544f.f455544f.f455544f.f455544f.f455544f.f455544f.f455554ff......................
                    .f444f.f444ff...f444ff...f444ff...f444ff...f444ff...f444ff...f444ff...f444ff........................
                    ..fff...fff......fff......fff......fff......fff......fff......fff......fff..........................
                    ........f.f......f.f......f.f......f.f......f.f......f.f......f.f......f.f..........................
                    ........f.f......f.f......f.f......f.f......f.f......f.f......f.f......f.f..........................
                    .......f.f......f.f......f.f......f.f......f.f......f.f......f.f......f.f...........................
                    `, SpriteKind.Enemy)
                tiles.placeOnTile(deathbug, tiles.getTileLocation(16, 7))
                statusbar2 = statusbars.create(20, 4, StatusBarKind.EnemyHealth)
                statusbar2.attachToSprite(deathbug, 0, -50)
                statusbar2.value = 3
                animation.runImageAnimation(
                deathbug,
                assets.animation`deathbugfaceleft`,
                100,
                true
                )
                deathbug.follow(mySprite, 50)
                controller.moveSprite(mySprite, 100, 100)
                if (players2 == 1) {
                    controller.moveSprite(mySprite2, 100, 100)
                }
                pause(200)
                deathbug.follow(mySprite, 100)
                deathbugon = 1
                theme = 3
                Overlapped = 0
            }
        } else if (tilemap2 == 4) {
            tiles.placeOnTile(mySprite, tiles.getTileLocation(0, 15))
            if (players2 == 1) {
                tiles.placeOnTile(mySprite2, tiles.getTileLocation(0, 15))
            }
            tiles.setTilemap(tilemap`MazeLvl`)
            multilights.toggleLighting(true)
            multilights.addFlashLightSource(
            mySprite,
            0,
            32,
            30
            )
            multilights.addLightSource(mySprite, 4)
            theme = 2
        }
        if (!(deathbugon == 1)) {
            tilemap2 += 1
        }
    } else if (Overlapped == 2) {
        Overlapped = 0
        if (tilemap2 == 2) {
            if (deathbugon == 1 && swordlearned == 0 || deathbugon == 0) {
                tiles.setTilemap(tilemap`1`)
                tiles.placeOnTile(mySprite, tiles.getTileLocation(14, 7))
                if (players2 == 1) {
                    tiles.placeOnTile(mySprite2, tiles.getTileLocation(14, 7))
                }
                if (deathbugon == 1 && swordlearned == 0) {
                    theme = 1
                    deathbugon = 0
                    deathbug.destroy()
                    mySprite2 = sprites.create(img`
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        `, SpriteKind.npc)
                    animation.runImageAnimation(
                    mySprite2,
                    assets.animation`Bugnotmove0`,
                    100,
                    true
                    )
                    tiles.placeOnTile(mySprite2, tiles.getTileLocation(0, 7))
                    controller.moveSprite(mySprite, 0, 0)
                    mySprite.setVelocity(-100, 0)
                    pause(1500)
                    game.showLongText("Yikes! One of the corrupt citizens of this world! You couldn't touch him!", DialogLayout.Bottom)
                    game.showLongText("Here! Let me teach you how to use that sword of yours!", DialogLayout.Bottom)
                    game.splash("You learned to use your sword.")
                    game.showLongText("Now you can kill that deathbug and bring me back my jewel!", DialogLayout.Bottom)
                    game.showLongText("Oh? He's camping outside the door? Let me fix that.", DialogLayout.Bottom)
                    scene.cameraShake(8, 2000)
                    mySprite.setVelocity(0, 0)
                    swordlearned = 1
                    pause(2000)
                    game.splash("The deathbug left...")
                    game.showLongText("The deathbug isn't gone! He's right back where you found him.", DialogLayout.Bottom)
                    game.showLongText("Y'know what? That seems a bit hard. Can I help you?", DialogLayout.Bottom)
                    if (game.ask("Play in 2-player mode?")) {
                        game.showLongText("Thanks! I've always wanted to go on an adventure!", DialogLayout.Bottom)
                        controller.player2.moveSprite(mySprite2)
                        players2 += 1
                        weaponP2 = sprites.create(assets.image`Sword`, SpriteKind.Projectile)
                        weaponP2.follow(mySprite2)
                    } else {
                        game.showLongText("Okay... Good luck.", DialogLayout.Bottom)
                    }
                    controller.moveSprite(mySprite, 100, 100)
                }
            }
        } else if (tilemap2 == 3) {
            if (deathbugon == 1) {
                tiles.placeOnTile(deathbug, tiles.getTileLocation(22, 7))
            }
            tiles.setTilemap(tilemap`2`)
            tiles.placeOnTile(mySprite, tiles.getTileLocation(14, 7))
            if (players2 == 1) {
                tiles.placeOnTile(mySprite2, tiles.getTileLocation(14, 7))
            }
        } else {
        	
        }
        tilemap2 += -1
    }
})
