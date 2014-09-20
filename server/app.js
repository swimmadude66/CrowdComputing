var express = require('express');
var path = require('path');

var methodOverride = require('method-override');
var session = require('express-session');
var bodyParser = require('body-parser');

var app = express();

var timeAndIP = require('./routes/timeAndIP');

// all environments
app.set('port', process.env.PORT || 3000);
app.set('views', path.join(__dirname, 'views'));
app.use(methodOverride());
app.use(session({ resave: true,
                  saveUninitialized: true,
                  secret: 'uwotm8' }));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(timeAndIP);
//app.use(express.static(path.join(__dirname, 'public')));

var routes = require('./routes/routes');
app.use(routes);



app.listen(app.get('port'), function(){
  console.log('Express server listening on port ' + app.get('port'));
});