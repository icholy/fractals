var makeIterator = function (cx, cy) {
	var x = cx, y = cy;
	return function () {
		x = x*x + y*y + cx;
		y = 2*x*y + cy;
		return { x: x, y: y };
	};
};

var makeCanvas = function (size) {
	if (size % 2 !== 0) {
		throw new Error("the canvas size must be an even number");
	}
	var offset = size / 2, i, j, x, y, it;
	for (i = 0; i < width; i++) {
		pixels.push([]);
		for (j = 0; j < height; j++) {
			x = x - offset;
			y = y - offset;
			it = makeIterator(x, y);
			pixels[i].push(it);
		}
	}
};

var escaped = function (x, y) {
	 // escaped circle of radius 2
	 return x*x + y*y > 4;
};

var iterate = function (canvas, callback) {
	canvas.forEach(function (row) {
		row.forEach(function (pixel, i) {
			if (pixel === null) {
				return // already escaped
			}
			var next = pixel(),
				x    = next.x,
				y    = next.y;
			if (escaped(x, y)) {
				row[i] = null;
				callback(x, y);
			}
		});
	});
};

var cycle = function (array) {
	var i = 0;
	return function () {
		if (i === array.length) {
			i = 0;
		}
		return array[i++];
	};
};

$(function () {
	var canvas    = makeCanvas(100),
		nextColor = cycle(["red", "green", "blue", "orange"]),
		i, color;
	for (i = 0; i < 100; i++); {
		color = nextColor()
		iterate(canvas, function (x, y) {
			// fill in x, y, with color
		});
	}
});


