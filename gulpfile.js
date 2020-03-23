let syntax = 'sass';

const gulp 		        = require('gulp'),
      sass 			      = require('gulp-sass'),
      concat        	= require('gulp-concat'),
      uglify        	= require('gulp-uglify-es').default,
      cleancss      	= require('gulp-clean-css'),
      rename			    = require('gulp-rename'),
      autoprefixer  	= require('gulp-autoprefixer'),
      notify        	= require('gulp-notify'),
      livereload 	  	= require('gulp-livereload');

gulp.task('styles', function() {
  return gulp.src('./static/assets/'+syntax+'/**/*.'+syntax)
    .pipe(sass({ outputStyle: 'expanded' }).on('error', notify.onError()))
    .pipe(rename({ suffix: '.min', prefix : '' }))
    .pipe(autoprefixer(['last 15 versions']))
    .pipe(cleancss( {level: { 1: { specialComments: 0 } } }))
    .pipe(gulp.dest('./static/assets/css'))
    .pipe(livereload());
});

gulp.task('scripts', function() {
  return gulp.src([
    './static/assets/libs/jquery/dist/jquery.min.js',
    './static/assets/js/**/*.js'
  ])
    .pipe(concat('scripts.min.js'))
    .pipe(uglify())
    .pipe(gulp.dest('./static/assets/dist-js'))
    .pipe(livereload());
});

gulp.task('watch',  function() {
  livereload.listen();
  gulp.watch('./static/assets/'+syntax+'/**/*.'+syntax, gulp.parallel('styles'));
  gulp.watch([
      './static/assets/libs/**/*.js', 
      './static/assets/js/**/*.js'
    ], gulp.parallel('scripts'));
  gulp.watch('./templates/**/*.html').on('change', livereload.changed);
});

gulp.task('default', gulp.parallel('styles', 'scripts', 'watch'));