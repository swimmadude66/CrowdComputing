var express = require('express');
var router = express.Router();

// define the home page route
router.get('/', function (req, res) {
	res.send({requestIP: req.ip}).end();
});

router.get('/test', function (req,res) {
	console.log('Loaded the test page');
	res.status(200).end();
});

module.exports = router;