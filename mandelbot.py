import Image
import os

def has_escaped(x, y):
	"has the point escaped a circle of radius 2"
	return x*x + y*y >= 4

def make_iterator(x, y):
	cx, cy = x, y
	while True:
		nx = x*x - y*y + cx
		ny = 2*x*y + cy
		x, y = nx, ny
		yield x, y

def iterate(x, y, limit=1):
	it = make_iterator(x, y)
	for i in xrange(limit):
		x, y = next(it)
		if has_escaped(x, y):
			return i + 1
	return -1

def get_colour(pallet, index):
	return pallet[(index % len(pallet)) - 1]

def pixel_to_complex_plane(x, y, size):
	x = ((4.0 / size) * x) - 2
	y = ((4.0 / size) * y) - 2
	return x, y

def make_grayscale_pallet(size):
	step = 255 / size
	return [(step*i, step*i, step*i) for i in xrange(size)]

def main():
	size = 1000
	img = Image.new('RGB', (size, size), "black")
	n_iterations = 50
	pallet = make_grayscale_pallet(n_iterations)
	pixels = img.load()
	for i in xrange(size):
		for j in xrange(size):
			x, y = pixel_to_complex_plane(i, j, size)
			if not has_escaped(x, y):
				it_count = iterate(x, y, limit=n_iterations)
				if it_count != -1:
					pixels[i, j] = get_colour(pallet, it_count)
	img.save('out.bmp')
	os.startfile('out.bmp')

if __name__ == '__main__':
	main()
