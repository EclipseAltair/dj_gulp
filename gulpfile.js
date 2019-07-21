var syntax = 'sass';

var gulp 		      	= require('gulp'),
    sass 			      = require('gulp-sass'),
    concat        	= require('gulp-concat'),
    cleancss      	= require('gulp-clean-css'),
    rename			    = require('gulp-rename'),
    autoprefixer  	= require('gulp-autoprefixer'),
    notify        	= require('gulp-notify'),
    livereload 	  	= require('gulp-livereload');

gulp.task('styles', function() { // Создаем таск Sass
  return gulp.src('./static/assets/'+syntax+'/**/*.'+syntax) // Берем источник
    .pipe(sass({ outputStyle: 'expanded' }).on('error', notify.onError())) // Преобразуем Sass в CSS посредством gulp-sass
    .pipe(rename({ suffix: '.min', prefix : '' }))
    .pipe(autoprefixer(['last 15 versions']))
    .pipe(cleancss( {level: { 1: { specialComments: 0 } } })) // Закомментить при дебаге
    .pipe(gulp.dest('./static/assets/css')) // Выгружаем результат в папку static/assets/css
    .pipe(livereload());
});

gulp.task('scripts', function() {
  return gulp.src([ // Берем все необходимые библиотеки
    './static/assets/libs/jquery/jquery.min.js', // Берем jQuery
    './static/assets/libs/slick/slick.js',
    './static/assets/js/common.js'
  ])
    .pipe(concat('scripts.min.js')) // Собираем их в кучу в новом файле scripts.min.js
  // .pipe(uglify()) // Сжимаем JS файл, Mifify js (opt.)
    .pipe(gulp.dest('./static/assets/js')) // Выгружаем в папку static/assets/js
    .pipe(livereload());
});

gulp.task('watch',  function() {
  livereload.listen();
  gulp.watch('./static/assets/'+syntax+'/**/*.'+syntax, gulp.parallel('styles'));
  gulp.watch(['./static/assets/libs/**/*.js', './static/assets/js/common.js'], gulp.parallel('scripts'));
  gulp.watch('./templates/**/*.html').on('change', livereload.changed);
});

gulp.task('default', gulp.parallel('styles', 'scripts', 'watch'));