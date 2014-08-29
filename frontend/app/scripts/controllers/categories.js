'use strict';

/**
 * @ngdoc function
 * @name frontendApp.controller:CategoriesCtrl
 * @description
 * # CategoriesCtrl
 * Controller of the frontendApp
 */
angular.module('frontendApp')
  .controller('CategoriesCtrl', function ($scope) {
    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
  });
