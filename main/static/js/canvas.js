function newCanvas() {
  var wrapper = document.createElement("div");
  var content = document.createElement("div");
  var canvas = document.createElement("canvas");
  content.appendChild(canvas);
  wrapper.appendChild(content);
  document.querySelector("body").appendChild(wrapper);
  wrapper.id = "canvas-modal";
  wrapper.style.display = "none";
  content.className = "content";
  canvas.style.display = "block";
  canvas.width = 540;
  canvas.height = 430;
  var control = undefined;
  function done() {
    wrapper.style.display = "none";
    var img = document.createElement("img");
    img.width = "150";
    img.src = canvas.toDataURL();
    control.innerHTML = "";
    control.appendChild(img);
    control.value = value;
  }
  var button = document.createElement("button");
  button.className = "save";
  button.innerHTML = "Save and close";
  button.onclick = done;
  content.appendChild(button);
  var margin = 60;
  var r = 40;
  var sx = 60;
  var sy = sx/3*4;
  var ctx = canvas.getContext("2d");
  var n_rows = 5,n_cols = 8, value = [];

  for (j=0;j<n_rows;j++) {
    row = [];
    for (i=0;i<n_cols;i++) {
      row.push(0);
    }
    value.push(row);
  }
  value[2][4] = 1;
  value[1][4] = -1;
  //value[2][3] = -1;
  //value[2][2] = 1;
  //value[3][3] = 1;

  function tick(e) {
    // draw grid
    ctx.clearRect(0,0,canvas.width,canvas.height);
    for (j=0;j<n_rows;j++) {
      for (i=0;i<n_cols;i++) {
        spin = ((i+j)%2==0)?1:-1;
        var x = sx*i+margin,y=sy*j+margin;
        if (e) {
          var dx = x-e.offsetX, dy = y-e.offsetY;
          if (Math.sqrt(dx*dx+dy*dy) < r*0.75) { value[j][i] = value[j][i]?0:spin; }
        }
        ctx.beginPath();
        _t = spin*Math.PI/2;
        if (spin == 1) { y -= sy/4; }
        ctx.moveTo(x+r*Math.cos(_t),y+r*Math.sin(_t));
        ctx.lineTo(x+r*Math.cos(Math.PI*2/3+_t),y+r*Math.sin(Math.PI*2/3+_t));
        ctx.lineTo(x+r*Math.cos(Math.PI*4/3+_t),y+r*Math.sin(Math.PI*4/3+_t));
        ctx.lineTo(x+r*Math.cos(_t),y+r*Math.sin(_t));
        ctx.fillStyle="#333";
        ctx.stroke();
        if (!!value[j][i]) { ctx.fill() };
      }
    }
  }

  tick();
  canvas.onclick = tick;
  function open() {
    wrapper.style.display = "block";
    tick();
  }
  function getControl() {
    control = document.createElement("div");
    control.onclick = open;
    done();
    return control;
  }
  return {
    open: open,
    value: value,
    getControl: getControl,
    getValue: function() { return this.value; }
  }
}

//setTimeout(newCanvas,2000);
