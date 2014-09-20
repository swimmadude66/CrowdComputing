var express = require('express');
var router = express.Router();

var dateObj = new Date();

// middleware specific to this router
router.use(function (req, res, next) {
  console.log('--------------------');
  console.log('Time: ');
  console.log(dateObj.toString());
  console.log('IP Address: ');
  console.log(req.ip);
  next();
});

module.exports = router;