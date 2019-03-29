function outletPowerOn( event ) {
  console.log( "Outlet power on: " + event.data.outlet );
  $.ajax({
    type: "GET",
    // url: "https://mcp.kurohai.com/api/v1/outlets/main-strip-01/control/on/" + event.data.outlet + "/",
    url: "http://mcp.kurohai.com:9002/api/v1/outlets/main-strip-01/control/on/" + event.data.outlet + "/",
    // data: { param: text}
  }).done(function( o ) {
     // do something
     console.log("done: " + JSON.stringify(o));
  });

}

function outletPowerOff( event ) {
  console.log( "Outlet power on: " + event.data.outlet );
  $.ajax({
    type: "GET",
    url: "http://mcp.kurohai.com:9002/api/v1/outlets/main-strip-01/control/off/" + event.data.outlet + "/",
    // data: { param: text}
  }).done(function( o ) {
     // do something
     console.log("done: " + JSON.stringify(o));
  });

}

var objOn = "";
for (i = 1; i<=4; i++) {
  objOn = $("#outlet-power-on-" + i);
  objOn.click({outlet: objOn.val()}, outletPowerOn)
}

var objOff = "";
for (i = 1; i<=4; i++) {
  objOff = $("#outlet-power-off-" + i);
  objOff.click({outlet: objOff.val()}, outletPowerOff)
}
