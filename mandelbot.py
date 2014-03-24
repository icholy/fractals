#!/usr/bin/env python

import Image
import os

def has_escaped(x, y):
  return x*x + y*y >= 4

def iterate(x, y, limit=1):
  cx, cy = x, y
  for i in xrange(limit):
    x, y = x*x - y*y + cx, 2*x*y + cy
    if has_escaped(x, y):
      return i + 1
  return -1

def pixel_to_complex_plane(x, y, size):
  x = ((4.0 / size) * x) - 2
  y = ((4.0 / size) * y) - 2
  return x, y

def make_grayscale_pallet(size):
  step = int(255 / size)
  return [(step*i,) * 3 for i in xrange(size)]

def get_color(pallet, x):
  if x == -1:
    return (0, 0, 0)
  else:
    return pallet[x - 1]

def main():

  size = 1000       # 1000 x 1000 pixel output
  n_iterations = 50 # use 50 iterations to check for divergence
  fname = "out.bmp" # save image as

  image = Image.new("RGB", (size, size), "black")
  pixels = img.load()
  pallet = make_grayscale_pallet(n_iterations)

  for px in xrange(size):
    for py in xrange(size):
      x, y = pixel_to_complex_plane(px, py, size)
      it_count = iterate(x, y, limit=n_iterations)
      pixels[px, py] = get_color(pallet, it_count)

  image.save(fname)

if __name__ == "__main__":
  main()
