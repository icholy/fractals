#!/usr/bin/env python

import Image
import os

def has_escaped(x, y):
  return x*x + y*y >= 4

def make_iterator(x, y):
  cx, cy = x, y
  while True:
    x, y = x*x - y*y + cx, 2*x*y + cy
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
  step = int(255 / size)
  return [(step*i,) * 3 for i in xrange(size)]

def main():

  size = 1000       # 1000 x 1000 pixel output
  n_iterations = 50 # use 50 iterations to check for divergence
  fname = "out.bmp" # save image as

  img = Image.new("RGB", (size, size), "black")
  pallet = make_grayscale_pallet(n_iterations)
  pixels = img.load()
  for px in xrange(size):
    for py in xrange(size):
      x, y = pixel_to_complex_plane(px, py, size)
      it_count = iterate(x, y, limit=n_iterations)
      if it_count != -1:
        pixels[px, py] = get_colour(pallet, it_count)
  img.save(fname)

if __name__ == "__main__":
  main()
