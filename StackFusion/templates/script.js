function Ctrl($scope) {
  var today = new Date();
  var minAge = 18;
  $scope.minAge = new Date(today.getFullYear() - minAge, today.getMonth(), today.getDate());
}

  angular.module('formExample', [])
    .controller('ExampleController', ['$scope', function($scope) {
      $scope.master = {};
      $scope.update = function(user) {
        $scope.master = angular.copy(user);
      };
      $scope.reset = function() {
        $scope.user = angular.copy($scope.master);
      };
      $scope.reset();
    }]);source
