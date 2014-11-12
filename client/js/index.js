var Chart = require('chart.js/Chart');
var _ = require('underscore');
var $ = require('jquery');

$(document).ready(function() {

  var ctx = $('#half-year')[0].getContext('2d');
  var chart = new Chart(ctx).Pie([]);

  $.get('/data/half-year.json', function(stats) {
    var colors = ['#F7464A', '#46BFBD', '#FDB45C', '#949FB1', '#4D5360'];
    var i = 0;

    _.each(stats, function(stat, user) {
      chart.addData({
        value: stat.added,
        color: colors[i++],
        label: user
      });
    });
  });

});


$(document).ready(function() {

  var ctx = $('#month')[0].getContext('2d');
  var chart = new Chart(ctx).Pie([]);

  $.get('/data/month.json', function(stats) {
    var colors = ['#F7464A', '#46BFBD', '#FDB45C', '#949FB1', '#4D5360'];
    var i = 0;

    _.each(stats, function(stat, user) {
      chart.addData({
        value: stat.added,
        color: colors[i++],
        label: user
      });
    });
  });

});


$(document).ready(function() {

  var ctx = $('#week')[0].getContext('2d');
  var chart = new Chart(ctx).Pie([]);

  $.get('/data/week.json', function(stats) {
    var colors = ['#F7464A', '#46BFBD', '#FDB45C', '#949FB1', '#4D5360'];
    var i = 0;

    _.each(stats, function(stat, user) {
      chart.addData({
        value: stat.added,
        color: colors[i++],
        label: user
      });
    });
  });

});

