// Minimal runtime code for otto
var dict = function (anObject) {
	return anObject;
};
var list = function (iterable) {
	return iterable;
}
var len = function (anObject) {
	return anObject.length;
};
Array.prototype.append = function (element) {
	this.push(element);
};
String.prototype.py_replace = function (old, aNew, maxreplace) {
	return this.split(old, maxreplace).join(aNew);
};
