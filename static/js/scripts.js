var sk = null;
var win = { "W": jQuery(window).width(), "H": jQuery(window).height() };
var stage = { "W": 1118, "H": 798 };
var mult = 0;

function initialize()
{
	win.W = jQuery(window).width();
	win.H = jQuery(window).height();
	mult = (win.W > win.H ? win.H / stage.H : win.W / stage.W);
	
	initSteps();
	return true;
}

function initSteps()
{
	$(".viewport").width(win.W).height(win.H);
	
	$("[size]").each(function(){
		var s = this.getAttribute("size").split("x");
		s = { "W": Number(s[0]) * mult, "H": Number(s[1]) * mult };
		jQuery(this).width(s.W).height(s.H);
	});
	
	$(".bubbles").each(function(){
		var div = jQuery(this).children("div");
		div.css("margin-top", ($(this).height() - div.height()) / 2);
	});
	
	// Step 0 ------------------------------------------------------------------
//	jQuery("#step-0 > div > div:nth-child(2)").width(Math.floor(mult * stage.W)).height(win.H);
	
	var screenWidth = jQuery(window).width();
	jQuery("#step-0 > div > div:nth-child(2)").width(screenWidth).height(win.H);
	var centerW = $("#step-0 > div > div:nth-child(2)").width();
	jQuery("#step-0 > div > div:first-child, #step-0 > div > div:last-child").height(win.H).width((win.W - centerW) / 2);
	
	// Step 1~3 ----------------------------------------------------------------
	jQuery(".viewport").each(function(){
		if($(this).children(".pack").length > 0){
			var p = $(this).children(".pack").attr("size").split("x");
			p = { "W": Number(p[0]) * mult, "H": Number(p[1]) * mult };
			jQuery(this).children(".pack").width(p.W).height(p.H);
			jQuery(this).children(".pack").css({ "margin-left": (p.W / -2) + "px", "margin-top": (p.H / -2) + "px" });
		}
	});
	
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


jQuery(window).on("resize", function(){ prepare(); });
jQuery(document).ready(function($)
{
	prepare();
	sk = skrollr.init({
		"skrollrBody": "back",
		"constants": {
			"key1": 2000, "key2": 3000, "key3": 5000,
			"key4": 6000, "key5": 8000, "key6": 9000,
			"key7": 11000, "key8": 12000, "key9": 13000,
			"key10": 14000, "key11": 15000, "key12": 17000,
			"key13": 18000,
		}
	});
	$("#goup").on("click", function(){
		$("html, body").animate({ "scrollTop": 0 });
	});
});

redirect();