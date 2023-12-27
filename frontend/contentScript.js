chrome.runtime.onMessage.addListener(function (message, sender, sendResponse) {
  if (message.prediction !== undefined) {
    alert("Prediction: " + message.prediction);
  }
});
