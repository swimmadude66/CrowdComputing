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
        	console.log('Added user successfully - responding');
        	res.send(true);
    	}
    });
});

router.post('/login', function (req,res){
	var b = req.body;

	var userDAO = new UserDAO('localhost', 3306);

	userDAO.loginUser(b.userName,b.thePassword, function(results,err){
		console(results);
		if(err){
			console.log('Could not find the user in DB');
			res.send(err);
		}
		else{
			console.log('Successfully found user - logging in');
			res.render('userPage.html',{data: results});
		}
	});

});

module.exports = router;