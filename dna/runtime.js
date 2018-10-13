// Minimal runtime code for otto, excerpts from Transcrypt runtime
var dict = function (anObject) {
	return anObject;
};

var list = function (iterable) {
	return iterable;
};

var len = function (anObject) {
	return anObject.length;
};

Array.prototype.append = function (element) {
	this.push(element);
};

String.prototype.__getslice__ = function (start, stop, step) {
	if (start < 0) {
		start = this.length + start;
	}
	if (stop == null) {
		stop = this.length;
	}
	else if (stop < 0) {
		stop = this.length + stop;
	}
	var result = '';
	if (step == 1) {
		result = this.substring (start, stop);
	}
	else {
		for (var index = start; index < stop; index += step) {
			result = result.concat (this.charAt(index));
		}
	}
  return result;
};

String.prototype.py_replace = function (old, aNew, maxreplace) {
	return this.split(old, maxreplace).join(aNew);
};

var __in__ = function (element, container) {
		if (container === undefined || container === null) {
				return false;
		}
		if (container.__contains__ instanceof Function) {
				return container.__contains__ (element);
		}
		else {
				return (
						container.indexOf ?
						container.indexOf (element) > -1 :
						container.hasOwnProperty (element)
				);
		}
};
