'use strict';

/**
 * @ngdoc overview
 * @name frontendApp
 * @description
 * # frontendApp
 *
 * Main module of the application.
 */
angular
  .module('frontendApp', [
    'ngAnimate',
    'ngCookies',
    'ngResource',
    'ngRoute',
    'ngSanitize',
    'ngTouch'
  ])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/categories', {
        templateUrl: 'views/categories.html',
        controller: 'CategoriesCtrl'
      })
      .when('/monthlyExpenses', {
        templateUrl: 'views/monthlyexpenses.html',
        controller: 'MonthlyexpensesCtrl'
      })
      .when('/weeklyExpenses', {
        templateUrl: 'views/weeklyexpenses.html',
        controller: 'WeeklyexpensesCtrl'
      })
      .when('/totalExpenses', {
        templateUrl: 'views/totalexpenses.html',
        controller: 'TotalexpensesCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });
  });
