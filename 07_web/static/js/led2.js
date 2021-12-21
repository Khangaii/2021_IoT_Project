const led_list = ["red", "blue"];
const state = ["off", "on"];

function led_op(led, op) {
  let url = "/led/".concat(led_list[led], "/", state[op]);
  fetch(url)
  .then(response=>response.text())
  .then(data=> {
    let result = document.querySelector("#result");
    result.innerHTML = data;
  });
}