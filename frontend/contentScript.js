chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
  alert(request.result);
});
