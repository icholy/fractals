import Image
import os


def has_escaped(x, y):
	"has the point escaped a circle of radius 2"
	return x*x + y*y > 4

def make_iterator(x, y):
	cx, cy = x, y
	while True:
		x = x*x + y*y + cx
		y = 2*x*y + cy
		yield x, y

def iterate(x, y, limit=1):
	it = make_iterator(x, y)
	for i in xrange(limit):
		x, y = next(it)
		if has_escaped(x, y):
			return i + 1
	return -1

def get_colour(index):
	index = (index % 3) - 1
	return [(255, 0, 0), (0, 255, 0), (0, 0, 255)][index]

def pixel_to_complex_plane(x, y, size):
	x = ((4.0 / size) * x) - 2
	y = ((4.0 / size) * y) - 2
	return x, y

def main():
	size = 1000
	img = Image.new('RGB', (size, size), "black")
	pixels = img.load()
	for i in xrange(size):
		for j in xrange(size):
			x, y = pixel_to_complex_plane(i, j, size)
			it_count = iterate(x, y, limit=50)
			if it_count != -1:
				pixels[i, j] = get_colour(it_count)
	img.save('out.bmp')
	os.startfile('out.bmp')

if __name__ == '__main__':
	main()
