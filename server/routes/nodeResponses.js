var express = require('express');
var rest = require('restler');
var router = express.Router();

router.post('/sendNodeStatusUpdate', function (req,res){
	var b = req.body;
	res.send(b);
});

router.post('/sendNodeProcessResponse', function (req,res){

});

router.post('/addNode', function(req,res){
	b = req.body;

	machine_id = b.machine_id;

	var jsonData = {
		userName : b.userName,
		thePassword : b.thePassword,
		source : b.machine_id
	};

	rest.postJson('http://www.crowdcomp.me/login',jsonData)
		.on('complete',function(data,response){
			console.log("data from /addNode -> login " + data);
		});

});

module.exports = router;