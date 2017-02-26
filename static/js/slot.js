var x = document.getElementsByClassName("box box-primary number");
for (i = 0; i < x.length; i++) {
   x[i].innerHTML = "0";
}

var reeling_time = 1000;
var stop_spinning_time_difference = 200;
var start_spinning_time = 360;

$.fn.slotMachine = function() {

    var hidden_reels_html = '';
    var hidden_reels_array = [];

    for (var $j = 0; $j <= 9; $j++) {
         hidden_reels_array[$j] = "";
      for (var $i = 0; $i <= 9; $i++) {
          hidden_reels_array[$j] += '<div class="reel-symbol' + ($i == 0 ? ' reel-loop' : '') + '">' + (($j + $i) % 10) + '</div>';
      }
    }

    var effectBeforeSpin = function () {
        $('.box-number .number').find('.main-reel-symbol').removeClass('reel-stop').addClass('reel-begin');
    };

    slotMachine();
    return this;
    };
