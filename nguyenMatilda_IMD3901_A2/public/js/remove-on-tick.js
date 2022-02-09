'use strict';



entityEl.parentNode.removeChild(entityEl);


var sphere = document.querySelector('a-sphere');
sphere.parentNode.removeChild(sphere);

//this component will basically just toggle off/on the spinning of the walls
AFRAME.registerComponent('remove-on-tick', {
  tick: function () {
    var sphere = this.el;
    if (condition) {
      entity.parentNode.removeChild(sphere);
    }
  }
});


 //component documentation: https://github.com/aframevr/aframe/blob/master/docs/core/component.md
  
  // update: function (oldData) {},
  // tick: function(time, timeDelta) {},
  // tock: function(time, timeDelta) {},
  // remove: function() {},
  // pause: function() {},
  // play: function() {},
  // updateScheme: function(data) {}