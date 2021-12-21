function led_op(op) {
  let url = (op == 1) ? "/led/on" : "/led/off";
  fetch(url)
  .then(response=>response.text())
  .then(data=> {
    let result = document.querySelector("#result");
    result.innerHTML = "<h1>" + data + "</h1>";
  });
}
