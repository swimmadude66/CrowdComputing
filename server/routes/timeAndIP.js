var express = require('express');
var router = express.Router();
var fs = require('fs');

var dateObj = new Date();

// middleware specific to this router
router.use(function (req, res, next) {

	var timeAndIPString = '--------------------\n' +
	'Time: \n' +
	dateObj.toString() + '\n' +
	'IP Address: \n' + 
	req.ip + '\n' +
	'Request URL: ' +
	req.method + ' ' + req.path + '\n';

	console.log(timeAndIPString);

	fs.appendFile('timeLog.txt', timeAndIPString , function (err) {
		if (err) {
			throw err;
		}
	});

	next();
});

module.exports = router;