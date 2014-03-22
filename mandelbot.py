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

def iterate(x, y, limit=10):
	it = make_iterator(x, y)
	it_count = 0
	for x, y in it:
		it_count += 1
		if has_escaped(x, y):
			return it_count
		if it_count > limit:
			return -1

def get_colour(index):
	index = (index % 3) - 1
	return [(255, 0, 0), (0, 255, 0), (0, 0, 255)][index]

def main():
	img = Image.new('RGB', (1000, 1000), "black")
	pixels = img.load()
	size = 1000
	offset = size / 2
	for i in xrange(size):
		for j in xrange(size):
			x = i - offset
			y = j - offset
			it_count = iterate(x, y)
			if it_count != -1:
				pixels[i, j] = get_colour(it_count)
	img.save('out.bmp')
	os.startfile('out.bmp')

if __name__ == '__main__':
	main()
