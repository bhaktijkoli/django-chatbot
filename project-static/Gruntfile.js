module.exports = function(grunt) {
  // Configuartion
  grunt.initConfig({
    concat: {
      options: {
        stripBanners: true,
      },
      js: {
        src: [
          'src/js/axios.js',
          'src/js/scrollreveal.js',
          'src/js/formhandler.js',
          'src/js/core.js',
        ],
        dest: 'js/app.js'
      }
    },
    watch: {
      files: ['src/sass/*.scss', 'src/js/*.js'],
      tasks: ['sass', 'concat'],
      options: {
        interrupt: true,
      },
    },
    sass: {
      app: {
        files: {
          'css/app.css': 'src/sass/app.scss',
        }
      }
    },
  });

  // Tasks
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-sass');
}
