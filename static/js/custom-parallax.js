var win = { "W": $(window).width(), "H": $(window).height() };
var mult = 0;
var stage = { "W": 1118, "H": 798 };

function initialize()
{
	win.W = $(window).width();
	win.H = $(window).height();
	mult = (win.W > win.H ? win.H / stage.H : win.W / stage.W);
	initSteps();
	return true;
}

function initSteps()
{
	$(".bg-color").height(win.H + 100);
	$(".first-part").height(win.H);
	
	$("[size]").each(function(){
		var s = this.getAttribute("size").split("x");
		s = { "W": Number(s[0]) * mult, "H": Number(s[1]) * mult };
		$(this).width(s.W).height(s.H);
	});
//	
//	$(".bubbles").each(function(){
//		var div = jQuery(this).children("div");
//		div.css("margin-top", ($(this).height() - div.height()) / 2);
//	});
	
	return true;
}
// ========================================================================== //

function redirect()
{
	if(!/^\#intro?$/i.test(window.location.hash)){
		if(Storage !== undefined){
			// Use local storage
			var lang = localStorage.getItem("lang");
			//if(lang !== null) location.href = hrefs[lang];
		}else{
			// Use cookies
		}
	}else{
		localStorage.removeItem("lang");
	}
	return true;
}

function prepare()
{
	initialize();
	return true;
}


$(window).on("resize", function(){ 
	prepare(); 
});
$(document).ready(function()
{
	prepare();
	sk = skrollr.init({
		"skrollrBody": "back",
		"constants": {
			"key1": 2000, "key2": 3000, "key3": 5000,
			"key4": 6000, "key5": 8000, "key6": 9000,
			"key7": 11000, "key8": 12000, "key9": 13000,
		}
	});
});

redirect();
