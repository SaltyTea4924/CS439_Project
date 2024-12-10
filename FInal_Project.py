import math
import random
from PIL import Image


class Vector2 :
	def __init__(self,x, y) :
		self.x = x
		self.y = y
	

	def dot(self, other): 
		return self.x*other.x + self.y*other.y
	


def Shuffle(arrayToShuffle) :
	e = len(arrayToShuffle)-1
	while (e > 0):
		index = random.randint(0,e-1)
		temp = arrayToShuffle[e]
		
		arrayToShuffle[e] = arrayToShuffle[index]
		arrayToShuffle[index] = temp
		e = e - 1
	


def MakePermutation() :
	permutation = []
	for  i in range(0,256):  
		permutation.append(i)
		i += 1
	

	Shuffle(permutation)
	
	for  i in range(0,256):
		permutation.append(permutation[i])
	
	
	return permutation

Permutation = MakePermutation()

def GetConstantVector(v) :
	# v is the value from the permutation table
	h = v & 3
	if(h == 0):
		return Vector2(1.0, 1.0)
	elif(h == 1):
		return Vector2(-1.0, 1.0)
	elif(h == 2):
		return Vector2(-1.0, -1.0)
	else:
		return Vector2(1.0, -1.0)


def Fade(t) :
	return ((6*t - 15)*t + 10)*t*t*t


def interpolation(t, a1, a2) :
	return a1 + t*(a2-a1)


def Noise2D(x, y):
	newX = math.floor(x) & 255
	newY = math.floor(y) & 255

	xf = x-math.floor(x)
	yf = y-math.floor(y)

	topRight = Vector2(xf-1.0, yf-1.0)
	topLeft = Vector2(xf, yf-1.0)
	bottomRight = Vector2(xf-1.0, yf)
	bottomLeft = Vector2(xf, yf)
	
	#Select a value from the permutation array for each of the 4 corners
	valueTopRight = Permutation[Permutation[newX+1]+newY+1]
	valueTopLeft = Permutation[Permutation[newX]+newY+1]
	valueBottomRight = Permutation[Permutation[newX+1]+newY]
	valueBottomLeft = Permutation[Permutation[newX]+newY]
	
	dotTopRight = topRight.dot(GetConstantVector(valueTopRight))
	dotTopLeft = topLeft.dot(GetConstantVector(valueTopLeft))
	dotBottomRight = bottomRight.dot(GetConstantVector(valueBottomRight))
	dotBottomLeft = bottomLeft.dot(GetConstantVector(valueBottomLeft))
	
	u = Fade(xf)
	v = Fade(yf)
	
	return interpolation(u,
		interpolation(v, dotBottomLeft, dotTopLeft),
		interpolation(v, dotBottomRight, dotTopRight)
	)


def BWMap():
    image = Image.new(mode="RGB",size=[500,500])
    heightmap = Image.new(mode="RGB",size=[500,500])
    p = image.load()
    color = heightmap.load()
    for y in range(0,500):
        for x in range(0,500):
            n = Noise2D(x*0.01,y*0.01)
            n += 1.0
            n /= 2.0
            c = math.floor(255*n)
            p[x,y] = (c,c,c)
            if(n < 0.5):
                color[x,y] = (0,0,c*2,255)
            elif(n < 0.6):
                color[x,y] = (math.floor(c*0.9),math.floor(c*0.7),math.floor(c*0.5),255)
            elif(n < 0.9):
                color[x,y] = (0,c,math.floor(c*0.5),255)
            else:
                color[x,y] = (c,c,c,255)
    image.show()
    heightmap.show()

def CLMap(w,h,octa,f,a):
	image = Image.new(mode="RGB",size=[w,h])
	p = image.load()
	o = 0
	for x in range(0,w):
		for y in range(0,h):
			n = 0.0
			a = 1.0
			f = 0.005
			while(o < octa):
				v = a * Noise2D(x*f,y*f)
				n += v
				a *= 0.5
				f *= 2.0
				o+=1
			n += 1.0
			n /= 2.0
			rgb = math.floor(255*n)
			if(n < .5):
				p[x,y] = (0,0,rgb*2,255)
			elif(n < 0.6):
				p[x,y] = (math.floor(rgb*.9),math.floor(rgb*0.7),math.floor(rgb*0.5),255)	
			elif(n < 0.9):
				p[x,y] = (0,rgb,round(rgb*0.5),255)
			else:
				p[x,y] = (rgb,rgb,rgb,255)
			o = 0
	image.show()


def main():
	BWMap()
	CLMap(1000,1000,8,.015,2)

if __name__ == "__main__":
    main()