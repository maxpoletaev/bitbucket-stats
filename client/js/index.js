var Chart = require('chart.js/Chart');
var _ = require('underscore');
var $ = require('jquery');

var colors = [
  '#00CC33', '#CCFF00', '#009999', '#336699',
  '#9966CC', '#FF00FF', '#FF3366', '#FF3300',
  'FF9900'
];

// ---

$(document).ready(function() {

  var ctx = $('#changesets-year')[0].getContext('2d');

  var chart = new Chart(ctx).PolarArea([], {
    animation: false
  });

  $.get('/data/commits/year.json', function(stats) {
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

  var ctx = $('#changesets-month')[0].getContext('2d');

  var chart = new Chart(ctx).PolarArea([], {
    animation: false
  });

  $.get('/data/commits/month.json', function(stats) {
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

  var ctx = $('#changesets-week')[0].getContext('2d');

  var chart = new Chart(ctx).PolarArea([], {
    animation: false
  });

  $.get('/data/commits/week.json', function(stats) {
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


// ---

$(document).ready(function() {

  var ctx = $('#commits-year')[0].getContext('2d');

  var chart = new Chart(ctx).PolarArea([], {
    animation: false
  });

  $.get('/data/commits/year.json', function(stats) {
    var i = 0;

    _.each(stats, function(stat, user) {
      chart.addData({
        value: stat.commits,
        color: colors[i++],
        label: user
      });
    });
  });

});


$(document).ready(function() {

  var ctx = $('#commits-month')[0].getContext('2d');

  var chart = new Chart(ctx).PolarArea([], {
    animation: false
  });

  $.get('/data/commits/month.json', function(stats) {
    var i = 0;

    _.each(stats, function(stat, user) {
      chart.addData({
        value: stat.commits,
        color: colors[i++],
        label: user
      });
    });
  });

});


$(document).ready(function() {

  var ctx = $('#commits-week')[0].getContext('2d');

  var chart = new Chart(ctx).PolarArea([], {
    animation: false
  });

  $.get('/data/commits/week.json', function(stats) {
    var i = 0;

    _.each(stats, function(stat, user) {
      chart.addData({
        value: stat.commits,
        color: colors[i++],
        label: user
      });
    });
  });

});
