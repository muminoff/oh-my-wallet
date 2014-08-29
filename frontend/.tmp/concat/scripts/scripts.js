'use strict';
/**
 * @ngdoc overview
 * @name frontendApp
 * @description
 * # frontendApp
 *
 * Main module of the application.
 */
angular.module('frontendApp', [
  'ngAnimate',
  'ngCookies',
  'ngResource',
  'ngRoute',
  'ngSanitize',
  'ngTouch'
]).config([
  '$routeProvider',
  function ($routeProvider) {
    $routeProvider.when('/categories', {
      templateUrl: 'views/categories.html',
      controller: 'CategoriesCtrl'
    }).when('/monthlyExpenses', {
      templateUrl: 'views/monthlyexpenses.html',
      controller: 'MonthlyexpensesCtrl'
    }).when('/weeklyExpenses', {
      templateUrl: 'views/weeklyexpenses.html',
      controller: 'WeeklyexpensesCtrl'
    }).when('/totalExpenses', {
      templateUrl: 'views/totalexpenses.html',
      controller: 'TotalexpensesCtrl'
    }).otherwise({ redirectTo: '/' });
  }
]);
'use strict';
/**
 * @ngdoc function
 * @name frontendApp.controller:CategoriesCtrl
 * @description
 * # CategoriesCtrl
 * Controller of the frontendApp
 */
angular.module('frontendApp').controller('CategoriesCtrl', [
  '$scope',
  function ($scope) {
    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
  }
]);
'use strict';
/**
 * @ngdoc function
 * @name frontendApp.controller:MonthlyexpensesCtrl
 * @description
 * # MonthlyexpensesCtrl
 * Controller of the frontendApp
 */
angular.module('frontendApp').controller('MonthlyexpensesCtrl', [
  '$scope',
  function ($scope) {
    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
  }
]);
'use strict';
/**
 * @ngdoc function
 * @name frontendApp.controller:WeeklyexpensesCtrl
 * @description
 * # WeeklyexpensesCtrl
 * Controller of the frontendApp
 */
angular.module('frontendApp').controller('WeeklyexpensesCtrl', [
  '$scope',
  function ($scope) {
    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
  }
]);
'use strict';
/**
 * @ngdoc function
 * @name frontendApp.controller:TotalexpensesCtrl
 * @description
 * # TotalexpensesCtrl
 * Controller of the frontendApp
 */
angular.module('frontendApp').controller('TotalexpensesCtrl', [
  '$scope',
  function ($scope) {
    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
  }
]);