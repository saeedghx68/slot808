angular.module('myApp', [])
.controller('myCtrl', ['$scope', '$http', function($scope, $http) {
    $scope.first_wheel = 0;
    $scope.second_wheel = 0;
    $scope.third_wheel = 0;

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
    $scope.slotMachine = function () {

      var my_number_array = [$scope.first_wheel, $scope.second_wheel, $scope.third_wheel]

        var reels_html = '<div class="reel">' + hidden_reels_array[($i % 10)] + '</div>';

        effectBeforeSpin();

        var startSpinning = function () {

            document.getElementById('msg').innerHTML = "";
            spin_btn = document.getElementById('spin');
            spin_btn.setAttribute("disabled","disabled");
            spin_btn.value = "wait...";

            $('.box-number').find(".number").html(reels_html);

            var my_timer = reeling_time;

            $.each(my_number_array, function (my_index, my_value) {

              var next_value = /^[0-9]$/.test(my_value) ? (parseInt(my_value, 10) + 1) % 10 : "0";

                var stopSpinning = function () {

                    $('.box-number').find('.reel:eq(' + my_index + ')')
                      .html("<div class='reel-symbol main-reel-symbol reel-stop'>" + my_value + "</div>")
                      .append("<div class='reel-symbol'>" + next_value + "</div>");

                        window.setTimeout(function() {
                            spin_btn.removeAttribute("disabled");
                            spin_btn.value = "spin";
                            spin_btn.innerHTML = "spin";

                            document.getElementById('msg').innerHTML = $scope.msg;

                        }, 500);
                };
                setTimeout(stopSpinning, my_timer );
                my_timer += stop_spinning_time_difference;
            });
        };

        setTimeout(startSpinning, start_spinning_time);

    };

    $scope.myFunc = function() {
        $http.get('/get-lattery/')
          .success(function(data) {

                $scope.first_wheel = data.firstWheel;
                $scope.second_wheel = data.secondWheel;
                $scope.third_wheel = data.thirdWheel;
                $scope.msg = data.message;
                $scope.total_spin = data.totalSpin ;
                $scope.slotMachine()

        });
    };
}]);
