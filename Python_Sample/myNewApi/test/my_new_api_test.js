var assert = require("chai").assert;
var myNewAp = require("../lib/my_new_api.js");
describe("myNewApi",function(){it("exports handleRequest",function(){assert.typeOf(myNewApi.handleRequest,"function");});});
