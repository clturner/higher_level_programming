#!/usr/bin/node
//
const request = require('request');

request(process.argv[2], function(err, res, body) {
    let check_id = 1;
    let count = 0;
    let a = JSON.parse(body);
    let final_object = {};
    let body_length = Object.keys(a).length;
    for (x = 0; x < body_length; x++) {
	if (a[x]['completed'] == true && check_id == a[x]['userId']) {
	    count += 1;
	} else if (a[x]['completed'] == false && check_id == a[x]['userId']) {
	    {}
	} else {
//	    console.log(a[x]['userId'] - 1);
	    console.log(count);
//	    final_object[(a[x]['userId'])];
	    count = 0;
	    check_id += 1;
        }
    }
//    console.log(final_object);
});
//	} else if (a[x]['completed'] == true && check_id != a[x]['userId']) {
//	    console.log(a[x]['userId'] - 1);
//	    console.log(count);
//	    final_object[(a[x]['userId'])];
//	    count = 0;
//	    check_id += 1;
//	} else if (a[x]['completed'] == false && check_id != a[x]['userId']) {
//	    q = a[x]['userId'] - 1;
//	    console.log(q);
//	    console.log(count);
//	    count = 0;
  //          check_id += 1;
//	} else {
//	    console.log("ooopppss :(");
//	}
  //  }
    //console.log(final_object);
//});
