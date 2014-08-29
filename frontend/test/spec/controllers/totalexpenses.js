'use strict';

describe('Controller: TotalexpensesCtrl', function () {

  // load the controller's module
  beforeEach(module('frontendApp'));

  var TotalexpensesCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    TotalexpensesCtrl = $controller('TotalexpensesCtrl', {
      $scope: scope
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(scope.awesomeThings.length).toBe(3);
  });
});
