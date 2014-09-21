var express = require('express');
var router = express.Router();

var UserDAO = require('../DAO/userDAO').UserDAO;

// define the home page route
router.get('/', function (req, res) {
	res.render('index.html',{requestIP: req.ip});
});

router.post('/register', function (req,res){
	var b = req.body;

	var userDAO = new UserDAO('localhost', 3306);

    userDAO.addUser(b.userName, b.thePassword, function(err){
    	if(err){
    		console.log('Error adding user - responding');
    		res.send(err);
    	}
    	else{
			req.session.userName = userName;
			req.session.thePassword = thePassword;
        	console.log('Added user successfully - responding');
        	res.redirect('/home');
    	}
    });
});

router.post('/login', function (req,res){
	var b = req.body;

	var userDAO = new UserDAO('localhost', 3306);

	userDAO.loginUser(b.userName,b.thePassword, function(err){
		if(err){
			console.log('Could not find the user in DB');
			res.send(err);
		}
		else{
			req.session.userName = b.userName;
			req.session.thePassword = b.thePassword;
			console.log('Successfully found user - logging in');
			if(b.source === null){
				res.redirect('/home');
			}
			else{
				res.send({access : 'granted'});
			}
		}
	});

});

router.get('/home', function(req,res){
	// add bunch of rest calls here to get the data for groups/clusters/nodes
	console.log(req.session.userName);
	res.render('userPage.html');
});

router.get('/getClusters', function(req,res){
	userName = req.param.userName;


});

module.exports = router;