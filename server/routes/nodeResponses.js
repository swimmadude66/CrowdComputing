var express = require('express');
var router = express.Router();

router.post('/sendNodeStatusUpdate', function (req,res){
	var b = req.body;
	res.send(b);
});

router.post('/sendNodeProcessResponse', function (req,res){

});

module.exports = router;