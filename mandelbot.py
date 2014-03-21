
import itertools


def escaped(x, y):
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
		if escaped(x, y):
			return it_count
		if it_count > limit:
			return None

def main():
	colors = itertools.cycle(["red", "yellow", "blue"])
	size = 100
	offset = size / 2
	for i in xrange(size):
		for j in xrange(size):
			x, y = i - offset, j - offset
			it_count = iterate(x, y)
			if it_count is not None:
				color = itertools.isslice(colors, it_count, it_count+1)
				draw(x, y, color)


if __name__ == '__main__':
	main()
