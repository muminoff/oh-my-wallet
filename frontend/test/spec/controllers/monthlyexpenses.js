'use strict';

describe('Controller: MonthlyexpensesCtrl', function () {

  // load the controller's module
  beforeEach(module('frontendApp'));

  var MonthlyexpensesCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    MonthlyexpensesCtrl = $controller('MonthlyexpensesCtrl', {
      $scope: scope
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(scope.awesomeThings.length).toBe(3);
  });
});
