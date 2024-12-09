# CS439_Project

## Overview
This is the python version of procedural generation from the article/page made by Raufs blog which was helpful with coding and understanding both perlin noise and how procedural generation works. I’m also making a link to his github project. 

## Libraries 
Libraries/dependencies you will need to have for the code to work
Pillow
math
Random

You shouldn’t need to install math or random as those are in built libraries to Python and the import is already in the file, but you will need to install Pillow.
If you want to install it through terminal, use the command:
Pip install Pillow

If you use it in Thonny, you may need the actual file of Pillow in order to get that to work.

## Functions

Def BWMap()
This will create the black and white perlin noise map that is set to a 500 by 500 image size.

Def CLMap(w,h,octa,f,a)
This will create a better version of a color map and utilizes Fractal Brown motion to give it more jagged curves, adding more depth to the generated world. You can mess with the values in the main() function to get different results, like how many octaves mess with the perlin noise, size of the map, and the frequency and amplitude of the height map.

## Conclusion
I do want to somehow make this work with tiles where you would use a perlin noise map to determine where to place a tile, but so far I haven’t figured it out yet. My professor gave an idea of getting a matrix, like a 8x8 size for example, and calculating the average of that to determine what tile to use in that spot. Another idea I had which was how I was going to do it originally was to multiply a separate image by the size of the tiles and place it in a way similar to how you would use color map, but this would take longer and just add more unnecessary code.

I did accomplish in wanting to learn more about procedural generation and implementing it into a different language. The main problem I had was going into Python with the headspace of JES, which had functions that Python didn't, so I had to learn how to do things with images and incorporating different libraries I didn't know existed but still using that with what I have learned in the past.

## Links to Raufs blog
[Perlin Noise: A Procedural Generation Algorithm](https://rtouti.github.io/graphics/perlin-noise-algorithm)


[rtouti.github.io/examples/perlin-noise.html at gh-pages · rtouti/rtouti.github.io](https://github.com/rtouti/rtouti.github.io/blob/gh-pages/examples/perlin-noise.html)
