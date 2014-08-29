'use strict';

describe('Controller: WeeklyexpensesCtrl', function () {

  // load the controller's module
  beforeEach(module('frontendApp'));

  var WeeklyexpensesCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    WeeklyexpensesCtrl = $controller('WeeklyexpensesCtrl', {
      $scope: scope
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(scope.awesomeThings.length).toBe(3);
  });
});
