#!/usr/bin/env python3
import soy
from time import sleep

room = soy.scenes.Room(soy.atoms.Size((10.0,10.0,4.0)))
room['cam'] = soy.bodies.Camera(soy.atoms.Position((0, 0, 10)))
room['light'] = soy.bodies.Light(soy.atoms.Position((3, 3, 5)))

client = soy.Client()
client.window.append(soy.widgets.Projector(room['cam']))

blue = soy.atoms.Color('blue')
deeppink = soy.atoms.Color('deeppink')
darkslategray = soy.atoms.Color('darkslategray')
red = soy.atoms.Color('red')
green = soy.atoms.Color('green')
brick = soy.textures.Texture('brick.jpg')
gravel = soy.textures.Texture('gravel.jpg')

material1 = soy.materials.Textured()
#material1.colormap = soy.textures.Cubemap("checkered", [deeppink, blue, darkslategray], 1,2,3)


room['cube1'] = soy.bodies.Box(soy.atoms.Position((1.0, 0.2, 1)))
room['cube1'].material = material1
room['cube1'].material = soy.materials.Textured(colormap = gravel)
room['light1'] = soy.bodies.Light(soy.atoms.Position((1.3, 0.2, 1)))
room['light1'].diffuse = soy.atoms.Color('deeppink')
room['light1'].specular = soy.atoms.Color('deeppink')

material2 = soy.materials.Textured()
#material2.bumpmap = soy.textures.Bumpmap("media/lava.png")
material2 = soy.materials.Colored('yellow')

#room['cube2'] = soy.bodies.Sphere(soy.atoms.Position((3.0, 0.2, 1)))

material3 = soy.materials.Textured()
#material3.bumpmap = soy.textures.Bumpmap('brick.jpg')
#colormap = soy.materials.Textured(colormap = brick)

room['cube2'] = soy.bodies.Box(soy.atoms.Position((3,0.2,1)))
room['cube2'].material = material2
room['cube2'].material = soy.materials.Colored('yellow')

room['sphere1'] = soy.bodies.Sphere()
room['sphere1'].material = material3
room['sphere1'].material = soy.materials.Textured(colormap = brick)



if __name__ == '__main__':
    while client:
        sleep(.1)
