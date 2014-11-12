var gulp = require('gulp');
var stylus = require('gulp-stylus');
var concat = require('gulp-concat');
var buffer = require('vinyl-buffer');
var browserify = require('browserify');
var stream = require('vinyl-source-stream');

var source = {
  js: [
    './client/js/index.js'
  ],
  css: [
    './client/inc/reset.css',
    './client/css/*.styl'
  ]
};

var config = {
  browserify: {
    entries: source.js
  },
  stylus: {}
};

gulp.task('js', function() {
  return browserify(config.browserify)
    .bundle()
    .pipe(stream('app.js'))
    .pipe(buffer())
    .pipe(gulp.dest('public/assets/js'));
});

gulp.task('css', function() {
  return gulp.src(source.css)
    .pipe(stylus(config.stylus))
    .pipe(concat('app.css'))
    .pipe(gulp.dest('./public/assets/css'));
});

gulp.task('default', ['css', 'js']);
